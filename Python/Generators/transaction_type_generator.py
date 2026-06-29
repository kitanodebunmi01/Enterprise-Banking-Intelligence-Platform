import pandas as pd
import os


# TRANSACTION TYPE DATA

transaction_types = [

    
    # CASH TRANSACTIONS


    {
        "TransactionTypeID": 1,
        "TransactionCode": "CASH_DEP",
        "TransactionCategory": "Cash",
        "TransactionType": "Cash Deposit",
        "Direction": "Credit",
        "Channel": "Branch"
    },
    {
        "TransactionTypeID": 2,
        "TransactionCode": "CASH_WD",
        "TransactionCategory": "Cash",
        "TransactionType": "Cash Withdrawal",
        "Direction": "Debit",
        "Channel": "Branch"
    },
    {
        "TransactionTypeID": 3,
        "TransactionCode": "ATM_DEP",
        "TransactionCategory": "Cash",
        "TransactionType": "ATM Cash Deposit",
        "Direction": "Credit",
        "Channel": "ATM"
    },
    {
        "TransactionTypeID": 4,
        "TransactionCode": "ATM_WD",
        "TransactionCategory": "Cash",
        "TransactionType": "ATM Cash Withdrawal",
        "Direction": "Debit",
        "Channel": "ATM"
    },

    
    # TRANSFERS
    

    {
        "TransactionTypeID": 5,
        "TransactionCode": "IB_IN",
        "TransactionCategory": "Transfer",
        "TransactionType": "Intra-bank Transfer In",
        "Direction": "Credit",
        "Channel": "Internal Banking"
    },
    {
        "TransactionTypeID": 6,
        "TransactionCode": "IB_OUT",
        "TransactionCategory": "Transfer",
        "TransactionType": "Intra-bank Transfer Out",
        "Direction": "Debit",
        "Channel": "Internal Banking"
    },
    {
        "TransactionTypeID": 7,
        "TransactionCode": "NIP_IN",
        "TransactionCategory": "Transfer",
        "TransactionType": "Inter-bank Transfer In",
        "Direction": "Credit",
        "Channel": "NIP"
    },
    {
        "TransactionTypeID": 8,
        "TransactionCode": "NIP_OUT",
        "TransactionCategory": "Transfer",
        "TransactionType": "Inter-bank Transfer Out",
        "Direction": "Debit",
        "Channel": "NIP"
    },
    {
        "TransactionTypeID": 9,
        "TransactionCode": "SALARY_CR",
        "TransactionCategory": "Transfer",
        "TransactionType": "Salary Credit",
        "Direction": "Credit",
        "Channel": "Internal Clearing"
    },
    {
        "TransactionTypeID": 10,
        "TransactionCode": "STANDING_ORDER",
        "TransactionCategory": "Transfer",
        "TransactionType": "Standing Order",
        "Direction": "Debit",
        "Channel": "Standing Order"
    },
    {
        "TransactionTypeID": 11,
        "TransactionCode": "TRANSFER_FEE",
        "TransactionCategory": "Charges",
        "TransactionType": "Transfer Fee",
        "Direction": "Debit",
        "Channel": "Core Banking"
    },

    
    # CARD TRANSACTIONS
    

    {
        "TransactionTypeID": 12,
        "TransactionCode": "POS_PUR",
        "TransactionCategory": "Card",
        "TransactionType": "POS Purchase",
        "Direction": "Debit",
        "Channel": "POS"
    },
    {
        "TransactionTypeID": 13,
        "TransactionCode": "ONLINE_PUR",
        "TransactionCategory": "Card",
        "TransactionType": "Online Card Purchase",
        "Direction": "Debit",
        "Channel": "Card Network"
    },
    {
        "TransactionTypeID": 14,
        "TransactionCode": "CARD_REFUND",
        "TransactionCategory": "Card",
        "TransactionType": "Card Refund",
        "Direction": "Credit",
        "Channel": "Card Network"
    },
    {
        "TransactionTypeID": 15,
        "TransactionCode": "CARD_REV",
        "TransactionCategory": "Card",
        "TransactionType": "Card Reversal",
        "Direction": "Credit",
        "Channel": "Card Network"
    },
    {
        "TransactionTypeID": 16,
        "TransactionCode": "CARD_MAINT_FEE",
        "TransactionCategory": "Charges",
        "TransactionType": "Card Maintenance Fee",
        "Direction": "Debit",
        "Channel": "Core Banking"
    },

    
    # PAYMENTS

    {
        "TransactionTypeID": 17,
        "TransactionCode": "AIRTIME",
        "TransactionCategory": "Payment",
        "TransactionType": "Airtime Purchase",
        "Direction": "Debit",
        "Channel": "Mobile App"
    },
    {
        "TransactionTypeID": 18,
        "TransactionCode": "DATA",
        "TransactionCategory": "Payment",
        "TransactionType": "Data Purchase",
        "Direction": "Debit",
        "Channel": "Mobile App"
    },
    {
        "TransactionTypeID": 19,
        "TransactionCode": "ELECTRICITY",
        "TransactionCategory": "Payment",
        "TransactionType": "Electricity Bill",
        "Direction": "Debit",
        "Channel": "Mobile App"
    },
    {
        "TransactionTypeID": 20,
        "TransactionCode": "CABLETV",
        "TransactionCategory": "Payment",
        "TransactionType": "Cable TV Subscription",
        "Direction": "Debit",
        "Channel": "Mobile App"
    },
    {
        "TransactionTypeID": 21,
        "TransactionCode": "SCHOOL_FEES",
        "TransactionCategory": "Payment",
        "TransactionType": "School Fees",
        "Direction": "Debit",
        "Channel": "Mobile App"
    },
    {
        "TransactionTypeID": 22,
        "TransactionCode": "INSURANCE",
        "TransactionCategory": "Payment",
        "TransactionType": "Insurance Premium",
        "Direction": "Debit",
        "Channel": "Mobile App"
    },


    # FOREIGN EXCHANGE

    {
        "TransactionTypeID": 23,
        "TransactionCode": "FX_BUY",
        "TransactionCategory": "Foreign Exchange",
        "TransactionType": "FX Purchase",
        "Direction": "Debit",
        "Channel": "Treasury"
    },
    {
        "TransactionTypeID": 24,
        "TransactionCode": "FX_SELL",
        "TransactionCategory": "Foreign Exchange",
        "TransactionType": "FX Sale",
        "Direction": "Credit",
        "Channel": "Treasury"
    },
    {
        "TransactionTypeID": 25,
        "TransactionCode": "SWIFT_IN",
        "TransactionCategory": "Foreign Exchange",
        "TransactionType": "SWIFT Incoming",
        "Direction": "Credit",
        "Channel": "SWIFT"
    },
    {
        "TransactionTypeID": 26,
        "TransactionCode": "SWIFT_OUT",
        "TransactionCategory": "Foreign Exchange",
        "TransactionType": "SWIFT Outgoing",
        "Direction": "Debit",
        "Channel": "SWIFT"
    },

    
    # LENDING

    {
        "TransactionTypeID": 27,
        "TransactionCode": "LOAN_DISB",
        "TransactionCategory": "Lending",
        "TransactionType": "Loan Disbursement",
        "Direction": "Credit",
        "Channel": "Loan System"
    },
    {
        "TransactionTypeID": 28,
        "TransactionCode": "LOAN_REPAY",
        "TransactionCategory": "Lending",
        "TransactionType": "Loan Repayment",
        "Direction": "Debit",
        "Channel": "Loan System"
    },
    {
        "TransactionTypeID": 29,
        "TransactionCode": "LOAN_INT",
        "TransactionCategory": "Lending",
        "TransactionType": "Loan Interest Payment",
        "Direction": "Debit",
        "Channel": "Loan System"
    },
    {
        "TransactionTypeID": 30,
        "TransactionCode": "LOAN_PENALTY",
        "TransactionCategory": "Lending",
        "TransactionType": "Loan Penalty Charge",
        "Direction": "Debit",
        "Channel": "Loan System"
    },


    # INVESTMENTS

    {
        "TransactionTypeID": 31,
        "TransactionCode": "FD_PLACE",
        "TransactionCategory": "Investment",
        "TransactionType": "Fixed Deposit Placement",
        "Direction": "Debit",
        "Channel": "Branch"
    },
    {
        "TransactionTypeID": 32,
        "TransactionCode": "FD_MATURE",
        "TransactionCategory": "Investment",
        "TransactionType": "Fixed Deposit Maturity",
        "Direction": "Credit",
        "Channel": "Branch"
    },
    {
        "TransactionTypeID": 33,
        "TransactionCode": "FD_INT",
        "TransactionCategory": "Investment",
        "TransactionType": "Fixed Deposit Interest",
        "Direction": "Credit",
        "Channel": "Core Banking"
    },

    
    # CHARGES

    {
        "TransactionTypeID": 34,
        "TransactionCode": "SMS_FEE",
        "TransactionCategory": "Charges",
        "TransactionType": "SMS Alert Fee",
        "Direction": "Debit",
        "Channel": "Core Banking"
    },
    {
        "TransactionTypeID": 35,
        "TransactionCode": "ACCT_MAINT",
        "TransactionCategory": "Charges",
        "TransactionType": "Account Maintenance Fee",
        "Direction": "Debit",
        "Channel": "Core Banking"
    },
    {
        "TransactionTypeID": 36,
        "TransactionCode": "STAMP_DUTY",
        "TransactionCategory": "Charges",
        "TransactionType": "Stamp Duty",
        "Direction": "Debit",
        "Channel": "Core Banking"
    },
    {
        "TransactionTypeID": 37,
        "TransactionCode": "VAT_CHARGE",
        "TransactionCategory": "Charges",
        "TransactionType": "VAT on Charges",
        "Direction": "Debit",
        "Channel": "Core Banking"
    },


    # INTEREST

    {
        "TransactionTypeID": 38,
        "TransactionCode": "SAV_INT",
        "TransactionCategory": "Interest",
        "TransactionType": "Savings Interest Credit",
        "Direction": "Credit",
        "Channel": "Core Banking"
    },
    {
        "TransactionTypeID": 39,
        "TransactionCode": "CURR_INT",
        "TransactionCategory": "Interest",
        "TransactionType": "Current Account Interest",
        "Direction": "Credit",
        "Channel": "Core Banking"
    },

    
    # OPERATIONAL

    {
        "TransactionTypeID": 40,
        "TransactionCode": "DEBIT_REV",
        "TransactionCategory": "Operational",
        "TransactionType": "Debit Reversal",
        "Direction": "Credit",
        "Channel": "Operations"
    },
    {
        "TransactionTypeID": 41,
        "TransactionCode": "CREDIT_REV",
        "TransactionCategory": "Operational",
        "TransactionType": "Credit Reversal",
        "Direction": "Debit",
        "Channel": "Operations"
    },
    {
        "TransactionTypeID": 42,
        "TransactionCode": "FAILED_REV",
        "TransactionCategory": "Operational",
        "TransactionType": "Failed Transfer Reversal",
        "Direction": "Credit",
        "Channel": "Operations"
    },
    {
        "TransactionTypeID": 43,
        "TransactionCode": "MANUAL_CR",
        "TransactionCategory": "Operational",
        "TransactionType": "Manual Adjustment Credit",
        "Direction": "Credit",
        "Channel": "Operations"
    },
    {
        "TransactionTypeID": 44,
        "TransactionCode": "MANUAL_DR",
        "TransactionCategory": "Operational",
        "TransactionType": "Manual Adjustment Debit",
        "Direction": "Debit",
        "Channel": "Operations"
    },
    {
        "TransactionTypeID": 45,
        "TransactionCode": "FRAUD_REC",
        "TransactionCategory": "Operational",
        "TransactionType": "Fraud Recovery",
        "Direction": "Credit",
        "Channel": "Fraud Operations"
    }

]


# CREATE DATAFRAME


df_transaction_type = pd.DataFrame(transaction_types)

print(df_transaction_type)


# VALIDATION

print("=" * 60)
print("DIM TRANSACTION TYPE VALIDATION")
print("=" * 60)

print(f"\nTotal Transaction Types : {len(df_transaction_type)}")
print(f"Duplicate IDs           : {df_transaction_type['TransactionTypeID'].duplicated().sum()}")
print(f"Duplicate Codes         : {df_transaction_type['TransactionCode'].duplicated().sum()}")
print(f"Missing Values          : {df_transaction_type.isnull().sum().sum()}")

print("\nTransaction Categories")
print(df_transaction_type["TransactionCategory"].value_counts())

print("\nDirection")
print(df_transaction_type["Direction"].value_counts())

print("\nChannels")
print(df_transaction_type["Channel"].value_counts())

print("\nPreview")
print(df_transaction_type.head())


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
    "DimTransactionType.csv"
)

df_transaction_type.to_csv(
    output_file,
    index=False
)

print()

print("DimTransactionType exported successfully.")




