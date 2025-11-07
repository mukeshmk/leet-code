SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee AS e
JOIN Department AS d
ON e.departmentId = d.id
WHERE e.salary = (
    SELECT MAX(s.salary)
    FROM Employee AS s
    WHERE s.departmentId = e.departmentId
)