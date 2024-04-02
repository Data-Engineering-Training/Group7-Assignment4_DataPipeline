import csv
from faker import Faker
from random import randint, uniform, choice
import random
import string
from datetime import datetime, timedelta

fake = Faker()

# List of possible email domains
email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']

def generate_random_numbers():
    random_numbers = ""
    for _ in range(3):
        random_numbers += str(random.randint(0, 9))  # Concatenate random numbers as strings
    return random_numbers

# Generate customer data
customers = []
for customer_id in range(1, 1001):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email_domain = random.choice(email_domains)
    random_numbers = generate_random_numbers()  # random numbers
    email = f"{first_name.lower()}.{last_name.lower()}.{random_numbers}@{email_domain}"
    phone_number = fake.phone_number()
    customer = {
        'CustomerID': customer_id,
        'FirstName': first_name,
        'LastName' : last_name,
        'Email' : email,
        'PhoneNumber' : phone_number
    }
    customers.append(customer)

with open('data/generated_data/customers.csv', 'w', newline='') as csvfile:
    fieldnames = ['CustomerID', 'FirstName', 'LastName', 'Email', 'PhoneNumber']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(customers)


# Generate Account Data
accounts = []
for account_id in range(1, 1500):
    customer_id = random.choice([x['CustomerID'] for x in customers])
    account_type = random.choice(['Checking', 'Savings'])
    account_balance =  round(uniform(10, 1000000), 2)
    account = {
        'AccountID': account_id,
        'CustomerID': customer_id,
        'AccountType': account_type,
        'Balance': account_balance
    }
    accounts.append(account)

with open('data/generated_data/accounts.csv', 'w', newline='') as csvfile:
    fieldnames = ['AccountID', 'CustomerID', 'AccountType', 'Balance']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(accounts)

# Generate Transaction Data
transactions = []
for transacation_id in range(100000, 200000):
    account_id = random.choice([x['AccountID'] for x in accounts])
    transaction_type = random.choice(['Credit', 'Debit'])
    amount = round(uniform(10, 1000000), 2)
    transaction_date = fake.date_between(start_date='-5y', end_date='today')
    transaction = {
        'TransactionID': transacation_id,
        'AccountID': account_id,
        'TransactionType': transaction_type,
        'Amount': amount,
        'TransactionDate': transaction_date
    }
    transactions.append(transaction)

random.shuffle(transactions) # Shuffles the list of transactions to ensure that the data is not ordered by date or any other factor

with open('data/generated_data/transactions.csv', 'w', newline='') as csvfile:
    fieldnames = ['TransactionID', 'AccountID', 'TransactionType', 'Amount', 'TransactionDate' ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(transactions)