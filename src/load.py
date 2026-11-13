import sqlite3
from pathlib import Path

from transform import read_json, build_table

PROCESSED_DIR = Path(__file__).parent.parent / "data" / "processed" #Directory to store processed data in ../data/processed

DB_PATH = PROCESSED_DIR / "rents.db" #Path to the database file

def create_table(link):
    """
    creates the db table for the rents, if it exists drops it and creates a new one
    """
    link.execute("DROP TABLE IF EXISTS rents")
    link.execute(
        """
        CREATE TABLE rents (
            geocod TEXT,
            name TEXT,
            year INTEGER,
            rent REAL,
            PRIMARY KEY (geocod, year)
        )
        """
    )

def insert_data(link, table):
    """
    inserts the data into the db table
    """
    link.executemany( #for each entry in table inserts the values into the corresponding columns in the rents table
        "INSERT INTO rents (geocod, name, year, rent) "
        "VALUES (:geocod, :name, :year, :rent)",
        table,
    )

if __name__ == "__main__":
    table = build_table(read_json("0014711")["Dados"]) #builds the table from the data

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True) #creates the directory if it doesn't exist

    link = sqlite3.connect(DB_PATH) #connects to the database

    create_table(link) #creates the table in the database

    insert_data(link, table) #inserts the data into the table

    link.commit() #commits the changes to the database

    link.close() #closes the connection to the database
