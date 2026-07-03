import pandas as pd
import random

from datetime import timedelta

import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)


customer_df = pd.read_csv(
    os.path.join(
        project_root,
        "Data",
        "Dimensions",
        "DimCustomer.csv"
    )
)

account_df = pd.read_csv(
    os.path.join(
        project_root,
        "Data",
        "Dimensions",
        "DimAccount.csv"
    )
)

branch_df = pd.read_csv(
    os.path.join(
        project_root,
        "Data",
        "Dimensions",
        "DimBranch.csv"
    )
)

date_df = pd.read_csv(
    os.path.join(
        project_root,
        "Data",
        "Dimensions",
        "DimDate.csv"
    )
)

print("=" * 60)
print("DIMENSIONS LOADED SUCCESSFULLY")
print("=" * 60)

print(f"Customers : {len(customer_df):,}")
print(f"Accounts  : {len(account_df):,}")
print(f"Branches  : {len(branch_df):,}")
print(f"Dates     : {len(date_df):,}")


LOAN_STATUS = [

    "Active",

    "Closed"

]

INTEREST_RATE = {

    "Personal Loan": 0.24,

    "Auto Loan": 0.18,

    "Mortgage": 0.16,

    "SME Working Capital": 0.23,

    "Business Expansion": 0.21,

    "Premium Credit": 0.17,

    "Corporate Term Loan": 0.19,

    "Corporate Overdraft": 0.20

}

LOAN_TENURE = {

    "Personal Loan": (1, 12),

    "Auto Loan": (12, 48),

    "Mortgage": (12, 240),

    "SME Working Capital": (12, 36),

    "Business Expansion": (12, 48),

    "Premium Credit": (12, 48),

    "Corporate Term Loan": (12, 36),

    "Corporate Overdraft": (12, 24)

}

LOAN_AMOUNT = {

    "Personal Loan": (100_000, 5_000_000),

    "Auto Loan": (1_000_000, 15_000_000),

    "Mortgage": (15_000_000, 250_000_000),

    "SME Working Capital": (5_000_000, 50_000_000),

    "Business Expansion": (10_000_000, 150_000_000),

    "Premium Credit": (20_000_000, 500_000_000),

    "Corporate Term Loan": (100_000_000, 3_000_000_000),

    "Corporate Overdraft": (20_000_000, 1_000_000_000)

}

LOAN_PROBABILITY = {

    "Retail": 0.18,

    "SME": 0.45,

    "HNWI": 0.35,

    "UHNWI": 0.45,

    "Corporate": 0.75

}

MAX_CONCURRENT_LOANS = {

    "Retail": 1,

    "SME": 1,

    "HNWI": 1,

    "UHNWI": 1,

    "Corporate": 1

}

LOAN_PRODUCT_WEIGHTS = {

    "Retail": {

        "Personal Loan": 60,

        "Auto Loan": 25,

        "Mortgage": 15

    },

    "SME": {

        "SME Working Capital": 70,

        "Business Expansion": 30

    },

    "HNWI": {

        "Premium Credit": 50,
        "Auto Loan": 50

    },

    "UHNWI": {

        "Premium Credit": 50,
        "Auto Loan": 50

    },

    "Corporate": {

        "Corporate Overdraft": 65,

        "Corporate Term Loan": 35

    }

}

SALARIED_OCCUPATIONS = [

    "Civil Servant",

    "Banker",

    "Teacher",

    "Doctor",

    "Engineer",

    "Lawyer",

    "Accountant",

    "Nurse",

    "IT Professional",

    "Government Employee"

]

MINIMUM_RETAIL_LOAN_INCOME = 2_400_000
MINIMUM_SALARY_HISTORY_MONTHS = 6

def retail_customer_eligible(customer, account):

    """
    Determines whether a Retail customer
    qualifies for lending.
    """

    if customer["Occupation"] not in SALARIED_OCCUPATIONS:

        return False

    if customer["AnnualIncome"] < MINIMUM_RETAIL_LOAN_INCOME:

        return False

    if customer["Age"] < 21:

        return False

    if customer["Age"] > 65:

        return False

    if account["AccountStatus"] != "Active":

        return False

    if account["Currency"] != "NGN":

        return False

    if account["AccountType"] not in [

        "Savings",

        "Current"

    ]:

        return False

# --------------------------------------------------
# Phase 2
#
# After FactTransaction production completes,
# verify the customer has received salary credits
# for at least MINIMUM_SALARY_HISTORY_MONTHS.
# --------------------------------------------------

    return True

def has_salary_history(customer_id):

    """
    Placeholder.

    This function will later analyse
    FactTransaction and determine whether
    the customer has consistent salary credits.
    """

    return True

def choose_loan_product(segment):

    """
    Selects a loan product based on
    business weights.
    """

    products = list(
        LOAN_PRODUCT_WEIGHTS[segment].keys()
    )

    weights = list(
        LOAN_PRODUCT_WEIGHTS[segment].values()
    )

    return random.choices(

        products,

        weights=weights,

        k=1

    )[0]

def calculate_loan_amount(
    customer,
    loan_product
):
    """
    Calculates a realistic loan amount
    based on customer profile.
    """

    income = customer["AnnualIncome"]

    # RETAIL

    if loan_product == "Personal Loan":

        maximum = income * 0.75

    elif loan_product == "Auto Loan":

        maximum = income * 2.50

    elif loan_product == "Mortgage":

        maximum = income * 5

    # SME

    elif loan_product == "SME Working Capital":

        maximum = income * 1

    elif loan_product == "Business Expansion":

        maximum = income * 2

    # HNWI / UHNWI

    elif loan_product == "Premium Credit":

        maximum = income * 3


    # CORPORATE

    elif loan_product == "Corporate Term Loan":

        maximum = random.randint(
            100_000_000,
            3_000_000_000
        )

        return maximum

    elif loan_product == "Corporate Overdraft":

        maximum = random.randint(
            20_000_000,
            1_000_000_000
        )

        return maximum

    else:

        minimum, maximum = LOAN_AMOUNT[
            loan_product
        ]

        return random.randint(
            minimum,
            maximum
        )

    minimum, _ = LOAN_AMOUNT[loan_product]

    maximum = min(
        maximum,
        LOAN_AMOUNT[loan_product][1]
    )



    return random.randint(
        int(minimum),
        int(maximum)
    )


def get_eligible_loan_products(customer):

    """
    Returns only the loan products
    the customer qualifies for.
    """

    segment = customer["CustomerSegment"]

    income = customer["AnnualIncome"]

    eligible_products = []

    for product in LOAN_PRODUCT_WEIGHTS[segment]:

        minimum_amount = LOAN_AMOUNT[product][0]

        if product == "Personal Loan":

            maximum = income * 0.75

        elif product == "Auto Loan":

            maximum = income * 2.5

        elif product == "Mortgage":

            maximum = income * 5

        elif product == "SME Working Capital":

            maximum = income * 1

        elif product == "Business Expansion":

            maximum = income * 2

        elif product == "Premium Credit":

            maximum = income * 3

        else:
            # Corporate products always qualify
            eligible_products.append(product)
            continue

        if maximum >= minimum_amount:

            eligible_products.append(product)

    return eligible_products

def determine_customer_loans(customer):

    """
    Determines whether a customer
    receives loans and how many.
    """

    segment = customer["CustomerSegment"]

    eligible_products = get_eligible_loan_products(
        customer
    )

    if not eligible_products:

        return []

    probability = LOAN_PROBABILITY[segment]

    if random.random() > probability:

        return []

    maximum = MAX_CONCURRENT_LOANS[segment]

    loan_count = random.randint(

        1,

        maximum

    )

    loan_products = []

    weights = LOAN_PRODUCT_WEIGHTS[segment]

    available_products = []

    available_weights = []

    for product in eligible_products:

        available_products.append(product)

        available_weights.append(
            weights[product]
        )

    while (

        len(loan_products) < loan_count

        and

        available_products

    ):

        product = random.choices(

            available_products,

            weights=available_weights,

            k=1

        )[0]

        loan_products.append(product)

        index = available_products.index(product)

        available_products.pop(index)

        available_weights.pop(index)

    return loan_products

def customer_can_receive_loans(customer, account):

    """
    Determines whether the customer
    qualifies for lending.
    """

    if customer["CustomerSegment"] == "Retail":

        if not retail_customer_eligible(
            customer,
            account
        ):
            return False

        if not has_salary_history(
            customer["CustomerID"]
        ):
            return False
        
    # Account must be at least 6 months old

    account_opened = pd.to_datetime(
        account["DateOpened"]
    )

    today = pd.to_datetime(
        date_df["Date"].max()
    )

    account_age_days = (
        today - account_opened
    ).days

    if account_age_days < 180:

        return False

    return True


def select_servicing_account(

    customer_accounts,

    loan_product

):
    """
    Selects the most appropriate account
    for servicing the loan.
    """

    active_accounts = customer_accounts[

        customer_accounts["AccountStatus"] == "Active"

    ]

    if active_accounts.empty:

        return None
    
    # CORPORATE LOANS

    if loan_product in [

        "Corporate Term Loan",

        "Corporate Overdraft"

    ]:

        current = active_accounts[

            (active_accounts["AccountType"] == "Current") &

            (active_accounts["Currency"] == "NGN")

        ]

        if not current.empty:

            return current.iloc[0]
        
    # NGN CURRENT

    current = active_accounts[

        (active_accounts["AccountType"] == "Current") &

        (active_accounts["Currency"] == "NGN")

    ]

    if not current.empty:

        return current.iloc[0]
    
        # NGN SAVINGS

    savings = active_accounts[

        (active_accounts["AccountType"] == "Savings") &

        (active_accounts["Currency"] == "NGN")

    ]

    if not savings.empty:

        return savings.iloc[0]
    
    return active_accounts.iloc[0]


loans = []

loan_id = 1

def create_loan_record(

    customer,

    account,

    loan_product

):

    global loan_id

    interest_rate = INTEREST_RATE[loan_product]

    tenure = random.randint(

        LOAN_TENURE[loan_product][0],

        LOAN_TENURE[loan_product][1]

    )

    original_loan_amount = calculate_loan_amount(

        customer,

        loan_product

    )

    monthly_installment = round(

        original_loan_amount /

        tenure,

        2

    )


    account_opened = pd.to_datetime(

        account["DateOpened"]

    )

    today = pd.to_datetime(

        date_df["Date"].max()

    )

    # Earliest loan can only be booked
    # after the account has existed for 6 months.

    earliest_disbursement = account_opened + timedelta(
        days=180
    )

    days_available = max(

        0,

        (
            today - earliest_disbursement
        ).days

    )

    disbursement_date = earliest_disbursement + timedelta(

        days=random.randint(

            0,

            days_available

        )

    )

    maturity_date = disbursement_date + timedelta(

        days=30 * tenure

    )

    outstanding_principal = round(

        original_loan_amount *

        random.uniform(

            0.20,

            1.00

        ),

        2

    )

    if maturity_date < today:

        loan_status = "Closed"

        outstanding_principal = 0

    else:

        loan_status = "Active"

    date_key = int(

        disbursement_date.strftime(

            "%Y%m%d"

        )

    )
    
    loans.append({

        "LoanID": loan_id,

        "CustomerID": customer["CustomerID"],

        "AccountID": account["AccountID"],

        "BranchID": account["BranchID"],

        "DateKey": date_key,

        "LoanProduct": loan_product,

        "Currency": account["Currency"],

        "OriginalLoanAmount": original_loan_amount,

        "MonthlyInstallment": monthly_installment,

        "OutstandingPrincipal": outstanding_principal,

        "InterestRate": interest_rate,

        "TenureMonths": tenure,

        "DisbursementDate": disbursement_date,

        "MaturityDate": maturity_date,

        "LoanStatus": loan_status

    })

    loan_id += 1



production_customers = customer_df

print()

print("=" * 60)

print("GENERATING LOANS")

print("=" * 60)

for _, customer in production_customers.iterrows():

    if (_ + 1) % 5000 == 0:

        print(
            f"Processed {_ + 1:,} customers..."
        )

    customer_accounts = account_df[

        account_df["CustomerID"] ==

        customer["CustomerID"]

    ]

    eligible_accounts = customer_accounts[

        customer_accounts["AccountStatus"] == "Active"

    ]

    if eligible_accounts.empty:

        continue

    

    loan_products = determine_customer_loans(

        customer

    )

    if not loan_products:

        continue

    for loan_product in loan_products:

        account = select_servicing_account(

            customer_accounts,

            loan_product

        )

        if account is None:

            continue

        if not customer_can_receive_loans(

            customer,

            account

        ):

            continue

        create_loan_record(

            customer,

            account,

            loan_product

        )

loan_df = pd.DataFrame(

    loans

)

output_path = os.path.join(

    project_root,

    "Data",

    "Facts",

    "FactLoan.csv"

)

loan_df.to_csv(

    output_path,

    index=False

)

print()

print("=" * 60)

print("LOANS GENERATED")

print("=" * 60)

print(

    f"Loans Generated : {len(loan_df):,}"

)

print(

    f"Output : {output_path}"

)



