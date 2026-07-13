/*
Enterprise Banking Intelligence & Early Warning Platform
Module 05 - Transform Staging Data

Description:

Transforms raw staging data into the enterprise
data warehouse.
*/

USE EBIEWP;
GO

TRUNCATE TABLE dbo.DimDate;
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

----------------------------------------------------------------

TRUNCATE TABLE dbo.DimBranch;
GO

INSERT INTO dbo.DimBranch
(
    BranchID,
    BranchCode,
    BranchName,
    City,
    BranchNumber,
    State,
    Region,
    OpeningDate,
    EmployeeCount,
    BranchManagerID,
    BranchManagerName,
    BranchStatus
)

SELECT

    BranchID,
    BranchCode,
    BranchName,
    City,
    BranchNumber,
    State,
    Region,
    OpeningDate,
    EmployeeCount,
    BranchManagerID,
    BranchManagerName,
    BranchStatus

FROM stg.DimBranch;

GO

SELECT COUNT(*) AS WarehouseRows
FROM dbo.DimBranch;

SELECT TOP (10) *
FROM dbo.DimBranch;

GO
-------------------------------------------------------------------------

TRUNCATE TABLE dbo.DimCustomer;
GO

INSERT INTO dbo.DimCustomer
(

    CustomerID,

    BranchID,

    FirstName,

    LastName,

    Gender,

    DateOfBirth,

    Age,

    PhoneNumber,

    Email,

    State,

    City,

    CustomerSegment,

    Occupation,

    AnnualIncome,

    DateJoined

)

SELECT

    CustomerID,

    BranchID,

    FirstName,

    LastName,

    Gender,

    DateOfBirth,

    Age,

    PhoneNumber,

    Email,

    State,

    City,

    CustomerSegment,

    Occupation,

    AnnualIncome,

    DateJoined

FROM stg.DimCustomer;

GO

SELECT COUNT(*) AS WarehouseRows
FROM dbo.DimCustomer;

SELECT TOP (10) *
FROM dbo.DimCustomer;

GO

-------------------------------------------------------------------------------------------

TRUNCATE TABLE dbo.DimAccount;
GO

INSERT INTO dbo.DimAccount
(
    AccountID,
    AccountNumber,
    CustomerID,
    BranchID,
    AccountType,
    Currency,
    AccountStatus,
    DateOpened,
    DateClosed,
    CurrentBalance
)

SELECT

    AccountID,

    AccountNumber,

    CustomerID,

    BranchID,

    AccountType,

    Currency,

    AccountStatus,

    DateOpened,

    DateClosed,

    CurrentBalance

FROM stg.DimAccount;

GO


SELECT COUNT(*) AS AccountRows
FROM dbo.DimAccount;

SELECT TOP (10) *
FROM dbo.DimAccount;

GO

----------------------------------------------------------------------------------

