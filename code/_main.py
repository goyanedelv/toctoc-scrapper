# toctoc scrapper
import datetime
import time
import sys
from auxiliary import *
import yaml

with open("parametros.yaml", 'r') as stream:
    try:
        parameters = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

if __name__ == "__main__":

    
    ct = datetime.datetime.now()
    time_tag = str(ct).replace(":","").replace(" ","-")[:17]

    print("Scrapeando links generales...")
    get_generales(f"data/seed/{sys.argv[1]}", time_tag, parameters)
    print("Links generales scrapeados! Descansando por 15 segundos...")

    time.sleep(15)

    print("Scrapeando links particulares...")
    get_particulares(time_tag, parameters)
    print("\rLinks particulares scrapeados! Data guardada en data/raw_output")