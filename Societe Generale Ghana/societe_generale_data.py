
from faker import Faker
from pydantic import BaseModel
import string
import csv

fake = Faker(["en_US"])
Faker.seed(123)

#A function to genr
class Order(BaseModel):
    name: str
    phone_number: str
    address: str
    email_address: str
    account_balance: float
    transaction_method: str

soge_data = [
    Order(name = fake.name(),
       phone_number = '0' + fake.random.choice(['2','5']) +  fake.numerify('########'),
        address = fake.address(),
        email_address = fake.name() + '@' + fake.random.choice(['gmail.com', 'yahoo.com']),
        account_balance = round(fake.random.uniform(50,10000000),2),
      transaction_method = fake.random.choice(['Mobile App', 'Website'])).model_dump()

for _ in range(10000)
]

with open('soge_data.csv', 'w', newline = '') as csvfile:
    top = soge_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames = top)
    writer.writeheader()
    writer.writerows(soge_data)
