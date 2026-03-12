SELECT 
    cr.Name AS Country, 
    ROUND(SUM(soh.TotalDue), 2) AS TotalRevenue
FROM Sales.SalesOrderHeader soh
INNER JOIN Sales.SalesTerritory st 
ON soh.TerritoryID = st.TerritoryID
INNER JOIN Person.CountryRegion cr 
ON st.CountryRegionCode = cr.CountryRegionCode
GROUP BY cr.Name
ORDER BY TotalRevenue DESC;
