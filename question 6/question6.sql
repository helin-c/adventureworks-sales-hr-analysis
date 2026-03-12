WITH XMLNAMESPACES ('http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/StoreSurvey' as ss)
SELECT 
    StoreData.Name AS StoreName,
    StoreData.SquareFeet,
    StoreData.NumberEmployees,
    SUM(SOH.TotalDue) AS TotalRevenue
FROM (
    -- SUBQUERY: Extract SquareFeet and NumberEmployees from XML
    SELECT 
        BusinessEntityID, 
        Name, 
        Demographics.value('(ss:StoreSurvey/ss:SquareFeet)[1]', 'int') AS SquareFeet,
        Demographics.value('(ss:StoreSurvey/ss:NumberEmployees)[1]', 'int') AS NumberEmployees
    FROM Sales.Store
) AS StoreData 
JOIN Sales.Customer AS C 
    ON StoreData.BusinessEntityID = C.StoreID
JOIN Sales.SalesOrderHeader AS SOH 
    ON C.CustomerID = SOH.CustomerID
GROUP BY StoreData.Name, StoreData.SquareFeet, StoreData.NumberEmployees
ORDER BY TotalRevenue DESC;