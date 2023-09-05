from sqlalchemy.engine import URL
from sqlalchemy import create_engine, select, TryCast, MetaData
from abc import ABC, abstractmethod
import json
import pyodbc
import pandas as pd
import requests

class Geradora:
    def __init__(self):
        self._data = None
    
    def ReadJson(self):
        with open("./data.json", 'r+') as file:
            self._data = json.load(file)

def CreateEngine():
    data = Geradora.ReadJson()
    conn_url = URL.create(
            "mssql+pyodbc",
            username=data['username'],
            password=data["password"],
            host=data["host"],
            port=1433,
            database=data["database"],
            query={
                "driver": "ODBC Driver 18 for SQL Server",
                "TrustServerCertificate": "yes"
            }
        )
    engine = create_engine(conn_url)
    return engine        

dataframe = pd.read_sql_query("select * from ONE_Bank_Data", CreateEngine())
print(dataframe)