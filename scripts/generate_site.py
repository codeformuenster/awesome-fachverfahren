#!/usr/bin/env python3
"""Simple site generator: ensures data.json exists and copies template index.html if present."""
import os
import shutil


def main():
    base = os.path.dirname(os.path.dirname(__file__))
    docs = os.path.join(base, "docs")
    template = os.path.join(docs, "index.html.template")
    index = os.path.join(docs, "index.html")
    if os.path.exists(template) and not os.path.exists(index):
        shutil.copyfile(template, index)
        print("Copied template to index.html")
    else:
        print("Index already present or template missing")


if __name__ == "__main__":
    main()
