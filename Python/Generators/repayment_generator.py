import pandas as pd
import random
import os

from datetime import timedelta
from pandas.tseries.offsets import DateOffset

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

loan_df = pd.read_csv(
    os.path.join(
        project_root,
        "Data",
        "Facts",
        "FactLoan.csv"
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

loan_df = loan_df[

    loan_df["LoanStatus"] == "Active"

].copy()

loan_df.reset_index(

    drop=True,

    inplace=True

)

print("=" * 60)
print("DATA LOADED SUCCESSFULLY")
print("=" * 60)

print(f"Active Loans : {len(loan_df):,}")
print(f"Dates        : {len(date_df):,}")

repayments = []

repayment_id = 1


PAYMENT_BEHAVIOUR = {

    "Good Payer": 0.75,

    "Average Payer": 0.20,

    "High Risk": 0.05

}

def determine_payment_status(

    behaviour

):

    if behaviour == "Good Payer":

        weights = [

            0.95,

            0.03,

            0.01,

            0.01

        ]

    elif behaviour == "Average Payer":

        weights = [

            0.75,

            0.15,

            0.05,

            0.05

        ]

    else:

        weights = [

            0.35,

            0.25,

            0.15,

            0.25

        ]

    return random.choices(

        [

            "Paid",

            "Late",

            "Partial",

            "Missed"

        ],

        weights=weights,

        k=1

    )[0]


def determine_payment_behaviour():

    return random.choices(

        population=list(

            PAYMENT_BEHAVIOUR.keys()

        ),

        weights=list(

            PAYMENT_BEHAVIOUR.values()

        ),

        k=1

    )[0]




def create_repayment_record(

    loan,

    scheduled_payment_date,

    outstanding_principal,

    consecutive_missed_payments

):

    global repayment_id

    payment_status = determine_payment_status(
        loan["PaymentBehaviour"]
    )


    expected_amount = loan["MonthlyInstallment"]

    amount_paid = min(

        expected_amount,

        outstanding_principal

    )

    days_past_due = 0


    if payment_status == "Paid":

        actual_payment_date = scheduled_payment_date

    elif payment_status == "Late":

        days_past_due = random.randint(

            1,

            15

        )

        actual_payment_date = (

            scheduled_payment_date +

            timedelta(days=days_past_due)

        )

    elif payment_status == "Partial":

        amount_paid = round(

            min(

                outstanding_principal,

                expected_amount *

                random.uniform(

                    0.40,

                    0.90

                )

            ),

            2

        )

        actual_payment_date = scheduled_payment_date

    else:

        amount_paid = 0

        actual_payment_date = pd.NaT

        days_past_due = random.randint(

            16,

            90

        )


    # Update consecutive missed repayments

    if payment_status == "Missed":

        consecutive_missed_payments += 1

    else:

        consecutive_missed_payments = 0



    # Update outstanding balance

    outstanding_principal = max(

        0,

        outstanding_principal - amount_paid

    )



    date_key = int(

        scheduled_payment_date.strftime(

            "%Y%m%d"

        )

    )

    loan_age_months = (

        (scheduled_payment_date.year - pd.to_datetime(

            loan["DisbursementDate"]

        ).year) * 12 +

        (

            scheduled_payment_date.month -

            pd.to_datetime(

                loan["DisbursementDate"]

            ).month

        )

    )

    repayments.append({

        "RepaymentID": repayment_id,

        "LoanID": loan["LoanID"],

        "CustomerID": loan["CustomerID"],

        "AccountID": loan["AccountID"],

        "BranchID": loan["BranchID"],

        "DateKey": date_key,

        "LoanAgeMonths": loan_age_months,

        "ScheduledPaymentDate": scheduled_payment_date,

        "ActualPaymentDate": actual_payment_date,

        "ExpectedAmount": expected_amount,

        "AmountPaid": amount_paid,

        "PaymentStatus": payment_status,

        "PaymentBehaviour": loan["PaymentBehaviour"],

        "ConsecutiveMissedPayments": consecutive_missed_payments,

        "DaysPastDue": days_past_due,

        "OutstandingPrincipal": outstanding_principal

    })

    repayment_id += 1

    # Customer behaviour may deteriorate over time

    if loan["PaymentBehaviour"] == "Good Payer":

        if random.random() < 0.01:

            loan["PaymentBehaviour"] = "Average Payer"

    elif loan["PaymentBehaviour"] == "Average Payer":

        if random.random() < 0.03:

            loan["PaymentBehaviour"] = "High Risk"

    return (
        
        outstanding_principal,

        consecutive_missed_payments
    )
            


print()

print("=" * 60)

print("GENERATING REPAYMENTS")

print("=" * 60)

for _, loan in loan_df.iterrows():

    if (_ + 1) % 1000 == 0:

        print(

            f"Processed {_ + 1:,} loans..."

        )

    loan["PaymentBehaviour"] = (

        determine_payment_behaviour()

    )

    disbursement_date = pd.to_datetime(

        loan["DisbursementDate"]

    )

    first_repayment_date = (

        disbursement_date +

        DateOffset(months=1)

    )

    today = pd.to_datetime(

        date_df["Date"].max()

    )

    last_repayment_date = min(

        today,

        pd.to_datetime(

            loan["MaturityDate"]

        )

    )

    outstanding_principal = loan["OutstandingPrincipal"]

    consecutive_missed_payments = 0

    scheduled_payment_date = first_repayment_date

    while (

        scheduled_payment_date <= last_repayment_date

        and

        outstanding_principal > 0

    ):
        (

            outstanding_principal,

            consecutive_missed_payments

        ) = create_repayment_record(

            loan,

            scheduled_payment_date,

            outstanding_principal,

            consecutive_missed_payments

        )

        scheduled_payment_date += DateOffset(

            months=1

        )



repayment_df = pd.DataFrame(

    repayments

)

output_path = os.path.join(

    project_root,

    "Data",

    "Facts",

    "FactRepayment.csv"

)

repayment_df.to_csv(

    output_path,

    index=False

)

print()

print("=" * 60)

print("REPAYMENTS GENERATED")

print("=" * 60)

print(

    f"Repayments Generated : {len(repayment_df):,}"

)

print(

    f"Output : {output_path}"

)

print(

    f"Unique Loans : {repayment_df['LoanID'].nunique():,}"

)
