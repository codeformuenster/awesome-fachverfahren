#!/usr/bin/env python3
"""Simple link checker for HTTP(S) links referenced in docs/index.html"""
import sys
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


def main():
    try:
        with open("docs/index.html", "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
    except FileNotFoundError:
        print("docs/index.html not found; run build first")
        sys.exit(1)

    tags = soup.find_all(["a", "img", "link", "script"])
    urls = set()
    for t in tags:
        for attr in ("href", "src"):
            u = t.get(attr)
            if not u:
                continue
            if u.startswith("http://") or u.startswith("https://"):
                urls.add(u)

    bad = 0
    for u in sorted(urls):
        try:
            r = requests.head(u, allow_redirects=True, timeout=10)
            if r.status_code >= 400:
                print("BAD:", u, r.status_code)
                bad += 1
            else:
                print("OK:", u, r.status_code)
        except Exception as e:
            print("ERR:", u, str(e))
            bad += 1

    if bad:
        print(f"{bad} broken links")
        sys.exit(2)
    print("All external links OK")


if __name__ == "__main__":
    main()
