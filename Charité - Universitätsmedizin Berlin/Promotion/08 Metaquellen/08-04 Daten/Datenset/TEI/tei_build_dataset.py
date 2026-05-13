#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd


_RE_FILLED = re.compile(r"Ausgefüllte Feedbacks:\s*(\d+)", re.IGNORECASE)
_RE_QUESTIONS = re.compile(r"Fragen:\s*(\d+)", re.IGNORECASE)
_RE_EVAL_NUM = re.compile(r"Evaluation-(\d+)\.csv$", re.IGNORECASE)


@dataclass(frozen=True)
class ExportMeta:
    source_file: str
    evaluation_number: int
    timestamp_raw: str | None
    filled_feedbacks: int | None
    questions_count: int | None


def _cell_str(value: Any) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return ""
    return str(value).strip()


def _parse_int(value: Any) -> int | None:
    s = _cell_str(value)
    if not s:
        return None
    try:
        return int(s)
    except Exception:
        match = re.search(r"(\d+)", s)
        return int(match.group(1)) if match else None


def _parse_float_de(value: Any) -> float | None:
    s = _cell_str(value)
    if not s:
        return None
    # exported means use comma as decimal separator
    s = s.replace(".", "").replace(",", ".") if re.search(r"\d+,\d+", s) else s
    try:
        return float(s)
    except Exception:
        return None


def read_export_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(
        path,
        sep=";",
        header=None,
        engine="python",
        dtype=str,
        encoding="utf-8-sig",
    )


def parse_meta(path: Path, raw: pd.DataFrame) -> ExportMeta:
    match = _RE_EVAL_NUM.search(path.name)
    if not match:
        raise ValueError(f"Unrecognized TEI export filename: {path.name}")
    evaluation_number = int(match.group(1))

    timestamp_raw = _cell_str(raw.iat[0, 0]) if raw.shape[0] and raw.shape[1] else None
    if timestamp_raw == "":
        timestamp_raw = None

    filled_feedbacks = None
    questions_count = None
    for row_idx in range(min(20, raw.shape[0])):
        s = _cell_str(raw.iat[row_idx, 0])
        if not s:
            continue
        filled_match = _RE_FILLED.search(s)
        if filled_match:
            filled_feedbacks = int(filled_match.group(1))
        questions_match = _RE_QUESTIONS.search(s)
        if questions_match:
            questions_count = int(questions_match.group(1))

    return ExportMeta(
        source_file=path.name,
        evaluation_number=evaluation_number,
        timestamp_raw=timestamp_raw,
        filled_feedbacks=filled_feedbacks,
        questions_count=questions_count,
    )


def find_header_row(raw: pd.DataFrame) -> int:
    for row_idx in range(raw.shape[0]):
        row = [_cell_str(v) for v in raw.iloc[row_idx].tolist()]
        if "Bezeichner" in row and "Frage" in row:
            return row_idx
    raise ValueError("Could not find table header row (Bezeichner/Frage).")


def build_items_from_first_file(raw: pd.DataFrame) -> pd.DataFrame:
    header_row = find_header_row(raw)
    item_rows = []
    item_idx = 0
    row_idx = header_row + 1
    while row_idx + 1 < raw.shape[0]:
        question = _cell_str(raw.iat[row_idx, 1]) if raw.shape[1] > 1 else ""
        if not question:
            row_idx += 1
            continue
        item_idx += 1
        item_rows.append({"item_index": item_idx, "question_text": question})
        row_idx += 2
    return pd.DataFrame(item_rows)


def extract_long_and_means(meta: ExportMeta, raw: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    header_row = find_header_row(raw)

    long_rows = []
    mean_rows = []

    item_index = 0
    row_idx = header_row + 1
    while row_idx + 1 < raw.shape[0]:
        question = _cell_str(raw.iat[row_idx, 1]) if raw.shape[1] > 1 else ""
        if not question:
            row_idx += 1
            continue

        counts_row_idx = row_idx + 1
        item_index += 1

        # response labels are in row_idx across columns 2..8, mean in last col (typically 8)
        response_labels = []
        mean_col_idx = None
        for col_idx in range(2, raw.shape[1]):
            label = _cell_str(raw.iat[row_idx, col_idx])
            if not label:
                continue
            if label.lower() == "mittelwert":
                mean_col_idx = col_idx
                continue
            response_labels.append((col_idx, label))

        # Case A: Likert item with counts
        total_n = 0
        if response_labels:
            for col_idx, label in response_labels:
                count = _parse_int(raw.iat[counts_row_idx, col_idx])
                if count is None:
                    continue
                score_match = re.search(r"\((\d+)\)", label)
                score = int(score_match.group(1)) if score_match else None
                long_rows.append(
                    {
                        "evaluation_number": meta.evaluation_number,
                        "source_file": meta.source_file,
                        "timestamp_raw": meta.timestamp_raw,
                        "filled_feedbacks": meta.filled_feedbacks,
                        "questions_count": meta.questions_count,
                        "item_index": item_index,
                        "question_text": question,
                        "response_label": label,
                        "response_score": score,
                        "count": count,
                    }
                )
                total_n += count

            mean_exported = (
                _parse_float_de(raw.iat[counts_row_idx, mean_col_idx]) if mean_col_idx is not None else None
            )
        else:
            # Case B: Open-ended item (freitext) exported as raw text lines below the question.
            # Convention observed in exports: comments are in column 2, with empty col1.
            freitext_count = 0
            scan_idx = counts_row_idx
            while scan_idx < raw.shape[0]:
                # stop if a new Likert header is detected (question in col1 and response labels in col2)
                col1 = _cell_str(raw.iat[scan_idx, 1]) if raw.shape[1] > 1 else ""
                col2 = _cell_str(raw.iat[scan_idx, 2]) if raw.shape[1] > 2 else ""
                if col1 and col2.lower().startswith("trifft"):
                    break

                if col2:
                    freitext_count += 1
                scan_idx += 1

            long_rows.append(
                {
                    "evaluation_number": meta.evaluation_number,
                    "source_file": meta.source_file,
                    "timestamp_raw": meta.timestamp_raw,
                    "filled_feedbacks": meta.filled_feedbacks,
                    "questions_count": meta.questions_count,
                    "item_index": item_index,
                    "question_text": question,
                    "response_label": "Freitext",
                    "response_score": 0,
                    "count": freitext_count,
                }
            )
            total_n = freitext_count
            mean_exported = None

        mean_rows.append(
            {
                "evaluation_number": meta.evaluation_number,
                "source_file": meta.source_file,
                "timestamp_raw": meta.timestamp_raw,
                "filled_feedbacks": meta.filled_feedbacks,
                "questions_count": meta.questions_count,
                "item_index": item_index,
                "question_text": question,
                "n": total_n,
                "mean_exported": mean_exported,
            }
        )

        row_idx += 2

    return pd.DataFrame(long_rows), pd.DataFrame(mean_rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build consolidated TEI dataset tables from TEI export CSVs.")
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("08 Metaquellen/08-04 Daten/Datenset/TEI"),
        help="Directory containing TEI export CSVs.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory to write consolidated CSVs (defaults to input dir).",
    )
    args = parser.parse_args()

    input_dir: Path = args.input_dir
    output_dir: Path = args.output_dir or input_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    export_files = sorted(input_dir.glob("*Evaluation-*.csv"))
    if not export_files:
        raise SystemExit(f"No TEI export CSVs found in {input_dir}")

    metas: list[dict[str, Any]] = []
    long_parts: list[pd.DataFrame] = []
    mean_parts: list[pd.DataFrame] = []

    first_raw = None
    for path in export_files:
        raw = read_export_csv(path)
        meta = parse_meta(path, raw)
        metas.append(meta.__dict__)
        if first_raw is None:
            first_raw = raw
        long_df, mean_df = extract_long_and_means(meta, raw)
        long_parts.append(long_df)
        mean_parts.append(mean_df)

    df_meta = pd.DataFrame(metas).sort_values("evaluation_number")
    df_long = pd.concat(long_parts, ignore_index=True).sort_values(
        ["evaluation_number", "item_index", "response_score"], na_position="last"
    )
    df_means = pd.concat(mean_parts, ignore_index=True).sort_values(["evaluation_number", "item_index"])

    df_items = build_items_from_first_file(first_raw) if first_raw is not None else pd.DataFrame()

    df_meta.to_csv(output_dir / "tei_export_meta.csv", index=False)
    df_items.to_csv(output_dir / "tei_items.csv", index=False)
    df_long.to_csv(output_dir / "tei_counts_long.csv", index=False)
    df_means.to_csv(output_dir / "tei_item_means.csv", index=False)

    print(f"Wrote {output_dir / 'tei_export_meta.csv'} ({len(df_meta)} rows)")
    print(f"Wrote {output_dir / 'tei_items.csv'} ({len(df_items)} rows)")
    print(f"Wrote {output_dir / 'tei_counts_long.csv'} ({len(df_long)} rows)")
    print(f"Wrote {output_dir / 'tei_item_means.csv'} ({len(df_means)} rows)")


if __name__ == "__main__":
    main()
