/*
Enterprise Banking Intelligence & Early Warning Platform
Module 05 - Transform Staging Data

Description:

Transforms raw staging data into the enterprise
data warehouse.
*/

USE EBIEWP;
GO

INSERT INTO dbo.DimDate
(
    DateKey,
    [Date],
    [Year],
    Quarter,
    QuarterName,
    MonthNumber,
    MonthName,
    MonthYear,
    YearMonthKey,
    WeekNumber,
    [Day],
    DayName,
    FinancialYear,
    DaysInMonth,
    MonthEndDate,
    IsWeekend,
    IsMonthStart,
    IsMonthEnd,
    IsLeapYear
)

SELECT

    DateKey,

    [Date],

    [Year],

    Quarter,

    QuarterName,

    MonthNumber,

    MonthName,

    MonthYear,

    YearMonthKey,

    WeekNumber,

    [Day],

    DayName,

    FinancialYear,

    DaysInMonth,

    MonthEndDate,

    CASE
        WHEN IsWeekend = 'True' THEN 1
        ELSE 0
    END,

    CASE
        WHEN IsMonthStart = 'True' THEN 1
        ELSE 0
    END,

    CASE
        WHEN IsMonthEnd = 'True' THEN 1
        ELSE 0
    END,

    CASE
        WHEN IsLeapYear = 'True' THEN 1
        ELSE 0
    END

FROM stg.DimDate;

GO

SELECT TOP 10 *

FROM dbo.DimDate;