SELECT employee_id,
    CASE 
        WHEN MOD(employee_id,2)=0 THEN 0
        WHEN name LIKE 'M%' THEN 0
        ELSE salary
    END AS bonus
FROM Employees
ORDER BY employee_id;