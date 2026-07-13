'''
import pandas as pd

from datetime import datetime

import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)


# TRANSACTION HISTORY

START_DATE = "2016-01-01"
END_DATE = "2026-06-30"


# ALL DATES

dates = pd.date_range(
    start=START_DATE,
    end=END_DATE,
    freq="D"
)


# CREATE THE DATAFRAME

dim_date = pd.DataFrame()

dim_date["Date"] = dates

# CREATE DATEKEY

dim_date["DateKey"] = (
    dim_date["Date"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)

dim_date["Year"] = dim_date["Date"].dt.year

dim_date["Quarter"] = dim_date["Date"].dt.quarter

dim_date["MonthNumber"] = dim_date["Date"].dt.month

dim_date["MonthName"] = dim_date["Date"].dt.month_name()

dim_date["Day"] = dim_date["Date"].dt.day

dim_date["DayName"] = dim_date["Date"].dt.day_name()

dim_date["WeekNumber"] = dim_date["Date"].dt.isocalendar().week.astype(int)

dim_date["MonthYear"] = dim_date["Date"].dt.strftime("%b %Y")

dim_date["QuarterName"] = (
    "Q"
    + dim_date["Quarter"].astype(str)
)

dim_date["FinancialYear"] = dim_date["Year"]

dim_date["IsWeekend"] = (
    dim_date["Date"]
    .dt.weekday
    >= 5
)


dim_date["IsMonthEnd"] = (
    dim_date["Date"]
    ==
    dim_date["Date"] + pd.offsets.MonthEnd(0)
)



dim_date["MonthEndDate"] = (
    dim_date["Date"]
    + pd.offsets.MonthEnd(0)
)

dim_date["IsMonthStart"] = (
    dim_date["Date"]
    ==
    dim_date["Date"] + pd.offsets.MonthBegin(0)
)

dim_date["DaysInMonth"] = (
    dim_date["Date"]
    .dt.days_in_month
)

dim_date["IsLeapYear"] = (
    dim_date["Date"]
    .dt.is_leap_year
)

dim_date["MonthYear"] = dim_date["Date"].dt.strftime("%b %Y")

dim_date["YearMonthKey"] = (
    dim_date["Date"]
    .dt.strftime("%Y%m")
    .astype(int)
)

dim_date["YearQuarter"] = (
    dim_date["Year"].astype(str)
    + " Q"
    + dim_date["Quarter"].astype(str)
)


dim_date = dim_date[
    [
        "DateKey",
        "Date",
        "Year",
        "Quarter",
        "QuarterName",
        "MonthNumber",
        "MonthName",
        "MonthYear",
        "YearMonthKey",
        "WeekNumber",
        "Day",
        "DayName",
        "FinancialYear",
        "DaysInMonth",
        "MonthEndDate",
        "IsWeekend",
        "IsMonthStart",
        "IsMonthEnd",
        "IsLeapYear"
    ]
]


output_file = (
    project_root
    + r"\Data\Dimensions\DimDate.csv"
)

dim_date.to_csv(
    output_file,
    index=False
)

print("=" * 60)
print("DIM DATE CREATED SUCCESSFULLY")
print("=" * 60)

print(f"Rows : {len(dim_date):,}")

print()

print(dim_date.head())
'''


import pandas as pd

df = pd.read_csv("Data/Dimensions/DimDate.csv")

print(df.columns.tolist())