import pandas as pd
import numpy as np

from faker import Faker
from datetime import datetime
import random
import os


# INITIALIZE

fake = Faker("en_NG")

random.seed(42)
np.random.seed(42)

NUMBER_OF_CUSTOMERS = 100000

# CUSTOMER ID GENERATION

customer_ids = [
    f"CUST{str(i).zfill(7)}"
    for i in range(1, NUMBER_OF_CUSTOMERS + 1)
]

# CREATE CUSTOMER DATAFRAME

customers = pd.DataFrame({

    "CustomerID": customer_ids,
    "FirstName": first_names,
    "LastName": last_names,
    "Gender": genders

})


# PREVIEW

print(customers.head())

print()

print(customers.tail())

print()

print(f"Total Customers : {len(customers):,}")

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