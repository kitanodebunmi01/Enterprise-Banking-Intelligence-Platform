import pandas as pd
import random
import numpy as np
import os


from datetime import datetime, timedelta
from faker import Faker

fake = Faker("en_NG")

random.seed(42)
np.random.seed(42)

# CONFIGURATION

NUMBER_OF_BRANCHES = 150


# OPENING DATE FUNCTION

def generate_opening_date():

    start_date = datetime(1995, 1, 1)

    end_date = datetime(2015, 12, 31)

    random_days = random.randint(
        0,
        (end_date - start_date).days
    )

    return start_date + timedelta(days=random_days)

# REFERENCE DATA

BRANCH_LOCATIONS = [

    ("Victoria Island", "Lagos", "South West"),
    ("Lekki", "Lagos", "South West"),
    ("Ikeja", "Lagos", "South West"),
    ("Yaba", "Lagos", "South West"),
    ("Surulere", "Lagos", "South West"),

    ("Ibadan", "Oyo", "South West"),
    ("Ogbomosho", "Oyo", "South West"),

    ("Wuse II", "Abuja", "North Central"),
    ("Maitama", "Abuja", "North Central"),
    ("Garki", "Abuja", "North Central"),

    ("Port Harcourt", "Rivers", "South South"),
    ("Obio-Akpor", "Rivers", "South South"),

    ("Enugu", "Enugu", "South East"),
    ("Nsukka", "Enugu", "South East"),

    ("Onitsha", "Anambra", "South East"),
    ("Awka", "Anambra", "South East"),

    ("Kaduna", "Kaduna", "North West"),
    ("Zaria", "Kaduna", "North West"),

    ("Kano", "Kano", "North West"),
    ("Bichi", "Kano", "North West")

]


# BRANCH IDS

branch_ids = np.arange(
    1,
    NUMBER_OF_BRANCHES + 1
)

# BRANCH CODES

branch_codes = []

for branch_id in branch_ids:

    branch_codes.append(
        f"BR{branch_id:04d}"
    )


# BRANCH GEOGRAPHY

branch_locations = []

while len(branch_locations) < NUMBER_OF_BRANCHES:

    branch_locations.extend(BRANCH_LOCATIONS)

branch_locations = branch_locations[:NUMBER_OF_BRANCHES]

random.shuffle(branch_locations)

branch_names = []
cities = []
branch_numbers = []
states = []
regions = []

branch_counter = {}

for city, state, region in branch_locations:

    if city not in branch_counter:
        branch_counter[city] = 1
    else:
        branch_counter[city] += 1

    branch_number = branch_counter[city]
    branch_numbers.append(branch_number)

    roman_numerals = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X"
    }

    suffix = roman_numerals.get(
        branch_number,
        str(branch_number)
    )

    branch_names.append(
        f"{city} Branch {suffix}"
    )

    states.append(state)
    cities.append(city)
    regions.append(region)


# OPENING DATES

opening_dates = []

for _ in range(NUMBER_OF_BRANCHES):

    opening_dates.append(
        generate_opening_date().date()
    )


# EMPLOYEE COUNT FUNCTION

def generate_employee_count(branch_number):

    if branch_number == 1:
        return random.randint(55, 70)

    elif branch_number == 2:
        return random.randint(45, 60)

    elif branch_number == 3:
        return random.randint(35, 50)

    else:
        return random.randint(25, 40)
    


# EMPLOYEE COUNT

employee_counts = []

for branch_number in branch_numbers:

    employee_counts.append(
        generate_employee_count(branch_number)
    )



# BRANCH MANAGERS

manager_ids = []
manager_names = []

for manager_number in range(1, NUMBER_OF_BRANCHES + 1):

    manager_ids.append(
        f"BM{manager_number:04d}"
    )

    manager_names.append(
        fake.name()
    )


# BRANCH STATUS


branch_status = ["Active"] * NUMBER_OF_BRANCHES



# CREATE THE DATAFRAME

branches = pd.DataFrame({

    "BranchID": branch_ids,
    "BranchCode": branch_codes,
    "BranchName": branch_names,
    "City": cities,
    "BranchNumber": branch_numbers,
    "State": states,
    "Region": regions,
    "OpeningDate": opening_dates,
    "EmployeeCount": employee_counts,
    "BranchManagerID": manager_ids,
    "BranchManagerName": manager_names,
    "BranchStatus": branch_status

})

# VALIDATION

print(branches.head())

print()

print(branches.tail())

print()

print(f"Total Branches : {len(branches):,}")

print()

print("Oldest Branch")

print(branches["OpeningDate"].min())

print()

print("Newest Branch")

print(branches["OpeningDate"].max())

print()

print("Employee Count Summary")

print(branches["EmployeeCount"].describe())

print()

print("Branch Status Distribution")

print(branches["BranchStatus"].value_counts())

print()

print("Duplicate Branch Codes")

print(
    branches["BranchCode"].duplicated().sum()
)

print()

print("Duplicate Branch Names")

print(
    branches["BranchName"].duplicated().sum()
)

# EXPORT DATASET

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
    "DimBranch.csv"
)

branches.to_csv(
    output_file,
    index=False
)

print()

print("DimBranch exported successfully.")




