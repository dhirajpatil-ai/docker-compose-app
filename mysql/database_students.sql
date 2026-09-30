CREATE DATABASE IF NOT EXISTS students;

USE students;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL
);

INSERT INTO students (FirstName, LastName) VALUES
('John', 'Doe'),
('Jane', 'Smith'),
('Alice', 'Johnson'),
('Bob', 'Brown');
