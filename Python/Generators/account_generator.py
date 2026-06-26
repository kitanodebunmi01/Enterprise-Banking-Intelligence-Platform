import os
import random

import numpy as np
import pandas as pd

from datetime import datetime

random.seed(42)
np.random.seed(42)



# GENERATE CURRENT BALANCE


def generate_current_balance(

    customer_segment,

    account_type,

    account_status,

    currency,

    account_age_days

):

    
    # CLOSED ACCOUNT
    

    if account_status == "Closed":

        return 0


    
    # ACCOUNT AGE BAND
    

    if account_age_days <= 30:

        account_age = "New"

    elif account_age_days <= 365:

        account_age = "Growing"

    elif account_age_days <= 1825:

        account_age = "Mature"

    else:

        account_age = "Established"


    
    # RETAIL
    

    if customer_segment == "Retail":

        if account_type == "Savings":

            if account_age == "New":

                balance = random.randint(0, 150000)

            elif account_age == "Growing":

                balance = random.randint(50000, 2000000)

            elif account_age == "Mature":

                balance = random.randint(150000, 5000000)

            else:

                balance = random.randint(500000, 10000000)

        elif account_type == "Current":

            if account_age == "New":

                balance = random.randint(10000, 300000)

            else:

                balance = random.randint(100000, 8000000)


    
    # SME
    

    elif customer_segment == "SME":

        if account_type == "Savings":

            balance = random.randint(
                200000,
                15000000
            )

        else:

            balance = random.randint(
                500000,
                50000000
            )


    
    # HNWI
    

    elif customer_segment == "HNWI":

        if account_type == "Savings":

            balance = random.randint(
                5000000,
                120000000
            )

        elif account_type == "Current":

            balance = random.randint(
                5000000,
                150000000
            )

        elif account_type == "Domiciliary":

            if currency == "USD":

                balance = random.randint(
                    5000,
                    400000
                )

            elif currency == "GBP":

                balance = random.randint(
                    2000,
                    150000
                )

            else:

                balance = random.randint(
                    2000,
                    180000
                )

        else:

            if currency == "NGN":

                balance = random.randint(
                    20000000,
                    250000000
                )

            else:      # USD Fixed Deposit

                balance = random.randint(
                    10000,
                    500000
                )


    
    # UHNWI
    

    elif customer_segment == "UHNWI":

        if account_type == "Savings":

            balance = random.randint(
                50000000,
                500000000
            )

        elif account_type == "Current":

            balance = random.randint(
                100000000,
                1000000000
            )

        elif account_type == "Domiciliary":

            if currency == "USD":

                balance = random.randint(
                    100000,
                    3000000
                )

            elif currency == "GBP":

                balance = random.randint(
                    50000,
                    1000000
                )

            else:

                balance = random.randint(
                    50000,
                    1200000
                )

        else:       # Fixed Deposit

            if currency == "NGN":

                balance = random.randint(
                    100000000,
                    3000000000
                )

            else:

                balance = random.randint(
                    50000,
                    3000000
                )


    
    # CORPORATE
    

    else:      # Corporate

        if account_type == "Current":

            balance = random.randint(
                20000000,
                5000000000
            )

        elif account_type == "Domiciliary":

            balance = random.randint(
                100000,
                10000000
            )

        else:       # Fixed Deposit

            if currency == "NGN":

                balance = random.randint(
                    100000000,
                    10000000000
                )

            else:

                balance = random.randint(
                    500000,
                    10000000
                )


    
    # DORMANT ACCOUNT
    

    if account_status == "Dormant":

        balance = int(

            balance *

            random.uniform(
                0.15,
                0.50
            )

        )


    return balance


# LOAD DIMCUSTOMER

project_directory = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

customer_file = os.path.join(
    project_directory,
    "Data",
    "Dimensions",
    "DimCustomer.csv"
)

customers = pd.read_csv(customer_file)


# ACCOUNT RECORDS

account_records = []

# ACCOUNT COUNTER

account_id = 1


# GENERATE UNIQUE ACCOUNT NUMBERS

account_numbers = random.sample(

    range(1000000000, 9999999999),

    300000

)

account_number_index = 0



# GENERATE ACCOUNTS


for _, customer in customers.iterrows():

    customer_segment = customer["CustomerSegment"]

    customer_join_date = pd.to_datetime(
    customer["DateJoined"]
    )

    
    # NUMBER OF ACCOUNTS
    

    if customer_segment == "Retail":

        number_of_accounts = random.randint(1, 2)

        account_types = [
            "Savings",
            "Current"
        ]

    elif customer_segment == "SME":

        number_of_accounts = random.randint(1, 2)

        account_types = [
            "Current",
            "Savings"
        ]

    elif customer_segment == "HNWI":

        number_of_accounts = random.randint(3, 4)

        account_types = [
            "Savings",
            "Current",
            "Domiciliary",
            "Fixed Deposit"
        ]

    elif customer_segment == "UHNWI":

        number_of_accounts = 4

        account_types = [
            "Savings",
            "Current",
            "Domiciliary",
            "Fixed Deposit"
        ]

    else:       # Corporate

        number_of_accounts = random.randint(3, 3)

        account_types = [
            "Current",
            "Domiciliary",
            "Fixed Deposit"
        ]

    
    
    
    # CUSTOMER ACCOUNT PORTFOLIO


    if customer_segment == "Retail":

        if number_of_accounts == 1:

            customer_account_types = [
                "Savings"
            ]

        else:

            customer_account_types = [
                "Savings",
                "Current"
            ]

    elif customer_segment == "SME":

        if number_of_accounts == 1:

            customer_account_types = [
                "Current"
            ]

        else:

            customer_account_types = [
                "Current",
                "Savings"
            ]

    elif customer_segment == "HNWI":

        if number_of_accounts == 3:

            customer_account_types = [
                "Savings",
                "Current",
                "Domiciliary"
            ]

        else:

            customer_account_types = [
                "Savings",
                "Current",
                "Domiciliary",
                "Fixed Deposit"
            ]

    elif customer_segment == "UHNWI":

        customer_account_types = [
            "Savings",
            "Current",
            "Domiciliary",
            "Fixed Deposit"
        ]

    else:   # Corporate

        customer_account_types = [
            "Current",
            "Domiciliary",
            "Fixed Deposit"
        ]

    
    # CREATE EACH ACCOUNT
    

    for account_type in customer_account_types:

    
    # ACCOUNT CURRENCY
    

        if account_type == "Savings":

            currency = "NGN"

        elif account_type == "Current":

            currency = "NGN"

        elif account_type == "Fixed Deposit":

            currency = random.choices(

                [

                    "NGN",

                    "USD",

                    "GBP",

                    "EUR"

                ],

                weights=[

                    88,

                    8,

                    2,

                    2

                ]

            )[0]

        else:

            currency = random.choices(
                ["USD", "GBP", "EUR"],
                weights=[85, 10, 5]
            )[0]


        
        # ACCOUNT STATUS
        

        account_status = random.choices(

            [
                "Active",
                "Dormant",
                "Closed"
            ],

            weights=[
                92,
                6,
                2
            ]

        )[0]

        
        # ACCOUNT OPENING DATE
        

        today = datetime.today()

        days_since_join = (
            today - customer_join_date
        ).days

        opening_offset = random.randint(
            0,
            max(days_since_join, 0)
        )

        date_opened = (
            customer_join_date +
            pd.Timedelta(days=opening_offset)
        ).date()

        # ACCOUNT AGE

        account_age_days = (

            today.date() -

            date_opened

        ).days

        # CURRENT BALANCE

        current_balance = generate_current_balance(

            customer_segment,

            account_type,

            account_status,

            currency,

            account_age_days

        )


        account_records.append({

            "AccountID": account_id,

            "AccountNumber": str(
                account_numbers[account_number_index]
            ),

            "CustomerID": customer["CustomerID"],

            "BranchID": customer["BranchID"],

            "AccountType": account_type,

            "Currency": currency,

            "AccountStatus": account_status,

            "DateOpened": date_opened,

            "CurrentBalance": current_balance

        })

        account_id += 1

        account_number_index += 1


# CREATE THE DATAFRAME

accounts = pd.DataFrame(account_records)


# VALIDATION

validation = accounts.merge(

    customers[
        [
            "CustomerID",
            "DateJoined"
        ]
    ],

    on="CustomerID"

)

validation["DateOpened"] = pd.to_datetime(
    validation["DateOpened"]
)

validation["DateJoined"] = pd.to_datetime(
    validation["DateJoined"]
)

print()

print("Accounts Opened Before Customer Joined")

print(
    (
        validation["DateOpened"] <
        validation["DateJoined"]
    ).sum()
)

print()

print("Total Accounts")

print(len(accounts))

print()

print(accounts.head())

print()

print(accounts.tail())

print()

print("Duplicate Account IDs")

print(
    accounts["AccountID"].duplicated().sum()
)

print()

print("Unique Customers")

print(
    accounts["CustomerID"].nunique()
)

accounts_per_customer = (
    accounts
    .groupby("CustomerID")
    .size()
)

print()

print("Accounts Per Customer")

print(
    accounts_per_customer.describe()
)

print()

print("Duplicate Account Numbers")

print(
    accounts["AccountNumber"].duplicated().sum()
)

print()

print("Account Number Length")

print(
    accounts["AccountNumber"]
    .str.len()
    .describe()
)

print()

print("Account Status Distribution")

print(

    accounts["AccountStatus"].value_counts()

)

print()

print(

    round(

        accounts["AccountStatus"]

        .value_counts(normalize=True) * 100,

        2

    )

)

print()

print("Earliest Account Opening Date")

print(
    accounts["DateOpened"].min()
)

print()

print("Latest Account Opening Date")

print(
    accounts["DateOpened"].max()
)

print()

print("Balance Summary")

print(

    accounts["CurrentBalance"]

    .describe()

)

print()

print("Top 10 Highest Balances")

print()

print("Account Type Distribution")

print(

    accounts["AccountType"]

    .value_counts()

)

print()

print("Currency Distribution")

print(

    accounts["Currency"]

    .value_counts()

)

print(

    accounts

    .sort_values(

        "CurrentBalance",

        ascending=False

    )[

        [

            "CustomerID",

            "AccountType",

            "Currency",

            "CurrentBalance"

        ]

    ].head(10)

)

print()

print("Closed Accounts With Non-Zero Balance")

print(

    accounts[

        (accounts["AccountStatus"] == "Closed")

        &

        (accounts["CurrentBalance"] > 0)

    ].shape[0]

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
    "DimAccount.csv"
)

accounts.to_csv(
    output_file,
    index=False
)

print()

print("DimAccount exported successfully.")