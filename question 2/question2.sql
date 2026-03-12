SELECT 
    E.BusinessEntityID,
    E.VacationHours,
    S.Bonus,
    S.SalesYTD -- Adding this helps explain the bonus later
FROM HumanResources.Employee AS E
JOIN Sales.SalesPerson AS S 
    ON E.BusinessEntityID = S.BusinessEntityID;