# Write your MySQL query statement below
select
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM person p left join address a on (a.personId = p.personId)
