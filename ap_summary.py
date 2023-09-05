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
    DELETE FROM ONE_AP_Summary
WHERE month = MONTH(DATEADD(MONTH, -1, GETDATE())) and Year = YEAR(GETDATE())

insert into ONE_AP_Summary
select 
	CONCAT(ap.CustomerID, ap.Month, ap.Year)as UniqueID,
	ap.CustomerID,
	ap.Month,
	ap.Year,
	cast(MAX(ap.JobRundate) as date) as Jobrundate,
	coalesce(count(distinct(ap.DisplayName)),0) as Vendors,
	coalesce(sum(ap.CheckAmount), 0) as CheckAmount,
	COALESCE(SUM(ap.CheckCount), 0) as CheckPayments,
	coalesce(sum(ap.AvidPaymentAmount),0) as AvidAmount,
	coalesce(sum(ap.AvidPaymentCount), 0) as AvidCount,
	coalesce(sum(ap.DigitalPaymentAmount),0) as DigitalPaymentAmount,
	coalesce(sum(ap.DigitalPaymentCount), 0 ) as DigitalPaymentCount,
	coalesce(sum(ap.InvoiceAmount), 0) as InvoiceAmount,
	coalesce(sum(ap.InvoiceCount), 0) as InvoiceCount
from ONE_AP_Vendor ap
WHERE ap.Month = MONTH(DATEADD(MONTH, -1, GETDATE())) and ap.Year = YEAR(GETDATE())
group by ap.CustomerID, ap.Month, ap.Year
"""
)

cursor.commit()
conn.close()
