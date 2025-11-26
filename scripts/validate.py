#!/usr/bin/env python3
"""Validate YAML files in data/ against JSON schemas in schema/"""
import json
import os
import sys
from glob import glob

import yaml
from jsonschema import validate, ValidationError, RefResolver


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_files():
    ok = True
    base = os.path.dirname(os.path.dirname(__file__))
    schema_dir = os.path.join(base, "schema")
    data_dir = os.path.join(base, "data")

    fach_schema = load_json(os.path.join(schema_dir, "fachverfahren.schema.json"))

    for path in glob(os.path.join(data_dir, "fachverfahren", "*.yaml")):
        try:
            doc = load_yaml(path)
            validate(instance=doc, schema=fach_schema)
            print("OK:", os.path.relpath(path, base))
        except ValidationError as e:
            ok = False
            print("ERROR:", os.path.relpath(path, base))
            print(e.message)
        except Exception as e:
            ok = False
            print("ERROR (parse):", os.path.relpath(path, base), str(e))

    # validate top-level lists
    for pair in [("kategorien.yaml", "kategorien.schema.json"), ("anbieter.yaml", "anbieter.schema.json")]:
        data_path = os.path.join(data_dir, pair[0])
        schema_path = os.path.join(schema_dir, pair[1])
        try:
            doc = load_yaml(data_path)
            sch = load_json(schema_path)
            validate(instance=doc, schema=sch)
            print("OK:", pair[0])
        except ValidationError as e:
            ok = False
            print("ERROR:", pair[0])
            print(e.message)
        except Exception as e:
            ok = False
            print("ERROR (parse):", pair[0], str(e))

    if not ok:
        print("Validation failed")
        sys.exit(2)
    print("All validations passed")


if __name__ == "__main__":
    validate_files()
