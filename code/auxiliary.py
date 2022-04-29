from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def get_generales(links_file, time_tag):
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options, executable_path=r"C:/Users/goyan/Documents/Software/chromedriver_win32/chromedriver.exe")

    lines = []
    with open(links_file) as f:
        lines = f.readlines()

    all_links = []

    for line in lines:

        driver.get(line.replace("\n",""))

        time.sleep(3)

        elems = driver.find_elements(By.XPATH, "//a[@href]")

        for elem in elems:
            all_links.append(elem.get_attribute("href"))

    with open(f"data/intermediate/{time_tag}_particulares.txt", "w") as f:
        for line in all_links:
            _ = f.write(line)
            _ = f.write('\n')

    driver.close()

def get_particulares(time_tag):
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options, executable_path=r"C:/Users/goyan/Documents/Software/chromedriver_win32/chromedriver.exe")

    lines = []
    with open(f"data/intermediate/{time_tag}_particulares.txt") as f:
        lines = f.readlines()

    all_info = []
    i = 0
    for line in lines:
        if "caluga_img" in line:
            i += 1
            sys.stdout.write(f"\rNuevo link procesado. Total: {i}")
            sys.stdout.flush()
            try:
                driver.get(line.replace("\n",""))

                time.sleep(3)

                element = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "precio-ficha"))
                )
                all_info.append(element.text)

                element_2 = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "info_ficha"))
                )
                all_info.append(element_2.text)
                all_info.append("-------------------------------------------------")

            except Exception:
                print("Nos pillaron po' compadre.")
                pass

    with open(f"data/raw_output/{time_tag}_scrapped_raw_data.txt", "w", encoding="utf-8") as f:
        for line in all_info:
            _ = f.write(line)
            _ = f.write('\n')

    driver.close()


