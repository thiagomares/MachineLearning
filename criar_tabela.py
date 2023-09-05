import json
import pyodbc



with open("./data.json", 'r+') as file:
    data = json.load(file)
print(data, type(data))
print(data['username'])


conn = pyodbc.connect(driver="ODBC Driver 17 for SQL Server",server=data['host'],database=data['database'],uid="TMares",pwd="ThiagoP@55word")
cursor = conn.cursor()
cursor.execute(
    """
    create table CENTRAL_AR_Doors_monthly(
	UniqueID varchar(15),
	customerID int,
	month int,
	Year int,
	dateUpdated date,
	DoorsInProduction int,
	CommunityInProduction int,
	DoorsEnabled int,
	CommunityEnabled int
)
    """
)

cursor.commit()
conn.close()
