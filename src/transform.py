import json
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"


def read_json(code):
    """
    reads the json file relative to the code
    """

    path = RAW_DIR / f"{code}.json"

    text = path.read_text(encoding="utf-8") #reads file into text

    reply= json.loads(text) #parses text into a python object

    return reply[0] #the response is a list with one element so we return just that element

def filter_median_concelhos(records):
    """
    filters the records of a year to only include the median and concelhos
    returns a list of the filtered records
    """
    result = []
    for record in records:
        if len(record["geocod"]) == 7 and record["dim_3"] == "2": #check if it is a concelho and if it is the median
            result.append(record) #if it is a concelho and the median we add it to the result

    return result

def build_table(data):
    """
    builds a table from the data
    returns a list of lists with the table
    """
    table = []
    for year, records in data.items(): #iterate over the years and records
        median_concelhos = filter_median_concelhos(records) #filters the records to only include the median and concelhos

        for record in median_concelhos: #iterate over the filtered records and build a dictionary with the relevant information
            linha = {
                "geocod": record["geocod"],
                "name": record["geodsg"],
                "year": int(year),
                "rent": float(record["valor"]) if "valor" in record else None, #if the record has a value we convert it to a float, if not we set it to None
            }
            table.append(linha)

    return table

#main for testing purposes
if __name__ == "__main__":
    object = read_json("0014711")

    data = object["Dados"] #extracts the data from the object

    table = build_table(data) #builds the table from the data

    print(f"First record: {table[0]}")
    print(f"Total number of records: {len(table)}")

    no_value = [linha for linha in table if linha["rent"] is None] #filters the table to only include the lines with no value
    print(f"Number of records with no value: {len(no_value)}")