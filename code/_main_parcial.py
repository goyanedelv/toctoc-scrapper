# toctoc scrapper
import sys
from auxiliary import *
import yaml

with open("parametros.yaml", 'r') as stream:
    try:
        parameters = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

if __name__ == "__main__":

    print("Scrapeando links particulares...")
    get_particulares(sys.argv[1], parameters)
    print("\rLinks particulares scrapeados! Data guardada en data/raw_output")