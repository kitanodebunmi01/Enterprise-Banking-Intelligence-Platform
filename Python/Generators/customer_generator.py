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

NIGERIAN_LOCATIONS = {

    "Lagos": [
        "Ikeja",
        "Lekki",
        "Victoria Island",
        "Yaba",
        "Surulere"
    ],

    "Abuja": [
        "Maitama",
        "Wuse",
        "Garki",
        "Asokoro",
        "Gwarinpa"
    ],

    "Rivers": [
        "Port Harcourt",
        "Obio-Akpor",
        "Eleme",
        "Oyigbo"
    ],

    "Oyo": [
        "Ibadan",
        "Ogbomosho",
        "Oyo"
    ],

    "Kano": [
        "Kano",
        "Bichi",
        "Wudil"
    ],

    "Kaduna": [
        "Kaduna",
        "Zaria",
        "Kafanchan"
    ],

    "Enugu": [
        "Enugu",
        "Nsukka"
    ],

    "Anambra": [
        "Awka",
        "Onitsha",
        "Nnewi"
    ]
}

OCCUPATIONS = {

    "Retail": [
        "Teacher",
        "Nurse",
        "Civil Servant",
        "Engineer",
        "Sales Representative",
        "Student",
        "Artisan",
        "Trader"
    ],

    "SME": [
        "Business Owner",
        "Restaurant Owner",
        "Fashion Designer",
        "Pharmacist",
        "Supermarket Owner"
    ],

    "HNWI": [
        "Medical Doctor",
        "Lawyer",
        "Oil & Gas Executive",
        "IT Director",
        "Bank Executive"
    ],

    "UHNWI": [
        "CEO",
        "Investor",
        "Chairman",
        "Industrialist"
    ],

    "Corporate": [
        "Corporate Account"
    ]

}

INCOME_RANGES = {

    "Retail": (600000, 8000000),

    "SME": (8000000, 40000000),

    "HNWI": (40000000, 150000000),

    "UHNWI": (150000000, 1000000000),

    "Corporate": (500000000, 10000000000)

}


# LOAD DIMBRANCH

project_directory = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

branch_file = os.path.join(
    project_directory,
    "Data",
    "Dimensions",
    "DimBranch.csv"
)

branch_df = pd.read_csv(branch_file)

branch_ids = branch_df["BranchID"].tolist()

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

def generate_join_date(date_of_birth):

    try:
        eighteenth_birthday = datetime(
            date_of_birth.year + 18,
            date_of_birth.month,
            date_of_birth.day
        )

    except ValueError:

        # Handles customers born on 29 February
        eighteenth_birthday = datetime(
            date_of_birth.year + 18,
            2,
            28
        )

    project_start = datetime(2016, 1, 1)

    earliest_join = max(eighteenth_birthday, project_start)

    latest_join = datetime.today()

    random_days = random.randint(
        0,
        (latest_join - earliest_join).days
    )

    return earliest_join + timedelta(days=random_days)


# ASSIGN CUSTOMERS TO BRANCHES


# Calculate branch allocation weights
branch_weights = (
    branch_df["EmployeeCount"] /
    branch_df["EmployeeCount"].sum()
)

# Assign customers using weighted probabilities
customer_branch_ids = np.random.choice(

    branch_df["BranchID"],

    size=NUMBER_OF_CUSTOMERS,

    p=branch_weights

)

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


# CUSTOMER LOCATION

states = []
cities = []

for _ in range(NUMBER_OF_CUSTOMERS):

    state = random.choice(list(NIGERIAN_LOCATIONS.keys()))

    city = random.choice(
        NIGERIAN_LOCATIONS[state]
    )

    states.append(state)
    cities.append(city)


# CUSTOMER SEGMENT

segments = []

for _ in range(NUMBER_OF_CUSTOMERS):

    segment = random.choices(

        population=[
            "Retail",
            "SME",
            "HNWI",
            "UHNWI",
            "Corporate"
        ],

        weights=[
            88,
            7,
            3,
            1,
            1
        ],

        k=1

    )[0]

    segments.append(segment)


# OCCUPATION

occupations = []

for segment in segments:

    occupation = random.choice(
        OCCUPATIONS[segment]
    )

    occupations.append(occupation)


# ANNUAL INCOME

annual_incomes = []

for segment in segments:

    minimum_income, maximum_income = INCOME_RANGES[segment]

    income = random.randint(
        minimum_income,
        maximum_income
    )

    annual_incomes.append(income)


# DATE JOINED

join_dates = []

for dob in dates_of_birth:

    join_date = generate_join_date(dob)

    join_dates.append(join_date.date())


# CREATE CUSTOMER DATAFRAME

customers = pd.DataFrame({

    "CustomerID": customer_ids,
    "BranchID": customer_branch_ids,

    "FirstName": first_names,
    "LastName": last_names,
    "Gender": genders,

    "DateOfBirth": dates_of_birth,
    "Age": ages,

    "PhoneNumber": phone_numbers,
    "Email": emails,

    "State": states,
    "City": cities,

    "CustomerSegment": segments,
    "Occupation": occupations,
    "AnnualIncome": annual_incomes,

    "DateJoined": join_dates

})

# DATA VALIDATION

print(f"Total Customers Generated : {len(customers):,}")

print(f"Duplicate Customer IDs : {customers['CustomerID'].duplicated().sum()}")

print(f"Minimum Age : {customers['Age'].min()}")

print(f"Maximum Age : {customers['Age'].max()}")

print(f"Duplicate Phone Numbers : {customers['PhoneNumber'].duplicated().sum()}")

print(f"Duplicate Emails : {customers['Email'].duplicated().sum()}")

print()

print("States Generated:")

print(customers["State"].value_counts())

print()

print("Customer Segment Distribution")

print(customers["CustomerSegment"].value_counts())

print()

print("Average Annual Income by Customer Segment")

print(
    customers
    .groupby("CustomerSegment")["AnnualIncome"]
    .mean()
    .round(0)
)

print()

print("Earliest Join Date")

print(customers["DateJoined"].min())

print()

print("Latest Join Date")

print(customers["DateJoined"].max())

print()

print("Branch Distribution")

print(
    customers["BranchID"].value_counts().head()
)

print()

print("Unique Branches")

print(
    customers["BranchID"].nunique()
)

branch_distribution = (
    customers["BranchID"]
    .value_counts()
    .reset_index()
)

branch_distribution.columns = [
    "BranchID",
    "CustomerCount"
]

branch_distribution = branch_distribution.merge(

    branch_df[["BranchID", "EmployeeCount"]],

    on="BranchID"

)

print()

print("Top Branches by Employee Count")

print(

    branch_distribution

    .sort_values(
        "EmployeeCount",
        ascending=True
    )

    .head(10)

)



# EXPORT DIMCUSTOMER

project_directory = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

output_file = os.path.join(
    project_directory,
    "Data",
    "Dimensions",
    "DimCustomer.csv"
)

customers.to_csv(
    output_file,
    index=False
)

print()

print("DimCustomer exported successfully.")
print(output_file)


# PREVIEW

print(customers.head())

print()

print(customers.tail())

print()

print(f"Total Customers : {len(customers):,}")

