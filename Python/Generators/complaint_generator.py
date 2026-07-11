import pandas as pd
import random
import os

from datetime import timedelta

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

COMPLAINT_CATEGORY = [

    "Failed Transfer",

    "Card Issue",

    "Dispense Error",

    "Mobile App",

    "Internet Banking",

    "Unauthorized Debit",

    "Loan Service",

    "Account Restricted (PND)"

]

COMPLAINT_CHANNEL = [

    "Branch",

    "Call Centre",

    "Email",

    "Mobile App",

    "Social Media"

]


COMPLAINT_RATE = {

    "Retail": (2, 4),

    "SME": (2, 5),

    "HNWI": (2, 4),

    "UHNWI": (2, 4),

    "Corporate": (3, 6)

}


COMPLAINT_BEHAVIOUR = {

    "Stable": 0.70,

    "Increasing": 0.20,

    "High Friction": 0.10

}


COMPLAINT_CATEGORY_WEIGHTS = {

    "Retail": {

        "Failed Transfer": 30,

        "Card Issue": 20,

        "Dispense Error": 15,

        "Mobile App": 20,

        "Loan Service": 2,

        "Account Restricted (PND)": 3

    },

    "SME": {

        "Failed Transfer": 25,

        "Card Issue": 10,

        "Internet Banking": 20,

        "Unauthorized Debit": 15,

        "Loan Service": 10,

        "Account Restricted (PND)": 5

    },

    "HNWI": {

        "Failed Transfer": 15,

        "Card Issue": 20,

        "Dispense Error": 10,

        "Mobile App": 10,

        "Internet Banking": 15,

        "Unauthorized Debit": 10,

        "Loan Service": 15,

        "Account Restricted (PND)": 5

    },

    "UHNWI": {

        "Failed Transfer": 10,

        "Card Issue": 20,

        "Dispense Error": 10,

        "Mobile App": 10,

        "Internet Banking": 15,

        "Unauthorized Debit": 10,

        "Loan Service": 20,

        "Account Restricted (PND)": 5

    },

    "Corporate": {

        "Failed Transfer": 15,

        "Internet Banking": 30,

        "Unauthorized Debit": 10,

        "Loan Service": 20,

        "Account Restricted (PND)": 10

    }

}


SEVERITY_WEIGHTS = {

    "Failed Transfer": {

        "Low": 10,

        "Medium": 70,

        "High": 18,

        "Critical": 2

    },

    "Card Issue": {

        "Low": 20,

        "Medium": 60,

        "High": 18,

        "Critical": 2

    },

    "Dispense Error": {

        "Low": 5,

        "Medium": 55,

        "High": 35,

        "Critical": 5

    },

    "Mobile App": {

        "Low": 60,

        "Medium": 35,

        "High": 5,

        "Critical": 0

    },

    "Internet Banking": {

        "Low": 25,

        "Medium": 50,

        "High": 20,

        "Critical": 5

    },

    "Unauthorized Debit": {

        "Low": 0,

        "Medium": 15,

        "High": 55,

        "Critical": 30

    },

    "Loan Service": {

        "Low": 5,

        "Medium": 55,

        "High": 35,

        "Critical": 5

    },

    "Account Restricted (PND)": {

        "Low": 0,

        "Medium": 20,

        "High": 60,

        "Critical": 20

    }

}


RESOLUTION_STATUS_WEIGHTS = {

    "Low": {

        "Resolved": 95,

        "Pending": 5,

        "Escalated": 0

    },

    "Medium": {

        "Resolved": 85,

        "Pending": 12,

        "Escalated": 3

    },

    "High": {

        "Resolved": 65,

        "Pending": 25,

        "Escalated": 10

    },

    "Critical": {

        "Resolved": 40,

        "Pending": 35,

        "Escalated": 25

    }

}

RESOLUTION_TIME = {

    "Resolved": (1, 5),

    "Pending": (6, 30),

    "Escalated": (15, 90)

}

SLA_DAYS = {

    "Low": 5,

    "Medium": 10,

    "High": 15,

    "Critical": 30

}


COMPLAINT_CHANNEL_WEIGHTS = {

    "Failed Transfer": {

        "Call Centre": 40,

        "Branch": 25,

        "Email": 5,

        "Social Media": 5,

        "Mobile App": 0

    },

    "Card Issue": {

        "Branch": 45,

        "Call Centre": 40,

        "Email": 5,

        "Social Media": 5,

        "Mobile App": 0

    },

    "Dispense Error": {

        "Branch": 55,

        "Call Centre": 35,

        "Mobile App": 2,

        "Email": 3,

        "Social Media": 5

    },

    "Mobile App": {

        "Mobile App": 45,

        "Call Centre": 35,

        "Email": 10,

        "Social Media": 10,

        "Branch": 10

    },

    "Internet Banking": {

        "Call Centre": 45,

        "Email": 30,

        "Branch": 15,

        "Social Media": 5,

        "Mobile App": 0

    },

    "Unauthorized Debit": {

        "Branch": 45,

        "Call Centre": 40,

        "Email": 10,

        "Social Media": 5,

        "Mobile App": 0

    },

    "Loan Service": {

        "Branch": 55,

        "Email": 20,

        "Call Centre": 20,

        "Social Media": 5,

        "Mobile App": 0

    },

    "Account Restricted (PND)": {

        "Branch": 60,

        "Call Centre": 30,

        "Email": 5,

        "Social Media": 5,

        "Mobile App": 0

    }

}


CUSTOMER_SATISFACTION_WEIGHTS = {

    ("Low", "Resolved"): {

        "Satisfied": 90,

        "Neutral": 10,

        "Unsatisfied": 0

    },

    ("Medium", "Resolved"): {

        "Satisfied": 75,

        "Neutral": 20,

        "Unsatisfied": 5

    },

    ("High", "Resolved"): {

        "Satisfied": 55,

        "Neutral": 30,

        "Unsatisfied": 15

    },

    ("Critical", "Resolved"): {

        "Satisfied": 30,

        "Neutral": 35,

        "Unsatisfied": 35

    },

    ("Low", "Pending"): {

        "Satisfied": 20,

        "Neutral": 40,

        "Unsatisfied": 40

    },

    ("Medium", "Pending"): {

        "Satisfied": 10,

        "Neutral": 30,

        "Unsatisfied": 60

    },

    ("High", "Pending"): {

        "Satisfied": 5,

        "Neutral": 20,

        "Unsatisfied": 75

    },

    ("Critical", "Pending"): {

        "Satisfied": 0,

        "Neutral": 10,

        "Unsatisfied": 90

    },

    ("Low", "Escalated"): {

        "Satisfied": 5,

        "Neutral": 20,

        "Unsatisfied": 75

    },

    ("Medium", "Escalated"): {

        "Satisfied": 0,

        "Neutral": 15,

        "Unsatisfied": 85

    },

    ("High", "Escalated"): {

        "Satisfied": 0,

        "Neutral": 10,

        "Unsatisfied": 90

    },

    ("Critical", "Escalated"): {

        "Satisfied": 0,

        "Neutral": 5,

        "Unsatisfied": 95

    }

}

def determine_account_complaints(customer, account):

    """
    Determines the expected number
    of complaints for an account
    based on relationship length
    and customer segment.
    """

    segment = customer["CustomerSegment"]

    relationship_start = pd.to_datetime(

        account["DateOpened"]

    )

    today = pd.to_datetime(

        date_df["Date"].max()

    )

    relationship_years = max(

        1,

        (today - relationship_start).days / 365

    )

    complaints_per_year = random.randint(

        COMPLAINT_RATE[segment][0],

        COMPLAINT_RATE[segment][1]

    )

    return round(

        relationship_years *

        complaints_per_year

    )

def choose_complaint_category(customer):

    """
    Selects a complaint category
    based on customer segment.
    """

    segment = customer["CustomerSegment"]

    categories = list(

        COMPLAINT_CATEGORY_WEIGHTS[segment].keys()

    )

    weights = list(

        COMPLAINT_CATEGORY_WEIGHTS[segment].values()

    )

    return random.choices(

        categories,

        weights=weights,

        k=1

    )[0]


def determine_severity(

    complaint_category

):

    """
    Determines complaint severity
    based on complaint category.
    """

    severities = list(

        SEVERITY_WEIGHTS[

            complaint_category

        ].keys()

    )

    weights = list(

        SEVERITY_WEIGHTS[

            complaint_category

        ].values()

    )

    return random.choices(

        severities,

        weights=weights,

        k=1

    )[0]


def generate_complaint_dates(

    account,

    complaint_count,

    complaint_behaviour

):

    """
    Generates complaint dates
    across the customer's
    banking relationship.
    """

    account_opened = pd.to_datetime(

    account["DateOpened"]

    )

    today = pd.to_datetime(

        date_df["Date"].max()

    )

    relationship_days = (

        today -

        account_opened

    ).days


    if complaint_behaviour == "Stable":
        complaint_days = sorted(

            random.sample(

                range(

                    relationship_days + 1

                ),

                min(

                    complaint_count,

                    relationship_days + 1

                )

            )

        )

    elif complaint_behaviour == "Increasing":

        complaint_days = []

        early = int(

            relationship_days * 0.60

        )

        for _ in range(complaint_count):

            complaint_days.append(

                random.randint(

                    early,

                    relationship_days

                )

            )

        complaint_days.sort()


    else:

        complaint_days = []

        late = int(

            relationship_days * 0.80

        )

        for _ in range(complaint_count):

            complaint_days.append(

                random.randint(

                    late,

                    relationship_days

                )

            )

        complaint_days.sort()

    complaint_dates = []

    for day in complaint_days:

        complaint_dates.append(

            account_opened +

            timedelta(days=day)

        )

    return complaint_dates


def determine_complaint_behaviour():

    """
    Assigns a complaint behaviour profile.
    """

    return random.choices(

        population=list(

            COMPLAINT_BEHAVIOUR.keys()

        ),

        weights=list(

            COMPLAINT_BEHAVIOUR.values()

        ),

        k=1

    )[0]

def determine_resolution_status(

    severity

):

    """
    Determines resolution status
    based on complaint severity.
    """

    statuses = list(

        RESOLUTION_STATUS_WEIGHTS[

            severity

        ].keys()

    )

    weights = list(

        RESOLUTION_STATUS_WEIGHTS[

            severity

        ].values()

    )

    return random.choices(

        statuses,

        weights=weights,

        k=1

    )[0]


def determine_resolution_days(

    resolution_status

):

    """
    Returns the number of days
    required to resolve a complaint.
    """

    minimum, maximum = RESOLUTION_TIME[

        resolution_status

    ]

    return random.randint(

        minimum,

        maximum

    )


def determine_sla_status(

    severity,

    resolution_status,

    resolution_days

):

    """
    Determines whether the complaint
    was resolved within SLA.
    """

    if resolution_status != "Resolved":

        return "No"

    if resolution_days <= SLA_DAYS[severity]:

        return "Yes"

    return "No"


def determine_customer_satisfaction(

    severity,

    resolution_status

):

    """
    Determines customer satisfaction
    after complaint resolution.
    """

    outcomes = CUSTOMER_SATISFACTION_WEIGHTS[

        (

            severity,

            resolution_status

        )

    ]

    return random.choices(

        list(outcomes.keys()),

        weights=list(outcomes.values()),

        k=1

    )[0]

complaints = []

complaint_id = 1


def choose_complaint_channel(

    complaint_category

):

    """
    Selects the complaint channel
    based on complaint category.
    """

    channels = list(

        COMPLAINT_CHANNEL_WEIGHTS[

            complaint_category

        ].keys()

    )

    weights = list(

        COMPLAINT_CHANNEL_WEIGHTS[

            complaint_category

        ].values()

    )

    return random.choices(

        channels,

        weights=weights,

        k=1

    )[0]

def create_complaint_record(

    customer,

    account,

    complaint_date,

    complaint_behaviour,

    previous_categories

):
    
    global complaint_id

    complaint_category = choose_complaint_category(

        customer

    )

    complaint_channel = choose_complaint_channel(

        complaint_category

    )

    severity = determine_severity(

        complaint_category

    )

    resolution_status = determine_resolution_status(

        severity

    )

    resolution_days = determine_resolution_days(

        resolution_status

    )

    sla_status = determine_sla_status(

        severity,

        resolution_status,

        resolution_days

    )

    if resolution_status == "Resolved":

        resolution_date = (

            complaint_date +

            timedelta(days=resolution_days)

        )

    else:

        resolution_date = pd.NaT


    customer_satisfaction = (

        determine_customer_satisfaction(

            severity,

            resolution_status

        )

    )

    repeat_complaint_count = (

        previous_categories.get(

            complaint_category,

            0

        )

    )

    previous_categories[

        complaint_category

    ] = (

        repeat_complaint_count + 1

    )

    date_key = int(

        complaint_date.strftime(

            "%Y%m%d"

        )

    )

    complaints.append({

        "ComplaintID": complaint_id,

        "CustomerID": customer["CustomerID"],

        "AccountID": account["AccountID"],

        "BranchID": account["BranchID"],

        "DateKey": date_key,

        "ComplaintDate": complaint_date,

        "ComplaintCategory": complaint_category,

        "ComplaintChannel": complaint_channel,

        "Severity": severity,

        "ResolutionStatus": resolution_status,

        "ResolutionDays": resolution_days,

        "MetSLA": sla_status,

        "ResolutionDate": resolution_date,

        "CustomerSatisfaction": customer_satisfaction,

        "ComplaintBehaviour": complaint_behaviour,

        "RepeatComplaintCount": repeat_complaint_count

    })

    complaint_id += 1

print()

print("=" * 60)

print("GENERATING COMPLAINTS")

print("=" * 60)

for _, customer in customer_df.iterrows():

    if (_ + 1) % 10000 == 0:

        print(

            f"Processed {_ + 1:,} customers..."

        )

    customer_accounts = account_df[

        (account_df["CustomerID"] == customer["CustomerID"])

        &

        (account_df["AccountStatus"] == "Active")

    ]

    if customer_accounts.empty:

        continue

    complaint_behaviour = (

        determine_complaint_behaviour()

    )


    for _, account in customer_accounts.iterrows():
        complaint_count = (

            determine_account_complaints(

                customer,

                account

            )

        )

        if complaint_count == 0:

            continue

        complaint_dates = (

            generate_complaint_dates(

                account,

                complaint_count,

                complaint_behaviour

            )

        )

        previous_categories = {}

        for complaint_date in complaint_dates:
            create_complaint_record(

                customer,

                account,

                complaint_date,

                complaint_behaviour,

                previous_categories

            )

print()

print("=" * 60)

print("COMPLAINT GENERATION COMPLETED")

print("=" * 60)

print(

    f"Complaints Generated : {len(complaints):,}"

)

complaint_df = pd.DataFrame(

    complaints

)

print()

print(

    f"Unique Customers : {complaint_df['CustomerID'].nunique():,}"

)

print(

    f"Unique Accounts : {complaint_df['AccountID'].nunique():,}"

)

print(

    f"Unique Branches : {complaint_df['BranchID'].nunique():,}"

)

print()

print(

    complaint_df["Severity"].value_counts()

)

print()

print(

    complaint_df["ResolutionStatus"].value_counts()

)

print()

print(

    complaint_df["CustomerSatisfaction"].value_counts()

)

print()

print(

    complaint_df["ComplaintBehaviour"].value_counts()

)

output_path = os.path.join(

    project_root,

    "Data",

    "Facts",

    "FactComplaint.csv"

)

complaint_df.to_csv(

    output_path,

    index=False

)

print()

print("=" * 60)

print("FACT COMPLAINT EXPORTED")

print("=" * 60)

print(

    f"Output : {output_path}"

)
