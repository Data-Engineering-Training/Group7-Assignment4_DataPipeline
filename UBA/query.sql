CREATE DATABASE IF NOT EXISTS UBA_database_database;
USE UBA_database;

CREATE TABLE IF NOT EXISTS customers (
    CustomerID INT PRIMARY KEY NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS accounts (
    AccountID INT PRIMARY KEY NOT NULL,
    CustomerID INT NOT NULL,
    AccountType ENUM('Checking', 'Savings') NOT NULL,
    Balance DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
);

CREATE TABLE IF NOT EXISTS transactions (
    TransactionID INT PRIMARY KEY NOT NULL,
    AccountID INT NOT NULL,
    TransactionType ENUM('Credit', 'Debit') NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    TransactionDate DATETIME NOT NULL,
    FOREIGN KEY (AccountID) REFERENCES accounts(AccountID)
);