from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options, executable_path=r"C:/Users/goyan/Documents/Software/chromedriver_win32/chromedriver.exe")

driver.get("https://www.toctoc.com/resultados/mapa/compra/casa-departamento/metropolitana/las-condes/?moneda=2&precioDesde=0&precioHasta=0&dormitoriosDesde=&dormitoriosHasta=&banosDesde=0&banosHasta=0&estado=0&disponibilidadEntrega=&numeroDeDiasTocToc=0&superficieDesdeUtil=0&superficieHastaUtil=0&superficieDesdeConstruida=0&superficieHastaConstruida=0&superficieDesdeTerraza=0&superficieHastaTerraza=0&superficieDesdeTerreno=0&superficieHastaTerreno=0&ordenarPor=0&pagina=1&paginaInterna=1&zoom=11.922750895403178&idZonaHomogenea=0&atributos=&texto=Las%20Condes,%20Santiago&viewport=-33.505593246599915,-70.71095301212753,-33.38863270589,-70.53709363375654&idPoligono=17&publicador=0&temporalidad=0")


all_links = []

time.sleep(7)

elems = driver.find_elements(By.XPATH, "//a[@href]")

for elem in elems:
    all_links.append(elem.get_attribute("href"))

driver.close()

