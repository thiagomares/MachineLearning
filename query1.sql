select
	concat(ar.UniqueID, cast(ar.Amount as int)) as UniqueID
	,ar.CustomerID
	,pmid.PayleasePropertyManagerId
	,ar.Month
	,ar.Year
	,sum(ar.Amount) Amount
	,ar.FeeAmount
	,sum(ar.TotalTransaction) TotalTransaction
	,ar.PaymentType
	,ar.recurrence
	,ar.DateUpdate
from ONE_AR_Summary ar
inner join ONE_Customer_PMID pmid on pmid.CustomerID = ar.CustomerID
group by ar.UniqueID
	,ar.CustomerID
	,pmid.PayleasePropertyManagerId
	,ar.Month
	,ar.Year
	, ar.Amount
	,ar.FeeAmount
	,ar.TotalTransaction
	,ar.PaymentType
	,ar.recurrence
	,ar.DateUpdate
