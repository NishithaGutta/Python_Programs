''' Program to generate random name, email, phone data using Faker'''
from faker  import Faker
fake = Faker()
emp_name = fake.name()
email = fake.email()
phone = fake.phone_number()
print("Employee Name:", emp_name)
print("Email ID:", email)
print("Phone Number:", phone)

