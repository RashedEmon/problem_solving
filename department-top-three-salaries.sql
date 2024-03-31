-- Write your PostgreSQL query statement below
SELECT 
    department as "Department", name as "Employee", salary as "Salary"
FROM(
    SELECT
    Employee.name as name, 
    salary, 
    Department.name as department,
    DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) as rn
    FROM Employee
    INNER JOIN
    Department
    ON Employee.departmentId = Department.id
) as main
WHERE rn in (1,2,3);
