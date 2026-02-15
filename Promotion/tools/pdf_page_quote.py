#!/usr/bin/env python3
import argparse
import re
import subprocess
import sys


def run(cmd: list[str]) -> str:
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(e.output.decode("utf-8", errors="replace")) from e
    return out.decode("utf-8", errors="replace")


def page_count(pdf_path: str) -> int:
    out = run(["pdfinfo", pdf_path])
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError("Could not determine page count via pdfinfo")


def extract_page_text(pdf_path: str, page: int) -> str:
    return run(
        [
            "pdftotext",
            "-f",
            str(page),
            "-l",
            str(page),
            "-layout",
            pdf_path,
            "-",
        ]
    )


def excerpt(text: str, match_span: tuple[int, int], context_chars: int) -> str:
    start = max(0, match_span[0] - context_chars)
    end = min(len(text), match_span[1] + context_chars)
    snippet = text[start:end]
    snippet = re.sub(r"[ \t]+", " ", snippet)
    snippet = re.sub(r"\n{3,}", "\n\n", snippet)
    return snippet.strip()


def find_first(pdf_path: str, pattern: re.Pattern, context_chars: int, start_page: int, end_page: int):
    for page in range(start_page, end_page + 1):
        text = extract_page_text(pdf_path, page)
        m = pattern.search(text)
        if not m:
            continue
        return {
            "page": page,
            "match": m.group(0),
            "excerpt": excerpt(text, m.span(), context_chars),
        }
    return None


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Find first occurrence of a regex in a PDF and report page + excerpt."
    )
    ap.add_argument("pdf", help="Path to PDF")
    ap.add_argument("regex", help="Python regex (case-insensitive by default)")
    ap.add_argument("--case-sensitive", action="store_true", help="Do not ignore case")
    ap.add_argument("--context", type=int, default=220, help="Context chars for excerpt")
    ap.add_argument("--start-page", type=int, default=1, help="Start page (1-based)")
    ap.add_argument("--end-page", type=int, default=0, help="End page (1-based, 0=last)")
    args = ap.parse_args()

    flags = 0 if args.case_sensitive else re.IGNORECASE
    try:
        pattern = re.compile(args.regex, flags=flags)
    except re.error as e:
        print(f"Invalid regex: {e}", file=sys.stderr)
        return 2

    total = page_count(args.pdf)
    end_page = total if args.end_page <= 0 else min(args.end_page, total)
    start_page = max(1, min(args.start_page, end_page))

    result = find_first(args.pdf, pattern, args.context, start_page, end_page)
    if not result:
        print("NO_MATCH")
        return 1

    print(f"PAGE\t{result['page']}")
    print(f"MATCH\t{result['match']}")
    print("EXCERPT\t" + result["excerpt"].replace("\n", "\\n"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

