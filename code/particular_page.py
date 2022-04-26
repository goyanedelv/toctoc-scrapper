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

lines = []
with open('data/particulares_2.txt') as f:
    lines = f.readlines()

all_info = []
for line in lines:
    if "caluga_img" in line:
        driver.get(line.replace("\n",""))

        time.sleep(4)

        try:
            element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "precio-ficha"))
            )
            all_info.append(element.text)

            element_2 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "info_ficha"))
            )
            all_info.append(element_2.text)
            all_info.append("----------------------------------------")

        except Exception:
            pass

with open('data/scrapped_raw_2.txt', 'w', encoding='utf-8') as f:
    for line in all_info:
        _ = f.write(line)
        _ = f.write('\n')

driver.close()

