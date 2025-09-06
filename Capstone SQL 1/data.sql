CREATE TABLE Users(
Personnel INT PRIMARY KEY,
Name VARCHAR(100) NOT NULL,
Email VARCHAR(100) NOT NULL UNIQUE,
Department VARCHAR(50) NOT NULL,
Salary DECIMAL(10, 2) NOT NULL
);

INSERT INTO Users (Personnel, Name, Email, Department, Salary) VALUES
(1, 'Alice Johnson', 'alice.johnson@example.com', 'Engineering', 75000.00),
(2, 'Bob Smith', 'bob.smith@example.com', 'Marketing', 60000.00),
(3, 'Charlie Brown', 'charlie.brown@example.com', 'Sales', 55000.00),
(4, 'David Wilson', 'david.wilson@example.com', 'HR', 50000.00),
(5, 'Eva Green', 'eva.green@example.com', 'Finance', 80000.00),
(6, 'Frank White', 'frank.white@example.com', 'IT', 90000.00),
(7, 'Grace Black', 'grace.black@example.com', 'Marketing', 65000.00),
(8, 'Nelson Anderson', 'nelson.anderson@example.com', 'Sales', 55000.00),
(9, 'William Harris', 'william.harris@example.com', 'IT', 90000.00),
(10, 'Olivia Martin', 'olivia.martin@example.com', 'HR', 50000.00);

SELECT * FROM Users;    
SELECT Name, Email FROM Users WHERE Department = 'IT';
SELECT AVG(Salary) AS AverageSalary FROM Users WHERE Department = 'Marketing';
SELECT Department, COUNT(*) AS EmployeeCount FROM Users GROUP BY Department;
SELECT * FROM Users WHERE Salary > 60000 ORDER BY Salary DESC;
