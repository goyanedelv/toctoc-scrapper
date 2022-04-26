from selenium import webdriver
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options, executable_path=r"C:/Users/goyan/Documents/Software/chromedriver_win32/chromedriver.exe")

lines = []
with open('data/links.txt') as f:
    lines = f.readlines()

all_links = []

for line in lines:

    driver.get(line.replace("\n",""))


    time.sleep(5)

    elems = driver.find_elements(By.XPATH, "//a[@href]")

    for elem in elems:
        all_links.append(elem.get_attribute("href"))

with open('data/particulares.txt', 'w') as f:
    for line in all_links:
        _ = f.write(line)
        _ = f.write('\n')

driver.close()

