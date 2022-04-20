from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options, executable_path=r"C:/Users/goyan/Documents/Software/chromedriver_win32/chromedriver.exe")

driver.get("https://www.toctoc.com/propiedades/compranuevo/departamento/las-condes/moller-carlos-alvarado-6184/1119459?o=listado_caluga_info")
try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "precio-ficha"))
    )
    print(element.text)

    element_2 = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "info_ficha"))
    )
    print(element_2.text)

finally:
    driver.quit()


