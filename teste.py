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
delete from
    ONE_AR_Summary
where
    Month = month(getdate())
    and year = year(getdate());

with ach as (
    select
        concat(CustomerId, month(Date), YEAR(Date)) UniqueID,
        CustomerId,
        PaymentType,
        month(Date) as Month,
        YEAR(Date) as Year,
        case
            when FeeAmount = 0 then 'Recurring'
            when FeeAmount <> 0 then 'One-Time'
        end as recurrence,
        COALESCE(sum(Amount), 0) as Amount,
        COALESCE(sum(FeeAmount), 0) as feeAmount,
        count(TransactionID) as Transactions,
        max(CAST(DateUpdated as date)) as DateUpdated,
        count(distinct(OwnerName)) as TransactionDoors
    from
        KPI_ACHResponseHistory
    group by
        PaymentType,
        month(Date),
        YEAR(Date),
        CustomerId,
case
            when FeeAmount = 0 then 'Recurring'
            when FeeAmount <> 0 then 'One-Time'
        end
)
insert into
    ONE_AR_Summary
select
    CONCAT(UniqueID, PaymentType, LEFT(recurrence, 3)) as UniqueID,
    CustomerID,
    Month,
    Year,
    Amount,
    DateUpdated,
    FeeAmount,
    PaymentType,
    Transactions,
    recurrence,
    TransactionDoors
from
    ach
where
    Month = month(getdate())
    and year = year(getdate())"""
)

cursor.commit()
conn.close()
