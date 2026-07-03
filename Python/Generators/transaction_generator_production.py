# IMPORT LIBRARIES

import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd



# PROJECT SETTINGS


TRANSACTION_START_DATE = datetime(2016, 1, 1)

TRANSACTION_END_DATE = datetime.today()

# During development we'll use fewer accounts.
# Set to None when generating the final dataset.


MAX_DEVELOPMENT_ACCOUNTS = None

RANDOM_SEED = 42

# BANK CHARGES

TRANSFER_FEE = 50

VAT_RATE = 0.075

VAT_AMOUNT = round(
    TRANSFER_FEE * VAT_RATE,
    2
)

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)



# TRANSACTION RULES


TRANSACTION_RULES = {

    
    # RETAIL
    

    ("Retail", "Savings"): [

        "ATM_WD", "ATM_DEP",
        "CASH_WD", "CASH_DEP",
        "IB_IN", "IB_OUT",
        "NIP_IN", "NIP_OUT",
        "POS_PUR", "ONLINE_PUR",
        "AIRTIME", "DATA",
        "ELECTRICITY", "CABLETV",
        "SCHOOL_FEES", "INSURANCE"

    ],

    ("Retail", "Current"): [

        "ATM_WD", "ATM_DEP",
        "CASH_WD", "CASH_DEP",
        "IB_IN", "IB_OUT",
        "NIP_IN", "NIP_OUT",
        "POS_PUR", "ONLINE_PUR",
        "AIRTIME", "DATA",
        "ELECTRICITY", "CABLETV",
        "SCHOOL_FEES", "INSURANCE"

    ],


    
    # SME
    

    ("SME", "Current"): [

        "CASH_DEP",
        "CASH_WD",

        "IB_IN",
        "IB_OUT",

        "NIP_IN",
        "NIP_OUT",

        "POS_PUR",
        "ONLINE_PUR",

        "ELECTRICITY",
        "INSURANCE",

        "LOAN_DISB",
        "LOAN_REPAY"

    ],


    
    # HNWI


    ("HNWI", "Savings"): [

        "ATM_WD",
        "ATM_DEP",

        "CASH_WD",
        "CASH_DEP",

        "IB_IN",
        "IB_OUT",

        "NIP_IN",
        "NIP_OUT",

        "POS_PUR",
        "ONLINE_PUR",

        "FX_BUY",
        "FX_SELL",

        "FD_PLACE",
        "FD_MATURE",

        "LOAN_REPAY"

    ],

    ("HNWI", "Current"): [

        "IB_IN",
        "IB_OUT",

        "NIP_IN",
        "NIP_OUT",

        "FX_BUY",
        "FX_SELL",

        "SWIFT_IN",
        "SWIFT_OUT",

        "FD_PLACE",
        "FD_MATURE",

        "LOAN_REPAY"

    ],

    ("HNWI", "Domiciliary"): [

        "SWIFT_IN",
        "SWIFT_OUT",

        "FX_BUY",
        "FX_SELL"

    ],


    
    # UHNWI

    ("UHNWI", "Savings"): [

        "ATM_WD",
        "ATM_DEP",

        "CASH_WD",
        "CASH_DEP",

        "IB_IN",
        "IB_OUT",

        "NIP_IN",
        "NIP_OUT",

        "POS_PUR",
        "ONLINE_PUR",

        "FX_BUY",
        "FX_SELL",

        "FD_PLACE",
        "FD_MATURE",

        "LOAN_REPAY"

    ],

    ("UHNWI", "Current"): [

        "IB_IN",
        "IB_OUT",

        "SWIFT_IN",
        "SWIFT_OUT",

        "FX_BUY",
        "FX_SELL",

        "FD_PLACE",
        "FD_MATURE",

        "LOAN_REPAY"

    ],

    ("UHNWI", "Domiciliary"): [

        "SWIFT_IN",
        "SWIFT_OUT",

        "FX_BUY",
        "FX_SELL"

    ],


    
    # CORPORATE
    

    ("Corporate", "Current"): [

        "IB_IN",
        "IB_OUT",

        "NIP_IN",
        "NIP_OUT",

        "SWIFT_IN",
        "SWIFT_OUT",

        "FX_BUY",
        "FX_SELL",

        "LOAN_DISB",
        "LOAN_REPAY"

    ],

    ("Corporate", "Domiciliary"): [

        "SWIFT_IN",
        "SWIFT_OUT",

        "FX_BUY",
        "FX_SELL"

    ]

}

TRANSACTION_WEIGHTS = {

    
    # RETAIL
    

    "ATM_WD": 15,
    "ATM_DEP": 5,

    "CASH_WD": 8,
    "CASH_DEP": 8,

    "IB_IN": 12,
    "IB_OUT": 12,

    "NIP_IN": 18,
    "NIP_OUT": 18,

    "POS_PUR": 20,
    "ONLINE_PUR": 12,

    "AIRTIME": 10,
    "DATA": 10,

    "ELECTRICITY": 6,
    "CABLETV": 4,

    "SCHOOL_FEES": 2,
    "INSURANCE": 2,



    # SME

    "LOAN_DISB": 1,
    "LOAN_REPAY": 4,


    # HNWI / CORPORATE


    "FX_BUY": 5,
    "FX_SELL": 5,

    "SWIFT_IN": 4,
    "SWIFT_OUT": 4,

    "FD_PLACE": 1,
    "FD_MATURE": 1

}

SEGMENT_MULTIPLIERS = {

    "Retail":1,

    "SME":5,

    "HNWI":15,

    "UHNWI":40,

    "Corporate":80

}

# BASE TRANSACTION AMOUNTS
# (Retail values)

BASE_TRANSACTION_AMOUNTS = {

    "POS_PUR": (1_000, 50_000),

    "ONLINE_PUR": (2_000, 100_000),

    "ATM_WD": (5_000, 100_000),

    "ATM_DEP": (5_000, 100_000),

    "CASH_WD": (10_000, 300_000),

    "CASH_DEP": (10_000, 300_000),

    "IB_IN": (5_000, 500_000),

    "IB_OUT": (5_000, 500_000),

    "NIP_IN": (5_000, 500_000),

    "NIP_OUT": (5_000, 500_000),

    "LOAN_DISB": (500_000, 20_000_000),

    "LOAN_REPAY": (20_000, 2_000_000),

    "FX_BUY": (1_000, 50_000),

    "FX_SELL": (1_000, 50_000),

    "SWIFT_IN": (5_000, 250_000),

    "SWIFT_OUT": (5_000, 250_000),

    "FD_PLACE": (100_000, 10_000_000),

    "FD_MATURE": (100_000, 10_000_000)

}

MONTHLY_TRANSACTION_VOLUME = {

    "Retail": (12, 30),

    "SME": (30, 80),

    "HNWI": (20, 60),

    "UHNWI": (30, 100),

    "Corporate": (80, 250)

}


EVENT_PROBABILITIES = {

    "LOAN_DISB": 0.005,

    "FD_PLACE": 0.01,

    "FD_MATURE": 0.01

}

# PROJECT ROOT

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)


# LOAD DIMENSIONS


customer_df = pd.read_csv(
    os.path.join(
        project_root,
        "Data",
        "Dimensions",
        "DimCustomer.csv"
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

account_df = pd.read_csv(
    os.path.join(
        project_root,
        "Data",
        "Dimensions",
        "DimAccount.csv"
    )
)

transaction_type_df = pd.read_csv(
    os.path.join(
        project_root,
        "Data",
        "Dimensions",
        "DimTransactionType.csv"
    )
)


# VALIDATION

print("=" * 60)
print("DIMENSIONS LOADED SUCCESSFULLY")
print("=" * 60)

print(f"Customers          : {len(customer_df):,}")
print(f"Branches           : {len(branch_df):,}")
print(f"Accounts           : {len(account_df):,}")
print(f"Transaction Types  : {len(transaction_type_df):,}")


# INITIALIZE TRANSACTION STORAGE

batch_transactions = []

failed_transactions = 0

transaction_id = 1

# HELPER FUNCTIONS

def assign_behaviour_profile(customer):

    """
    Assigns a behaviour profile based on
    customer and account characteristics.
    """

    return "Healthy"

def generate_transaction_amount(account, customer, transaction):

    """
    Generates a realistic amount based on
    the selected transaction type.
    """

    transaction_code = transaction["TransactionCode"]

    annual_income = customer["AnnualIncome"]

    monthly_income = annual_income / 12


    
    # SALARY CREDIT
    

    if transaction_code == "SALARY_CR":

        return int(
            monthly_income *
            random.uniform(0.95, 1.05)
        )


    
    # POS PURCHASE
    

    elif transaction_code == "POS_PUR":

        return get_scaled_amount(
            customer,
            transaction_code
        )


    
    # ONLINE PURCHASE
    

    elif transaction_code == "ONLINE_PUR":

        return get_scaled_amount(
            customer,
            transaction_code
        )
    

    # LOAN

    elif transaction_code in [

        "LOAN_DISB",
        "LOAN_REPAY"

    ]:

        return get_scaled_amount(

            customer,

            transaction_code

        )
    

    # FX

    elif transaction_code in [

        "FX_BUY",
        "FX_SELL"

    ]:

        return get_scaled_amount(

            customer,

            transaction_code

        )
    

    # SWIFT

    elif transaction_code in [

        "SWIFT_IN",
        "SWIFT_OUT"

    ]:

        return get_scaled_amount(

            customer,

            transaction_code

        )
    

    # FIXED DEPOSITS

    elif transaction_code in [

        "FD_PLACE",
        "FD_MATURE"

    ]:

        return get_scaled_amount(

            customer,

            transaction_code

        )


    
    # ATM WITHDRAWAL
    

    elif transaction_code == "ATM_WD":

        return get_scaled_amount(
            customer,
            transaction_code
        )


    
    # TRANSFERS
    

    elif transaction_code in [

        "IB_OUT",
        "NIP_OUT"

    ]:

      
        return get_scaled_amount(
            customer,
            transaction_code
        )


    
    # CASH DEPOSIT
    

    elif transaction_code == "CASH_DEP":

        return get_scaled_amount(
            customer,
            transaction_code
        )


    
    # BILL PAYMENTS
    

    elif transaction_code in [

        "ELECTRICITY",
        "CABLETV",
        "DATA",
        "AIRTIME"

    ]:

        return random.randint(500, 50_000)


    
    # ACCOUNT CHARGES
    

    elif transaction_code in [

        "SMS_FEE",
        "STAMP_DUTY",
        "ACCT_MAINT",
        "TRANSFER_FEE",
        "VAT_CHARGE"

    ]:

        return random.randint(10, 2_000)


    
    # INTEREST
    

    elif transaction_code in [

        "SAV_INT",
        "CURR_INT"

    ]:

        return random.randint(100, 20_000)


    
    # DEFAULT
    

    else:

        return random.randint(1_000, 100_000)


def generate_monthly_income(account, customer):
    """
    Generates the customer's regular monthly income.
    Returns 0 if the customer has no fixed monthly income.
    """

    occupation = customer["Occupation"]
    annual_income = customer["AnnualIncome"]

    salaried_occupations = [
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

    if occupation in salaried_occupations:

        monthly_salary = annual_income / 12

        return int(
            monthly_salary *
            random.uniform(0.95, 1.05)
        )

    return 0

def get_scaled_amount(customer, transaction_code):

    multiplier = SEGMENT_MULTIPLIERS[
        customer["CustomerSegment"]
    ]

    minimum, maximum = BASE_TRANSACTION_AMOUNTS[
        transaction_code
    ]

    return random.randint(

        int(minimum * multiplier),

        int(maximum * multiplier)

    )


def get_monthly_transaction_count(customer):
    """
    Returns the monthly transaction volume
    based on the customer's segment.
    """

    minimum, maximum = MONTHLY_TRANSACTION_VOLUME[
        customer["CustomerSegment"]
    ]

    return random.randint(
        minimum,
        maximum
    )


def generate_transaction_date(current_month):
    """
    Generates a random transaction date
    within the current month.
    """

    month_start = current_month.replace(day=1)

    month_end = (
        month_start
        + pd.offsets.MonthEnd(0)
    ).to_pydatetime()

    return month_start + timedelta(

        days=random.randint(

            0,

            (month_end - month_start).days

        )

    )


def should_generate_event(transaction_code):
    """
    Determines whether a rare banking event
    should occur.
    """

    probability = EVENT_PROBABILITIES.get(
        transaction_code,
        1
    )

    return random.random() < probability


def get_transaction_definition(transaction_code):
    """
    Returns the transaction definition from
    DimTransactionType.
    """

    transaction = transaction_type_df[
        transaction_type_df["TransactionCode"] == transaction_code
    ]

    if transaction.empty:

        raise ValueError(
            f"Transaction Code '{transaction_code}' not found."
        )

    return transaction.iloc[0]


def add_system_transaction(
    transaction_code,
    amount,
    account,
    customer,
    current_month,
    transaction_date,
    running_balance
):
    """
    Creates a system-generated transaction
    (fees, VAT, interest, etc.)
    """

    global transaction_id

    transaction = get_transaction_definition(
        transaction_code
    )

    balance_before = running_balance

    if transaction["Direction"] == "Credit":

        balance_after = balance_before + amount

    else:

        balance_after = balance_before - amount

    date_key = int(
        transaction_date.strftime("%Y%m%d")
    )

    batch_transactions.append({

        "TransactionID": transaction_id,

        "AccountID": account["AccountID"],

        "CustomerID": customer["CustomerID"],

        "BranchID": account["BranchID"],

        "TransactionDate": transaction_date,

        "DateKey": date_key,

        "TransactionTypeID": transaction["TransactionTypeID"],

        "TransactionType": transaction["TransactionType"],

        "Direction": transaction["Direction"],

        "Channel": transaction["Channel"],

        "Amount": amount,

        "BalanceBefore": balance_before,

        "BalanceAfter": balance_after

    })

    transaction_id += 1

    return round(balance_after, 2)


def generate_month_end_postings(

    account,

    customer,

    current_month,

    transaction_date,

    running_balance,

    monthly_debit_total

):
    """
    Generates all month-end system postings.
    """

    
    # SAVINGS INTEREST
    

    if account["AccountType"] == "Savings":

        interest_amount = round(
            running_balance * 0.0005,
            2
        )

        if interest_amount > 0:

            running_balance = add_system_transaction(

                transaction_code="SAV_INT",

                amount=interest_amount,

                account=account,

                customer=customer,

                current_month=current_month,

                transaction_date=transaction_date,

                running_balance=running_balance

            )


        

    # ACCOUNT MAINTENANCE

    if (

            account["Currency"] == "NGN"

            and

            account["AccountType"] == "Current"

            and

            customer["CustomerSegment"] in [

                "Retail",

                "SME",

                "Corporate",

                "HNWI",

                "UHNWI"

            ]

        ):

            maintenance_fee = round(

                monthly_debit_total * 0.001,

                2

            )

            if maintenance_fee > 0:

                running_balance = add_system_transaction(

                    transaction_code="ACCT_MAINT",

                    amount=maintenance_fee,

                    account=account,

                    customer=customer,

                    current_month=current_month,

                    transaction_date=transaction_date,

                    running_balance=running_balance

                )


    
    # SMS ALERT FEE
    

    if account["Currency"] == "NGN":

        running_balance = add_system_transaction(

            transaction_code="SMS_FEE",

            amount=4,

            account=account,

            customer=customer,

            current_month=current_month,

            transaction_date=transaction_date,

            running_balance=running_balance

        )

    return running_balance



def choose_transaction_type(account, customer):
    """
    Selects a transaction type using
    weighted probabilities.
    """

    key = (

        customer["CustomerSegment"],

        account["AccountType"]

    )

    if key not in TRANSACTION_RULES:

        raise ValueError(

            f"No transaction rules found for {key}"

        )

    allowed_codes = TRANSACTION_RULES[key]

    weights = [

        TRANSACTION_WEIGHTS.get(

            code,

            1

        )

        for code in allowed_codes

    ]

    selected_code = random.choices(

        population=allowed_codes,

        weights=weights,

        k=1

    )[0]

    transaction = transaction_type_df[

        transaction_type_df["TransactionCode"] == selected_code

    ].iloc[0]

    return transaction


def generate_monthly_transactions(account, customer):

    """
    Generates one month's transactions
    for a single account.
    """

    global failed_transactions
    global transaction_id


    account_open_date = pd.to_datetime(account["DateOpened"])

    current_month = max(
        TRANSACTION_START_DATE,
        account_open_date.to_pydatetime()
    )

    running_balance = account["CurrentBalance"]

    while current_month <= TRANSACTION_END_DATE:


        # Stop after account closure
        if (
            account["AccountStatus"] == "Closed"
            and
            pd.notna(account["DateClosed"])
        ):

            date_closed = pd.to_datetime(account["DateClosed"])

            if current_month > date_closed.to_pydatetime():

                break

        # Number of transactions for the month
        monthly_transaction_count = get_monthly_transaction_count(
            customer
        )

    

        monthly_debit_total = 0

        #print(f"Transactions This Month : {monthly_transaction_count}")

        
        # MONTHLY INCOME
        

        salary_amount = generate_monthly_income(
            account,
            customer
        )

        if salary_amount > 0:

            balance_before = running_balance

            salary_date = generate_transaction_date(
                current_month
            )

            salary_date_key = int(
                salary_date.strftime("%Y%m%d")
            )

            balance_after = balance_before + salary_amount

            running_balance = round(balance_after, 2)

            salary_transaction = get_transaction_definition(
                "SALARY_CR"
            )

            batch_transactions.append({

                "TransactionID": transaction_id,

                "AccountID": account["AccountID"],

                "CustomerID": customer["CustomerID"],

                "BranchID": account["BranchID"],

                "TransactionDate": salary_date,

                "DateKey": salary_date_key,

                "TransactionTypeID": salary_transaction["TransactionTypeID"],

                "TransactionType": salary_transaction["TransactionType"],

                "Direction": salary_transaction["Direction"],

                "Channel": salary_transaction["Channel"],

                "Amount": salary_amount,

                "BalanceBefore": balance_before,

                "BalanceAfter": balance_after

            })

            transaction_id += 1


        for _ in range(monthly_transaction_count):

            balance_before = running_balance

            transaction_date = generate_transaction_date(
                current_month
            )

            date_key = int(
                transaction_date.strftime("%Y%m%d")
            )

            transaction = choose_transaction_type(
                account,
                customer
            )

            # Skip rare banking events most months

            if transaction["TransactionCode"] in [

                "LOAN_DISB",

                "FD_PLACE",

                "FD_MATURE"

            ]:

                if not should_generate_event(

                    transaction["TransactionCode"]

                ):

                    continue

            amount = generate_transaction_amount(
                account,
                customer,
                transaction
            )

            '''
            print(
                transaction["TransactionCode"],
                amount
            )
            '''

            direction = transaction["Direction"]

            # CREDIT TRANSACTION

            if direction == "Credit":

                balance_after = balance_before + amount

                running_balance = round(balance_after, 2)


            # DEBIT TRANSACTION

            else:

                # Insufficient funds

                if amount > balance_before:

                    failed_transactions += 1

                    continue

                balance_after = balance_before - amount

                running_balance = round(balance_after, 2)

                # Track debits for monthly account maintenance

                if (

                    account["Currency"] == "NGN"

                    and

                    account["AccountType"] == "Current"

                    and

                    customer["CustomerSegment"] in [

                        "Retail",

                        "SME",

                        "Corporate",

                        "HNWI",

                        "UHNWI"

                    ]

                ):

                    monthly_debit_total += amount

            batch_transactions.append({

                "TransactionID": transaction_id,

                "AccountID": account["AccountID"],

                "CustomerID": customer["CustomerID"],

                "BranchID": account["BranchID"],

                "TransactionDate": transaction_date,

                "DateKey": date_key,

                "TransactionTypeID": transaction["TransactionTypeID"],

                "TransactionType": transaction["TransactionType"],

                "Direction": direction,

                "Channel": transaction["Channel"],

                "Amount": amount,

                "BalanceBefore": balance_before,

                "BalanceAfter": balance_after

            })

            transaction_id += 1

            
            
            # SYSTEM GENERATED TRANSACTIONS
            

            if transaction["TransactionCode"] in [

                "IB_OUT",
                "NIP_OUT"

            ]:

                running_balance = add_system_transaction(

                    transaction_code="TRANSFER_FEE",

                    amount=TRANSFER_FEE,

                    account=account,

                    customer=customer,

                    current_month=current_month,

                    transaction_date=transaction_date,

                    running_balance=running_balance

                )

                running_balance = add_system_transaction(

                    transaction_code="VAT_CHARGE",

                    amount=VAT_AMOUNT,

                    account=account,

                    customer=customer,

                    current_month=current_month,

                    transaction_date=transaction_date,

                    running_balance=running_balance

                )

        
        month_end_date = generate_transaction_date(

            current_month

        )

        running_balance = generate_month_end_postings(

            account,

            customer,

            current_month,

            month_end_date,

            running_balance,

            monthly_debit_total

        )

        

        current_month = (
            pd.Timestamp(current_month)
            + pd.DateOffset(months=1)
        ).to_pydatetime()


if MAX_DEVELOPMENT_ACCOUNTS is None:

    sample_accounts = account_df

else:

    sample_accounts = account_df.head(
        MAX_DEVELOPMENT_ACCOUNTS
    )

output_path = os.path.join(

    project_root,

    "Data",

    "Facts",

    "FactTransaction.csv"

)

checkpoint_path = os.path.join(

    project_root,

    "Data",

    "Checkpoints",

    "transaction_checkpoint.txt"

)


start_index = 0

if os.path.exists(checkpoint_path):

    with open(checkpoint_path, "r") as f:

        start_index = int(f.read())

    print(f"Resuming from account {start_index:,}")

counter = start_index

for index, account in sample_accounts.iloc[start_index:].iterrows():

    counter += 1

    if counter % 1000 == 0:

        print(
            f"Processed {counter:,} accounts..."
        )

    customer = customer_df[
        customer_df["CustomerID"] ==
        account["CustomerID"]
    ].iloc[0]

    generate_monthly_transactions(
        account,
        customer
    )

    if counter % 1000 == 0:

        pd.DataFrame(

            batch_transactions

        ).to_csv(

            output_path,

            mode="a",

            header=not os.path.exists(output_path),

            index=False

        )

        batch_transactions.clear()

        with open(

            checkpoint_path,

            "w"

        ) as f:

            f.write(str(counter))

        print(
            f"Checkpoint saved ({counter:,} accounts)"
        )

print()

print("=" * 60)
print("TRANSACTIONS GENERATED")
print("=" * 60)




if batch_transactions:

    pd.DataFrame(

        batch_transactions

    ).to_csv(

        output_path,

        mode="a",

        header=False,

        index=False

    )

    batch_transactions.clear()

transaction_df = pd.read_csv(output_path)

if os.path.exists(checkpoint_path):

    os.remove(checkpoint_path)

print()

print(f"Transactions generated: {len(transaction_df):,}")

print(f"Saved to: {output_path}")

print()
print(f"Failed Transactions: {failed_transactions:,}")

print()

print("=" * 60)

print("SUMMARY")

print("=" * 60)

print(f"Accounts processed : {len(sample_accounts):,}")

print(f"Transactions       : {len(transaction_df):,}")

print(f"Failed Transactions: {failed_transactions:,}")

print()

print(

    transaction_df

    .groupby("Direction")

    .size()

)

