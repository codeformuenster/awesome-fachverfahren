#!/usr/bin/env python3
"""Aggregate YAML fachverfahren into docs/data.json"""
import json
import os
from glob import glob

import yaml


def main():
    base = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base, "data", "fachverfahren")
    out_dir = os.path.join(base, "docs")
    os.makedirs(out_dir, exist_ok=True)

    items = []
    for path in sorted(glob(os.path.join(data_dir, "*.yaml"))):
        with open(path, "r", encoding="utf-8") as f:
            d = yaml.safe_load(f)
            items.append(d)

    out_path = os.path.join(out_dir, "data.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    print("Wrote", out_path)


if __name__ == "__main__":
    main()
