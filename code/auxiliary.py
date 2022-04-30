from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
import time

def get_generales(links_file, time_tag, parameters):
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options = options, executable_path = parameters['chromedriver'])

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
            if "caluga_img" in line:

                _ = f.write(line)
                _ = f.write('\n')

    driver.close()

def get_particulares(time_tag, parameters):
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    tolerance = int(parameters['error_tolerance'])

    lines = []
    with open(f"data/intermediate/{time_tag}_particulares.txt") as f:
        lines = f.readlines()

    print(f"\nScrapeando archivo: {time_tag}")    

    driver = webdriver.Chrome(options = options, executable_path = parameters['chromedriver'])

    all_info = []
    i = 0
    error_counter = 0
    for line in lines:

        if error_counter > tolerance:
            print(f"\nErrores superaron umbral de tolerancia. Abortando misión.")
            break

        i += 1
        sys.stdout.write(f"\rNuevo link procesado. Total: {i}")
        sys.stdout.flush()
        try:
            driver.get(line.replace("\n",""))

            time.sleep(4)

            element = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'precio-b') or contains(@class, 'precio-ficha')]"))
            )
            all_info.append(element.text)
            element_2 = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'info_ficha')]"))
            )
            all_info.append(element_2.text)
            all_info.append("-------------------------------------------------")

        except TimeoutException as ex:
            print(f"\nNos habrán pillaron? - {ex}")
            error_counter += 1
            print(f"\nErrores acumulados: {error_counter}")

    driver.close()
    print(f"\n{i} propiedades scrapeadas.")

    with open(f"data/raw_output/{time_tag}_scrapped_raw_data.txt", "w", encoding="utf-8") as f:
        for line in all_info:
            _ = f.write(line)
            _ = f.write('\n')

def get_full_site(time_tag, parameters):
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    tolerance = int(parameters['error_tolerance'])

    lines = []
    with open(f"data/intermediate/{time_tag}_particulares.txt") as f:
        lines = f.readlines()

    driver = webdriver.Chrome(options = options, executable_path = parameters['chromedriver'])

    all_info = []
    i = 0
    error_counter = 0

    for line in lines:
        if error_counter > tolerance:
            print(f"\nErrores superaron umbral de tolerancia. Abortando misión.")
            break

        i += 1
        sys.stdout.write(f"\rNuevo link procesado. Total: {i}")
        sys.stdout.flush()
        try:
            driver.get(line.replace("\n",""))

            time.sleep(4)

            element = driver.page_source
            all_info.append(element)
            all_info.append("-------------------------------------------------")
            print('hop')

        except TimeoutException as ex:
            print(f"\nNos pillaron? - {ex}")
            error_counter += 1
            print(f"\nErrores acumulados: {error_counter}")

    driver.close()
    print(f"\n{i} propiedades scrapeadas.")

    with open(f"data/raw_output/full_source_{time_tag}_scrapped_raw_data.txt", "w", encoding="utf-8") as f:
        for line in all_info:
            _ = f.write(line)
            _ = f.write('\n')