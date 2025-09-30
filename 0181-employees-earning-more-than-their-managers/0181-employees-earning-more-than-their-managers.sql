# Write your MySQL query statement below
SELECT
    a.name AS Employee
FROM Employee a join Employee b on(a.managerId = b.id)
WHERE a.salary > b.salary