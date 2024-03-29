SELECT HOUR, COUNT(0) AS COUNT
FROM (
    SELECT CAST(DATE_FORMAT(DATETIME,'%H') AS SIGNED) AS HOUR
    FROM ANIMAL_OUTS
) R
WHERE HOUR BETWEEN 9 AND 20
GROUP BY HOUR
ORDER BY HOUR;


/*
알게된 점
%h : 12시간 단위(오후 6시 -> 6)
%H : 24시간 단위(오후 6시 -> 18)
*/