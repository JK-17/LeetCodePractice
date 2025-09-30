# Write your MySQL query statement below
SELECT
    DISTINCT email AS Email
FROM Person a
WHERE email in (SELECT
                    email
                FROM Person b
                WHERE a.id <> b.id
)