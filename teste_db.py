import json
from sqlalchemy.engine import URL
from sqlalchemy.engine import create_engine
import pandas as pd


with open("query1.sql", "r+") as query:
    script = str(query.read())

with open("data.json", "r+") as data:
    data = json.load(data)

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
dataframe = pd.read_sql_query(query, engine)
print(dataframe)