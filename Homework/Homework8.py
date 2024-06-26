



CREATE DATABASE IF NOT EXISTS person.db;
USE person.db;

CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,,
    LastName VARCHAR(100) NOT NULL,,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
)


CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT
)

INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(101, 'HR'),
(102, 'IT'),
(103, 'Sales');

INSERT INTO Employees (FirstName, LastName, DepartmentID) VALUES
('John', 'Doe', 101),
('Jane', 'Smith', 101),
('Michael', 'Johnson', 102),
('Emily', 'Davis', 102),
('Robert', 'Wilson', 103),
('Sarah', 'Brown', 103);

SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID;

SELECT e.FirstName, e.LastName
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = 'IT';