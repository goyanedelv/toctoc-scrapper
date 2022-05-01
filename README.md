# Scrappeador de TOC-TOC.cl

### Carpetas relevantes
- `data/seed`: semillas para empezar a scrapear (manual). Ver `seed_creator.py` para construir semillas automáticas (no recomendados).
- `data/intermediate`: resultados de links de las 30 propiedades por cada link semilla.
- `data/raw_output`: información de las propiedades en `txt`.

### Funciones relevantes
- `get_generales(...)`: genera los links de propiedades particulares a partir de los link semilla.
- `get_particulares(...)`: scrapea la información de las 30 propiedades por cada link semilla.
- `get_full_site(...)`: scrapea todo el `html` del sitio (usar con precaución).
- `parse_raw_to_excel.py`: para transformar información scrapeada en `txt` de la carpeta `data/raw_output` a `xlsx` en la carpeta `data/db_output`.

### Parámetros
- `parametros.yaml`: archivo de configuración para establecer ubicación de `chromedriver` y nivel de tolerancia (cuántos errores aceptamos antes de abortar el scrapping de un archivo semilla).

### Dependencias
- `selenium`

### Archivos de ejemplo
- `seed_links_test.txt`. Archivo semilla.
- `batch_multi_comunas.sh` para correrlo en bash con múltiples semillas


### Para correr el programa principal:

```cmd
toctoc-scrapper> python code/_main.py archivo_semilla.txt
```

Asumiendo que `python` invoca a `python3`.

Si se quiere proseguir a partir de un archivo intermedio:

```cmd
toctoc-scrapper> python code/_main_parcial.py 2022-04-28-004834
```

Donde el último argumento es el timetag generado por `get_generales(...)`.
