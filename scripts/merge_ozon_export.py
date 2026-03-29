"""Merge Ozon seller export (Товары) with content CSVs for image URLs. Run from repo root."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


def norm_articul(value: str) -> str:
    if not value:
        return ""
    s = value.strip().strip('"').strip("'")
    return s


def load_content_images(repo: Path) -> dict[str, str]:
    images: dict[str, str] = {}
    files = [
        repo / "items" / "Запчасти для легковых автомобилей_29.03.2026.csv",
        repo / "items" / "Запчасти системы зажигания грузовика_29.03.2026.csv",
    ]
    for path in files:
        if not path.exists():
            continue
        with path.open(encoding="cp1251", newline="") as f:
            for row in csv.reader(f, delimiter=";"):
                if len(row) < 15:
                    continue
                art = row[1].strip()
                if not art.startswith("Neodim_"):
                    continue
                main = row[14].strip().split("\n")[0].strip().strip('"')
                if main.startswith("https://"):
                    images[art] = main
    return images


def merge(repo: Path) -> dict[str, dict]:
    products_path = repo / "items" / "Товары_29.03.2026.csv"
    images = load_content_images(repo)
    merged: dict[str, dict] = {}

    with products_path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            art = norm_articul(row.get("Артикул", ""))
            sku = norm_articul(row.get("SKU", ""))
            title = norm_articul(row.get("Название товара", ""))
            if not art:
                continue
            merged[art] = {
                "sku": sku,
                "title": title,
                "image": images.get(art, ""),
                "url": f"https://www.ozon.ru/product/{sku}/" if sku else "",
            }
    return merged


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    data = merge(repo)
    missing = [k for k, v in data.items() if not v["image"]]
    if missing:
        print("missing images:", ", ".join(missing), file=sys.stderr)
    out = repo / "scripts" / "ozon_merged.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(data)} rows to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
