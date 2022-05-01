import pandas as pd
import datetime
import os

ct = datetime.datetime.now()
time_tag = str(ct).replace(":","").replace(" ","-")[:17]

db = []

arr = os.listdir("data/raw_output/")
for i in arr:

    with open(f"data/raw_output/{i}", encoding="utf-8") as f:
        lines = f.readlines()
        
        price = None
        address = None
        surface = None

        for line in lines:
            if "UF " in line:
                price = line.replace("UF ","")
            
            if "Dirección:" in line:
                address = line.replace("Dirección: ","")

            if "Superficie útil desde: " in line:
                surface = line.replace("Superficie útil desde: ","").replace(" m²", "")

            if "-------------------------------------------------" in line:

                if ((price == None) | (address == None) | (surface == None)):
                    price = None
                    address = None
                    surface = None
                else:
                    db.append([price, address, surface])
                    price = None
                    address = None
                    surface = None

df = pd.DataFrame(db, columns = ['price', 'address', 'surface'])

df.to_excel(f"data/db_output/{time_tag}_clean_output.xlsx", index = False)