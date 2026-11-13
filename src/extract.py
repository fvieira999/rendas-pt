from pathlib import Path

import requests

URL = "https://www.ine.pt/ine/json_indicador/pindica.jsp?op=2&varcd={code}&lang=PT&Dim1=T" #generalizes URL to accept any code
RAW_DIR = Path(__file__).parent.parent / "data" / "raw" #Directory to store raw data in ../data/raw

def extract_data(code):
    """
    extracts data from INE API and saves it in a json file in the raw data directory
    returns the path to the json file
    """
    reply = requests.get(URL.format(code=code), timeout=60)
    reply.raise_for_status() #raises an erros if the request fails

    RAW_DIR.mkdir(parents=True, exist_ok=True) #creates the directory if it doesn't exist

    destination = RAW_DIR / f"{code}.json" # builds the path for the json file

    destination.write_bytes(reply.content)

    return destination #returns the path for the json file

if __name__ == "__main__":
    path = extract_data("0014711")
