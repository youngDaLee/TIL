SELECT sell_date, COUNT(distinct product) as num_sold, group_concat(distinct product order by product asc) as products
FROM Activities
GROUP BY sell_date;