from  (
	select
		concat(ar.month, ar.year, ar.CustomerID, ar.PaymentType, sum(ar.Amount)) as UniqueID,
		ar.customerid,
		MAX(ar.DateUpdated) as DateUpdate
		from ar
		group by ar.Month, ar.Year, ar.CustomerID, ar.PaymentType, ar.recurrence
	) max_date 
inner join ar on max_date.UniqueID = ar.UniqueID and max_date.CustomerId = ar.CustomerId