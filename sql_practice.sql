CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    city TEXT,
    salary INTEGER,
    department TEXT
); 

INSERT INTO employees VALUES (1, 'Bhavana', 'Bangalore', 35000, 'Analytics');
INSERT INTO employees VALUES (2, 'Priya', 'Mumbai', 50000, 'Engineering');
INSERT INTO employees VALUES (3, 'Raj', 'Chennai', 28000, 'Analytics');
INSERT INTO employees VALUES (4, 'Sneha', 'Delhi', 42000, 'Marketing');
INSERT INTO employees VALUES (5, 'Arjun', 'Hyderabad', 60000, 'Engineering');

SELECT * FROM employees;

SELECT name, salary FROM employees;

SELECT * FROM employees
WHERE department = 'Engineering';

SELECT * FROM employees
WHERE department = 'Engineering'
AND salary > 40000;

"""Show all employees sorted by salary lowest to highest
Show only name and salary sorted by salary highest to lowest
Show only Engineering department employees sorted by salary highest to lowest"""
SELECT * FROM employees
ORDER BY salary ASC;

SELECT name, salary FROM employees
ORDER BY salary DESC;

SELECT * FROM employees
where department = 'engineering'
ORDER BY salary DESC;


"""Show average salary per department
Show total salary per city (use SUM)
Show number of employees per department (use COUNT)"""
SELECT department, AVG(salary)
FROM employees
GROUP BY department;

SELECT city, SUM(salary)
FROM employees
GROUP BY city;

SELECT department, COUNT(id)
FROM employees
GROUP BY department;

"""What is the average salary per department, excluding the lowest paid employee, sorted highest to lowest?"""
SELECT department, AVG(salary)
FROM employees
WHERE salary > 28000
GROUP BY department
ORDER BY AVG(salary) DESC;

SELECT employees.name, employees.salary, departments.location
FROM employees
JOIN departments
ON employees.department = departments.dept_name;