import csv
import mysql.connector

def ingest_customers(cursor):
    try:
        with open('data/generated_data/customers.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                cursor.execute(
                    "INSERT INTO customers (CustomerID, FirstName, LastName, Email, PhoneNumber) VALUES (%s, %s, %s, %s, %s)",
                    (row['CustomerID'], row['FirstName'], row['LastName'], row['Email'], row['PhoneNumber'])
                )
    except mysql.connector.Error as err:
        print(f"Error while ingesting customers: {err}")

def ingest_accounts(cursor):
    try:
        with open('data/generated_data/accounts.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                cursor.execute(
                    "INSERT INTO accounts (AccountID, CustomerID, AccountType, Balance) VALUES (%s, %s, %s, %s)",
                    (row['AccountID'], row['CustomerID'], row['AccountType'], row['Balance'])
                )
    except mysql.connector.Error as err:
        print(f"Error while ingesting accounts: {err}")

def ingest_transactions(cursor):
    try:
        with open('data/generated_data/transactions.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                cursor.execute(
                    "INSERT INTO transactions (TransactionID, AccountID, TransactionType, Amount, TransactionDate) VALUES (%s, %s, %s, %s, %s)",
                    (row['TransactionID'], row['AccountID'], row['TransactionType'], row['Amount'], row['TransactionDate'])
                )
    except mysql.connector.Error as err:
        print(f"Error while ingesting transactions: {err}")

if __name__ == "__main__":
    try:
        # Connect to MySQL
        cnx = mysql.connector.connect(user='root', password='your_root_password', host='localhost', database='bank_database')
        cursor = cnx.cursor()

        # Ingest data
        ingest_customers(cursor)
        ingest_accounts(cursor)
        ingest_transactions(cursor)

        # Commit changes and close connection
        cnx.commit()
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
