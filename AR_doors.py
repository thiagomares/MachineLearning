import json
import pyodbc


with open("./data.json", 'r+') as file:
    data = json.load(file)
print(data, type(data))
print(data['username'])


conn = pyodbc.connect(driver="ODBC Driver 17 for SQL Server",
                      server=data['host'], database=data['database'], uid=data['username'], pwd=data["password"])
cursor = conn.cursor()
cursor.execute(
    """
delete from CENTRAL_AR_Doors_monthly
where month = month(GETDATE()) and year = year(GETDATE())

insert into CENTRAL_AR_Doors_monthly
select
	CONCAT(CustomerId, MONTH(Transaction_Date), year(Transaction_Date)) as UniqueID,
	CustomerId,
	MONTH(Transaction_Date) Month,
	year(Transaction_Date) Year,
	MAX(Transaction_Date) DateUpdate,
	MAX(DoorCount) DoorsInProduction,
	MAX(CommunityCount) CommunityInProduction,
	MAX(EnabledDoors) DoorsEnabled,
	MAX(EnabledCommunities) CommunityEnabled
from ONE_Door_Penetration
where month(Transaction_Date) = month(GETDATE()) and year(Transaction_Date) = year(GETDATE())
group by MONTH(Transaction_Date), CustomerID, YEAR(Transaction_Date)"""
)

cursor.commit()
conn.close()
