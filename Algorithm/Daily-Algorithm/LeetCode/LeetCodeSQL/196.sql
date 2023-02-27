DELETE t1 FROM Person t1 
JOIN Person t2
ON t1.email=t2.email
WHERE t1.id > t2.id;


-- -> 이게 더 빠름;
delete from person
where id not in  (
select * from(
	select min(id)
    from person
    group by email) as t
);