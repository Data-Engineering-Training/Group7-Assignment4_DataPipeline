import csv
import random
from faker import Faker

fake = Faker()

# Generate synthetic data for Customer table
customers = [{'Customer_ID': i + 1,
              'First_Name': fake.first_name(),
              'Last_Name': fake.last_name(),
              'Date_of_Birth': fake.date_of_birth(minimum_age=18, maximum_age=90),
              'Address': fake.address(),
              'Phone_Number': fake.phone_number(),
              'Email': fake.email(),
              'KYC_Details': fake.uuid4()} for i in range(100000)]

# Generate synthetic data for Employee table
employees = [{'Employee_ID': i + 1,
              'First_Name': fake.first_name(),
              'Last_Name': fake.last_name(),
              'Position': fake.job(),
              'Date_of_Hire': fake.date_time_between(start_date='-5y', end_date='now'),
              'Salary': fake.random_number(digits=5)} for i in range(100000)]

# Generate synthetic data for Branch table
branches = [{'Branch_ID': i + 1,
             'Branch_Name': fake.company(),
             'Location': fake.address(),
             'Phone_Number': fake.phone_number(),
             'Manager_ID': random.randint(1, 100000)} for i in range(100000)]

# Generate synthetic data for Account table
accounts = [{'Account_ID': i + 1,
             'Customer_ID': i + 1,
             'Account_Type': random.choice(['Savings', 'Checking']),
             'Balance': fake.random_number(digits=7),
             'Open_Date': fake.date_time_between(start_date='-2y', end_date='now'),
             'Status': random.choice(['Active', 'Closed'])} for i in range(100000)]

# Generate synthetic data for Transaction table
transactions = [{'Transaction_ID': i + 1,
                 'Account_ID': i + 1,
                 'Transaction_Type': random.choice(['Deposit', 'Withdrawal', 'Transfer']),
                 'Amount': fake.random_number(digits=5),
                 'Transaction_Date': fake.date_time_between(start_date='-1y', end_date='now'),
                 'Description': fake.text()} for i in range(100000)]

# Generate synthetic data for Loan table
loans = [{'Loan_ID': i + 1,
          'Customer_ID': i + 1,
          'Loan_Type': random.choice(['Mortgage', 'Personal', 'Auto']),
          'Amount': fake.random_number(digits=6),
          'Interest_Rate': random.uniform(0.05, 0.15),
          'Term': random.randint(12, 120),
          'Start_Date': fake.date_time_between(start_date='-1y', end_date='now'),
          'Status': random.choice(['Active', 'Paid Off'])} for i in range(100000)]

# Generate synthetic data for Payment table
payments = [{'Payment_ID': i + 1,
             'Loan_ID': i + 1,
             'Amount': fake.random_number(digits=4),
             'Payment_Date': fake.date_time_between(start_date='-1y', end_date='now')} for i in range(100000)]

# Write data to CSV files
def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

write_to_csv(customers, 'customers.csv')
write_to_csv(employees, 'employees.csv')
write_to_csv(branches, 'branches.csv')
write_to_csv(accounts, 'accounts.csv')
write_to_csv(transactions, 'transactions.csv')
write_to_csv(loans, 'loans.csv')
write_to_csv(payments, 'payments.csv')

print("Synthetic data generated and written to CSV files successfully.")
