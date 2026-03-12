SELECT 
    CR.Name AS Country,
    ST.Name AS Region,
    SUM(SOH.TotalDue) AS Revenue
FROM Sales.SalesOrderHeader AS SOH
JOIN Sales.SalesTerritory AS ST ON SOH.TerritoryID = ST.TerritoryID
JOIN Person.CountryRegion AS CR ON ST.CountryRegionCode = CR.CountryRegionCode
GROUP BY CR.Name, ST.Name
ORDER BY Revenue DESC;