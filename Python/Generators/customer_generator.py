import pandas as pd
import numpy as np

from faker import Faker
from datetime import datetime, timedelta
import random
import os


# INITIALIZE

fake = Faker("en_NG")
fake.seed_instance(42)

random.seed(42)
np.random.seed(42)

NUMBER_OF_CUSTOMERS = 100000

# REFERENCE DATA

CUSTOMER_SEGMENTS = [
    "Retail",
    "SME",
    "HNWI",
    "UHNWI",
    "Corporate"
]

NIGERIAN_PHONE_PREFIXES = [
    "070",
    "080",
    "081",
    "090",
    "091"
]

# HELPER FUNCTIONS

def generate_date_of_birth():

    today = datetime.today()

    # Exactly 85 years ago
    earliest_date = datetime(today.year - 85, today.month, today.day)

    # Exactly 18 years ago
    latest_date = datetime(today.year - 18, today.month, today.day)

    random_days = random.randint(
        0,
        (latest_date - earliest_date).days
    )

    return earliest_date + timedelta(days=random_days)

# CUSTOMER ID GENERATION

customer_ids = np.arange(
    100000001,
    100000001 + NUMBER_OF_CUSTOMERS
)


# CUSTOMER NAME & GENDER GENERATION

first_names = []
last_names = []
genders = []

for _ in range(NUMBER_OF_CUSTOMERS):

    gender = random.choice(["Male", "Female"])

    if gender == "Male":
        profile = fake.simple_profile(sex="M")
    else:
        profile = fake.simple_profile(sex="F")

    name_parts = profile["name"].split()

    first_name = name_parts[0]
    last_name = name_parts[-1]

    first_names.append(first_name)
    last_names.append(last_name)
    genders.append(gender)

# DATE OF BIRTH GENERATION

dates_of_birth = []

for _ in range(NUMBER_OF_CUSTOMERS):

    dob = generate_date_of_birth()

    dates_of_birth.append(dob.date())

# AGE CALCULATION

ages = []

today = datetime.today()

for dob in dates_of_birth:

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    ages.append(age)

# PHONE NUMBER GENERATION

phone_numbers = []
used_phone_numbers = set()

while len(phone_numbers) < NUMBER_OF_CUSTOMERS:

    prefix = random.choice(NIGERIAN_PHONE_PREFIXES)
    remaining_digits = random.randint(10000000, 99999999)

    phone_number = prefix + str(remaining_digits)

    if phone_number not in used_phone_numbers:
        used_phone_numbers.add(phone_number)
        phone_numbers.append(phone_number)


# EMAIL GENERATION

emails = []

for customer_id, first_name, last_name in zip(
    customer_ids,
    first_names,
    last_names
):

    email = (
        f"{first_name.lower()}."
        f"{last_name.lower()}."
        f"{customer_id}@email.com"
    )

    emails.append(email)


# CREATE CUSTOMER DATAFRAME

customers = pd.DataFrame({

    "CustomerID": customer_ids,
    "FirstName": first_names,
    "LastName": last_names,
    "Gender": genders,
    "DateOfBirth": dates_of_birth,
    "Age": ages,
    "PhoneNumber": phone_numbers,
    "Email": emails

})

# DATA VALIDATION

print(f"Total Customers Generated : {len(customers):,}")

print(f"Duplicate Customer IDs : {customers['CustomerID'].duplicated().sum()}")

print(f"Minimum Age : {customers['Age'].min()}")

print(f"Maximum Age : {customers['Age'].max()}")

print(f"Duplicate Phone Numbers : {customers['PhoneNumber'].duplicated().sum()}")

print(f"Duplicate Emails : {customers['Email'].duplicated().sum()}")

# PREVIEW

print(customers.head())

print()

print(customers.tail())

print()

print(f"Total Customers : {len(customers):,}")

