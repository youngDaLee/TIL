DELETE t1 FROM Person t1 
JOIN Person t2
ON t1.email=t2.email
WHERE t1.id > t2.id;