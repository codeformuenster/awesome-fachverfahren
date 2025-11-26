Awesome Fachverfahren

Eine community-geführte "Awesome"-Liste für kommunale Fachverfahren, die in deutschen Kommunalverwaltungen verwendet werden.

Repository-Struktur

```
awesome-fachverfahren/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
├── data/
├── schema/
├── scripts/
└── docs/
```

Quickstart

- Abhängigkeiten installieren:

```bash
python3 -m pip install -r requirements.txt
```

- YAML-Validierung lokal ausführen:

```bash
python3 scripts/validate.py
```

- Index und statische Seite bauen:

```bash
python3 scripts/build_index.py
python3 scripts/generate_site.py
```

CI

- Pull Requests: `validate-data.yml` prüft YAML gegen JSON-Schemata.
- Merge nach `main`: `build-site.yml` baut die statische Seite und deployed `docs/` via GitHub Pages.

Lizenz: MIT
