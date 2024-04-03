-- Retrieve the total number of customers in the database.
    SELECT COUNT(*) AS total_customers
    FROM customers;

-- Top 10 customers with highest account balance
SELECT c.FirstName, c.LastName, SUM(a.Balance) AS Balance FROM customers c JOIN accounts a ON c.CustomerID = a.CustomerID
GROUP BY c.FirstName, c.LastName, Balance
ORDER BY Balance DESC
LIMIT 10


