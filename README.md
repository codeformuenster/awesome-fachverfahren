Awesome Fachverfahren

Eine community-geführte "Awesome"-Liste für kommunale Fachverfahren, die in deutschen Kommunalverwaltungen verwendet werden.

Struktur

```
awesome-fachverfahren/
├── README.md                 # Dieses Dokument
├── CONTRIBUTING.md           # Beiträge-Richtlinien
├── LICENSE                   # MIT Lizenz
├── requirements.txt          # Python-Abhängigkeiten
├── data/
│   ├── fachverfahren/        # YAML-Dateien für jedes Fachverfahren
│   ├── kategorien.yaml       # Verfügbare Kategorien
│   ├── anbieter.yaml         # Liste der Anbieter
│   └── tags.yaml             # Tags
├── schema/
│   ├── fachverfahren.schema.json
│   ├── kategorien.schema.json
│   └── anbieter.schema.json
├── scripts/
│   ├── validate.py           # Validiere YAML gegen JSON-Schemata
│   ├── build_index.py        # Generiere docs/data.json
│   └── generate_site.py      # Generiere index.html
├── .github/
│   └── workflows/            # GitHub Actions Workflows
├── docs/
│   ├── index.html            # Statische Webseite
│   ├── data.json             # Generierte JSON-Daten (auto)
│   └── assets/
│       ├── style.css
│       └── search.js
└── .gitignore
```

Fachverfahren-Format

Jedes Fachverfahren wird als YAML-Datei in `data/fachverfahren/` gespeichert:

```yaml
id: meso
name: VOIS|MESO
provider: HSH Software
categories:
  - Meldewesen
  - Bürgerdienste
license: Proprietary          # z.B. Proprietary, MIT, AGPL-3.0, GPL-2.0
open_source: false
deployment:
  - on-premise
  - cloud
technical:
  language: C#
  database: MSSQL
interfaces:
  - XDM
  - OSCI
link: https://www.hsh.de/
description: >
  Kommunales Fachverfahren für das Meldewesen.
```

Quickstart

1. Abhängigkeiten installieren (optional, mit virtualenv):

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

2. YAML-Validierung:

```bash
python3 scripts/validate.py
```

3. Index und statische Seite bauen:

```bash
python3 scripts/build_index.py
python3 scripts/generate_site.py
```

4. Lokal testen (HTTP-Server):

```bash
python3 -m http.server 8000 --directory docs
# Dann öffnen: http://localhost:8000/
```

CI/CD

- **Pull Requests**: `validate-data.yml` prüft neue/geänderte YAML-Dateien gegen die JSON-Schemata.
- **Merge in main**: `build-site.yml` baut die statische Seite und deployed nach GitHub Pages.

Lizenz

MIT License - siehe `LICENSE`
