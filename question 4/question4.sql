SELECT 
    P.PersonType,
    E.JobTitle,
    E.SickLeaveHours
FROM HumanResources.Employee AS E
JOIN Person.Person AS P 
    ON E.BusinessEntityID = P.BusinessEntityID;