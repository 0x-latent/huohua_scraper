"""Export helpers for tabular crawler results."""

import re
from pathlib import Path
from typing import Any

from .dependencies import ensure_openpyxl

ILLEGAL_EXCEL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def clean_excel_value(value: Any) -> Any:
    if isinstance(value, str):
        return ILLEGAL_EXCEL_RE.sub("", value)
    return value


def save_rows_to_excel(rows: list[dict], filename: str | Path, sheet_name: str = "数据") -> None:
    openpyxl = ensure_openpyxl()
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = sheet_name

    if not rows:
        print("没有数据可保存")
        return

    headers: list[str] = []
    seen = set()
    for row in rows:
        for key in row.keys():
            if key not in seen:
                headers.append(key)
                seen.add(key)

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = openpyxl.styles.Font(bold=True)

    for row_idx, row_data in enumerate(rows, 2):
        for col, header in enumerate(headers, 1):
            ws.cell(row=row_idx, column=col, value=clean_excel_value(row_data.get(header, "")))

    for col_idx, header in enumerate(headers, 1):
        letter = openpyxl.utils.get_column_letter(col_idx)
        ws.column_dimensions[letter].width = max(len(str(header)) * 2 + 4, 12)

    wb.save(filename)
    print(f"数据已保存到: {filename}")
