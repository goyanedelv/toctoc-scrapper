# Scrappeador de TOC-TOC.cl

_Work in progress_

- `data/seed`: semillas para empezar a scrapear (manual)
- `get_generales(...)`: scrapea los links de la semilla (~ 30 propiedades por semilla)
- `data/intermediate`: resultados de links de las ~30 propiedades por cada semilla
- `get_particulares(...)`: scrapea la información de las ~30 propiedades por semilla
- `data/raw_output`: información de las propiedades en txt

Para correr el programa:

```cmd
toctoc-scrapper> python code/_main.py archivo_semilla.txt
```

Asumiendo que `python` invoca a `python3`.
