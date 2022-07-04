SELECT c.name as Customers
FROM Customers as c
LEFT JOIN (
    SELECT COUNT(*) as cnt, customerId
    FROM Orders
    GROUP BY customerId
) as o ON o.customerId=c.id
WHERE IFNULL(o.cnt, 0)=0;