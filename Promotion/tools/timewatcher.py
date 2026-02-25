#!/usr/bin/env python3
"""
Timewatcher report for the dissertation workflow.

This script is read-only. It aggregates:
- Git working tree status (dirty/untracked)
- #todo markers in Promotion/04 Kapitelstruktur
- GitHub issue metadata (via `gh`)

Typical use (from repo root or any subdir):
  python3 Promotion/tools/timewatcher.py
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import os
import re
import subprocess
import sys
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


@dataclasses.dataclass(frozen=True)
class TodoRef:
    path: str
    line: int
    text: str
    issue_number: Optional[int]
    todo_date: Optional[dt.date]


def run(cmd: Sequence[str], *, cwd: Optional[str] = None) -> str:
    try:
        out = subprocess.check_output(list(cmd), stderr=subprocess.STDOUT, cwd=cwd)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(e.output.decode("utf-8", errors="replace")) from e
    return out.decode("utf-8", errors="replace")


def try_run(cmd: Sequence[str], *, cwd: Optional[str] = None) -> Tuple[int, str]:
    p = subprocess.run(
        list(cmd),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=cwd,
        text=True,
    )
    return p.returncode, p.stdout


def git_root() -> str:
    return run(["git", "rev-parse", "--show-toplevel"]).strip()


def parse_github_repo(remote_url: str) -> Optional[str]:
    # Supports:
    # - git@github.com:OWNER/REPO.git
    # - https://github.com/OWNER/REPO.git
    # - https://github.com/OWNER/REPO
    s = remote_url.strip()
    m = re.search(r"github\.com[:/](?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?$", s)
    if not m:
        return None
    return f"{m.group('owner')}/{m.group('repo')}"


def detect_repo_slug(repo_override: str) -> str:
    if repo_override:
        return repo_override
    rc, out = try_run(["git", "config", "--get", "remote.origin.url"])
    if rc == 0:
        slug = parse_github_repo(out.strip())
        if slug:
            return slug
    return "jochen-hanisch/research"


def git_status_porcelain(repo_top: str) -> List[str]:
    rc, out = try_run(["git", "status", "-sb", "--porcelain"], cwd=repo_top)
    if rc != 0:
        return []
    return [line.rstrip("\n") for line in out.splitlines() if line.strip()]


def extract_todos_with_rg(repo_top: str) -> Iterable[Tuple[str, int, str]]:
    target_dir = os.path.join(repo_top, "Promotion", "04 Kapitelstruktur")
    rc, out = try_run(["rg", "-n", "#todo", "-S", target_dir], cwd=repo_top)
    if rc not in (0, 1):  # 1 = no matches
        raise RuntimeError(out.strip() or "rg failed")
    for line in out.splitlines():
        # format: path:line:text
        parts = line.split(":", 2)
        if len(parts) != 3:
            continue
        path, line_s, text = parts
        try:
            n = int(line_s)
        except ValueError:
            continue
        yield path, n, text


def extract_todos_fallback(repo_top: str) -> Iterable[Tuple[str, int, str]]:
    base = os.path.join(repo_top, "Promotion", "04 Kapitelstruktur")
    for root, _dirs, files in os.walk(base):
        for fn in files:
            if not fn.lower().endswith(".md"):
                continue
            p = os.path.join(root, fn)
            try:
                with open(p, "r", encoding="utf-8") as f:
                    for idx, line in enumerate(f, start=1):
                        if "#todo" in line:
                            yield p, idx, line.rstrip("\n")
            except OSError:
                continue


ISSUE_RE = re.compile(r"#todo\s*\(\s*#(?P<num>\d+)", re.IGNORECASE)
DATE_RE = re.compile(r"#todo\s*\(\s*#\d+\s*,\s*(?P<date>\d{4}-\d{2}-\d{2})", re.IGNORECASE)


def parse_todo(path: str, line: int, text: str) -> TodoRef:
    issue_number: Optional[int] = None
    todo_date: Optional[dt.date] = None

    m = ISSUE_RE.search(text)
    if m:
        issue_number = int(m.group("num"))

    d = DATE_RE.search(text)
    if d:
        try:
            todo_date = dt.date.fromisoformat(d.group("date"))
        except ValueError:
            todo_date = None

    return TodoRef(path=path, line=line, text=text.strip(), issue_number=issue_number, todo_date=todo_date)


def gh_issues(repo: str, limit: int) -> Dict[int, dict]:
    out = run(
        [
            "gh",
            "issue",
            "list",
            "-R",
            repo,
            "--state",
            "all",
            "--limit",
            str(limit),
            "--json",
            "number,title,state,updatedAt,url,labels",
        ]
    )
    rows = json.loads(out)
    by_number: Dict[int, dict] = {}
    for r in rows:
        try:
            by_number[int(r["number"])] = r
        except Exception:
            continue
    return by_number


def gh_issue_body(repo: str, number: int) -> Optional[str]:
    rc, out = try_run(["gh", "issue", "view", str(number), "-R", repo, "--json", "body"])
    if rc != 0:
        return None
    try:
        j = json.loads(out)
    except json.JSONDecodeError:
        return None
    body = j.get("body")
    return str(body) if body is not None else None


def cache_path(repo_top: str) -> str:
    # IMPORTANT: Do not write caches into the git working tree. Automations often run in
    # separate worktrees; writing under repo_top would create drift/untracked changes.
    slug = "repo"
    try:
        origin_rc, origin_out = try_run(["git", "config", "--get", "remote.origin.url"], cwd=repo_top)
        if origin_rc == 0:
            parsed = parse_github_repo(origin_out.strip())
            if parsed:
                slug = parsed.replace("/", "__")
    except Exception:
        pass

    codex_home = os.environ.get("CODEX_HOME") or os.path.join(os.path.expanduser("~"), ".codex")
    return os.path.join(codex_home, "tmp", f"timewatcher_cache_{slug}.json")


def load_cache(repo_top: str) -> Optional[dict]:
    p = cache_path(repo_top)
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return None


def save_cache(repo_top: str, cache: dict) -> None:
    p = cache_path(repo_top)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2, sort_keys=True)
    os.replace(tmp, p)


def gh_project(repo_owner: str, number: int) -> Optional[dict]:
    rc, out = try_run(["gh", "project", "view", str(number), "--owner", repo_owner, "--format", "json"])
    if rc != 0:
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return None


def owner_from_repo(repo: str) -> str:
    return repo.split("/", 1)[0] if "/" in repo else repo


def format_issue_short(issue: dict) -> str:
    n = issue.get("number", "?")
    state = issue.get("state", "?")
    title = (issue.get("title") or "").strip()
    return f"#{n} [{state}] {title}"


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate a local Timewatcher report (Git + GitHub + #todo).")
    ap.add_argument("--repo", default="", help="GitHub repo slug (owner/name). Default: detected from origin.")
    ap.add_argument(
        "--today",
        default="",
        help="Override today's date (YYYY-MM-DD). Default: local system date.",
    )
    ap.add_argument(
        "--no-gh",
        action="store_true",
        help="Do not call GitHub (use cached data if available).",
    )
    ap.add_argument("--issue-limit", type=int, default=500, help="Max issues to fetch via gh (default: 500).")
    ap.add_argument("--project", type=int, default=14, help="GitHub Project number to show (default: 14).")
    ap.add_argument(
        "--roadmap-issue",
        type=int,
        default=71,
        help="Issue number that contains the roadmap (used to order Next Actions). Default: 71.",
    )
    args = ap.parse_args()

    if args.today:
        try:
            today = dt.date.fromisoformat(args.today)
        except ValueError:
            print(f"ERROR: Invalid --today value: {args.today!r} (expected YYYY-MM-DD)", file=sys.stderr)
            return 2
    else:
        today = dt.date.today()
    repo_top = git_root()
    repo = detect_repo_slug(args.repo)
    cache_p = cache_path(repo_top)

    status_lines = git_status_porcelain(repo_top)
    untracked = [l for l in status_lines if l.startswith("?? ")]

    # Todos
    todos_raw: List[Tuple[str, int, str]] = []
    try:
        todos_raw = list(extract_todos_with_rg(repo_top))
    except Exception:
        todos_raw = list(extract_todos_fallback(repo_top))

    todos = [parse_todo(p, n, t) for (p, n, t) in todos_raw]
    todos_with_issue = [t for t in todos if t.issue_number is not None]
    todos_without_issue = [t for t in todos if t.issue_number is None]

    referenced: Set[int] = {t.issue_number for t in todos_with_issue if t.issue_number is not None}

    # GitHub
    github_status = "UNAVAILABLE"
    github_reason = ""
    issues_source = "none"

    cached = load_cache(repo_top) or {}
    issues_by_number: Dict[int, dict] = {}
    roadmap_body: Optional[str] = None

    if not args.no_gh:
        try:
            issues_by_number = gh_issues(repo, limit=int(args.issue_limit))
            github_status = "AVAILABLE"
            issues_source = "live"
        except Exception as e:
            github_reason = str(e).strip()

    if issues_by_number:
        cached = {
            "repo": repo,
            "fetched_at": dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc).isoformat(),
            "issues_by_number": issues_by_number,
            "roadmap_issue": int(args.roadmap_issue),
            "roadmap_body": None,
        }

    if not issues_by_number and isinstance(cached.get("issues_by_number"), dict):
        try:
            issues_by_number = {int(k): v for (k, v) in cached["issues_by_number"].items()}
            issues_source = "cache"
        except Exception:
            issues_by_number = {}

    if not args.no_gh:
        roadmap_body = gh_issue_body(repo, int(args.roadmap_issue))
        if roadmap_body and cached:
            cached["roadmap_issue"] = int(args.roadmap_issue)
            cached["roadmap_body"] = roadmap_body
    if not roadmap_body and isinstance(cached.get("roadmap_body"), str):
        roadmap_body = cached["roadmap_body"]

    if cached and (issues_source == "live" or (roadmap_body and cached.get("roadmap_body") == roadmap_body)):
        try:
            save_cache(repo_top, cached)
        except OSError:
            pass

    missing_in_github: List[int] = []
    open_referenced: List[dict] = []
    if issues_by_number:
        missing_in_github = sorted(n for n in referenced if n not in issues_by_number)
        for n in sorted(referenced):
            issue = issues_by_number.get(n)
            if not issue:
                continue
            if issue.get("state") == "OPEN":
                open_referenced.append(issue)

    roadmap_order: List[int] = []
    if roadmap_body:
        seen: Set[int] = set()
        for m in re.finditer(r"#(\d+)", roadmap_body):
            n = int(m.group(1))
            if n in seen:
                continue
            seen.add(n)
            roadmap_order.append(n)

    # Date-based triage
    overdue: List[TodoRef] = []
    upcoming: List[TodoRef] = []
    for t in todos:
        if not t.todo_date:
            continue
        if t.todo_date < today:
            overdue.append(t)
        elif t.todo_date <= (today + dt.timedelta(days=7)):
            upcoming.append(t)

    def todo_sort_key(t: TodoRef) -> Tuple[dt.date, str, int]:
        return (t.todo_date or dt.date.max, t.path, t.line)

    overdue.sort(key=todo_sort_key)
    upcoming.sort(key=todo_sort_key)

    # Project (optional)
    project = gh_project(owner_from_repo(repo), int(args.project))

    print("TIMEWATCHER_REPORT")
    print(f"DATE\t{today.isoformat()}")
    if args.today:
        print("DATE_SOURCE\toverride")
    else:
        print("DATE_SOURCE\tsystem")
    print(f"REPO\t{repo}")
    print(f"REPO_TOP\t{repo_top}")
    print(f"CACHE_PATH\t{cache_p}")
    if project and project.get("url"):
        print(f"PROJECT\t{project.get('title','').strip()}\t{project.get('url')}")
        try:
            items_total = project["items"]["totalCount"]
            print(f"PROJECT_ITEMS\t{items_total}")
        except Exception:
            pass
    if roadmap_body:
        print(f"ROADMAP_ISSUE\t#{int(args.roadmap_issue)}")
    print(f"GITHUB_STATUS\t{github_status}")
    if issues_source != "none":
        print(f"GITHUB_ISSUES_SOURCE\t{issues_source}")
    if github_reason and github_status != "AVAILABLE":
        print(f"GITHUB_REASON\t{github_reason.replace(chr(9), ' ').replace(chr(10), ' ')[:240]}")

    print("")
    print("GIT_STATUS")
    if not status_lines:
        print("CLEAN_OR_UNKNOWN")
    else:
        print(f"CHANGES\t{len(status_lines)}")
        print(f"UNTRACKED\t{len(untracked)}")
        for l in untracked[:10]:
            print(f"UNTRACKED_ITEM\t{l[3:]}")
        if len(untracked) > 10:
            print(f"UNTRACKED_MORE\t{len(untracked) - 10}")

    print("")
    print("TODOS")
    print(f"TOTAL\t{len(todos)}")
    print(f"WITH_ISSUE\t{len(todos_with_issue)}")
    print(f"WITHOUT_ISSUE\t{len(todos_without_issue)}")
    if todos_without_issue:
        for t in todos_without_issue[:10]:
            print(f"TODO_NO_ISSUE\t{t.path}:{t.line}\t{t.text}")
        if len(todos_without_issue) > 10:
            print(f"TODO_NO_ISSUE_MORE\t{len(todos_without_issue) - 10}")

    print("")
    print("GITHUB_ISSUES")
    print(f"REFERENCED_UNIQUE\t{len(referenced)}")
    if issues_by_number:
        print(f"REFERENCED_OPEN\t{len(open_referenced)}")
        print(f"MISSING_IN_GITHUB\t{len(missing_in_github)}")
        for n in missing_in_github[:10]:
            print(f"MISSING_ISSUE\t#{n}")
        if len(missing_in_github) > 10:
            print(f"MISSING_ISSUE_MORE\t{len(missing_in_github) - 10}")
    else:
        print("REFERENCED_OPEN\tUNKNOWN")
        print("MISSING_IN_GITHUB\tUNKNOWN")

    print("")
    print("TRIAGE")
    if overdue:
        print(f"OVERDUE\t{len(overdue)}")
        for t in overdue[:10]:
            num = f"#{t.issue_number}" if t.issue_number is not None else "NO_ISSUE"
            print(f"OVERDUE_ITEM\t{t.todo_date.isoformat()}\t{num}\t{t.path}:{t.line}\t{t.text}")
        if len(overdue) > 10:
            print(f"OVERDUE_MORE\t{len(overdue) - 10}")
    else:
        print("OVERDUE\t0")

    if upcoming:
        print(f"UPCOMING_7D\t{len(upcoming)}")
        for t in upcoming[:10]:
            num = f"#{t.issue_number}" if t.issue_number is not None else "NO_ISSUE"
            print(f"UPCOMING_ITEM\t{t.todo_date.isoformat()}\t{num}\t{t.path}:{t.line}\t{t.text}")
        if len(upcoming) > 10:
            print(f"UPCOMING_MORE\t{len(upcoming) - 10}")
    else:
        print("UPCOMING_7D\t0")

    # A short "next actions" suggestion list based on open referenced issues
    print("")
    print("NEXT_ACTIONS")
    open_by_number = {int(i.get("number")): i for i in open_referenced if i.get("number") is not None}

    emitted: Set[int] = set()
    for n in roadmap_order:
        issue = open_by_number.get(n)
        if not issue:
            continue
        emitted.add(n)
        print(f"OPEN_ISSUE\t{format_issue_short(issue)}\t{issue.get('url','')}")
        if len(emitted) >= 10:
            break

    if not emitted:
        # Fallback: suggest the most relevant TODO-issues based on file location + date.
        def section_priority(path: str) -> int:
            p = path.lower()
            if "04-05 ergebnisse" in p:
                return 1
            if "04-06 diskussion" in p:
                return 2
            if "04-07 conclusio" in p:
                return 3
            if "04-04 methodologie" in p:
                return 4
            if "04-02 theorieteil" in p:
                return 5
            if "04-03 forschungsgegenstand" in p:
                return 6
            if "04-01 einleitung" in p:
                return 7
            return 99

        def fallback_key(t: TodoRef) -> Tuple[int, dt.date, str, int]:
            return (section_priority(t.path), t.todo_date or dt.date.max, t.path, t.line)

        for t in sorted(todos_with_issue, key=fallback_key):
            if t.issue_number is None:
                continue
            if t.issue_number in emitted:
                continue
            emitted.add(t.issue_number)
            print(f"TODO_ISSUE_REF\t#{t.issue_number}\t{t.path}:{t.line}\t{t.text}")
            if len(emitted) >= 10:
                break

    if len(emitted) < 10:
        for issue in open_referenced:
            n = int(issue.get("number"))
            if n in emitted:
                continue
            emitted.add(n)
            print(f"OPEN_ISSUE\t{format_issue_short(issue)}\t{issue.get('url','')}")
            if len(emitted) >= 10:
                break

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
