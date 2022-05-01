import datetime

lines = []
for j in range(18,94):
    for i in range(1,6):
        link = f"https://www.toctoc.com/resultados/mapa/compra/casa-departamento/metropolitana/?moneda=2&precioDesde=0&precioHasta=0&dormitoriosDesde=&dormitoriosHasta=&banosDesde=0&banosHasta=0&estado=0&disponibilidadEntrega=&numeroDeDiasTocToc=0&superficieDesdeUtil=0&superficieHastaUtil=0&superficieDesdeConstruida=0&superficieHastaConstruida=0&superficieDesdeTerraza=0&superficieHastaTerraza=0&superficieDesdeTerreno=0&superficieHastaTerreno=0&ordenarPor=0&pagina={i}&paginaInterna={i}&zoom=9&idZonaHomogenea=0&idPoligono={j}&publicador=0&temporalidad=0"
        lines.append(link)

ct = datetime.datetime.now()
time_tag = str(ct).replace(":","").replace(" ","-")[:17]

with open(f"data/seed/automated_seed_{time_tag}.txt", "w", encoding="utf-8") as f:
    for line in lines:
        _ = f.write(line)
        _ = f.write('\n')

# Es conveniente partir el archivo en muchos archivos. Recomiendo correr:
# split myLargeFile.txt -l 3
# 3 semillas por archivo y correr un proceso bash

## omitir
