WITH XMLNAMESPACES ('http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/StoreSurvey' as ss)
SELECT 
    StoreData.Name AS StoreName,
    StoreData.YearOpened,
    SUM(SOH.TotalDue) AS TotalRevenue
FROM (
    -- SUBQUERY: Extract the XML data first
    SELECT 
        BusinessEntityID, 
        Name, 
        Demographics.value('(ss:StoreSurvey/ss:YearOpened)[1]', 'int') AS YearOpened
    FROM Sales.Store
) AS StoreData -- We give this subquery a nickname
JOIN Sales.Customer AS C 
    ON StoreData.BusinessEntityID = C.StoreID
JOIN Sales.SalesOrderHeader AS SOH 
    ON C.CustomerID = SOH.CustomerID
GROUP BY StoreData.Name, StoreData.YearOpened
ORDER BY StoreData.YearOpened;