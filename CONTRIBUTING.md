Contributing
============

Bitte folgende Punkte beachten, bevor ein Pull Request erstellt wird:

- YAML-Dateien im `data/`-Ordner gegen die Schemata in `schema/` validieren.
- Einfache Tests lokal ausführen:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/validate.py
```

- Beim Merge in den `main`-Branch wird automatisch die statische Seite gebaut und nach GitHub Pages deployed.

Danke für die Mitarbeit!
