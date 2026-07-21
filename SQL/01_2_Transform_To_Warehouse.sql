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

TRUNCATE TABLE dbo.DimTransactionType;
GO

INSERT INTO dbo.DimTransactionType
(

    TransactionTypeID,

    TransactionCode,

    TransactionCategory,

    TransactionType,

    Direction,

    Channel

)

SELECT

    TransactionTypeID,

    TransactionCode,

    TransactionCategory,

    TransactionType,

    Direction,

    Channel

FROM stg.DimTransactionType;

GO

SELECT COUNT(*) AS WarehouseRows

FROM dbo.DimTransactionType;

SELECT *

FROM dbo.DimTransactionType;

GO

---------------------------------------------------------------

TRUNCATE TABLE dbo.FactTransaction;
GO

INSERT INTO dbo.FactTransaction
(
    TransactionID,
    AccountID,
    CustomerID,
    BranchID,
    DateKey,
    TransactionTypeID,
    Amount,
    BalanceBefore,
    BalanceAfter
)

SELECT

    TransactionID,

    AccountID,

    CustomerID,

    BranchID,

    DateKey,

    TransactionTypeID,

    Amount,

    BalanceBefore,

    BalanceAfter

FROM stg.FactTransaction;

GO

SELECT COUNT(*) AS WarehouseRows
FROM dbo.FactTransaction;

GO

SELECT TOP (10) *
FROM dbo.FactTransaction;

GO

------------------------------------------------------------------------------------

TRUNCATE TABLE dbo.FactLoan;
GO

INSERT INTO dbo.FactLoan
(

    LoanID,

    CustomerID,

    AccountID,

    BranchID,

    DateKey,

    LoanProduct,

    Currency,

    OriginalLoanAmount,

    MonthlyInstallment,

    OutstandingPrincipal,

    InterestRate,

    TenureMonths,

    DisbursementDate,

    MaturityDate,

    LoanStatus

)

SELECT

    LoanID,

    CustomerID,

    AccountID,

    BranchID,

    DateKey,

    LoanProduct,

    Currency,

    OriginalLoanAmount,

    MonthlyInstallment,

    OutstandingPrincipal,

    InterestRate,

    TenureMonths,

    DisbursementDate,

    MaturityDate,

    LoanStatus

FROM stg.FactLoan;

GO

SELECT COUNT(*) AS WarehouseRows

FROM dbo.FactLoan;

GO

SELECT TOP (10) *

FROM dbo.FactLoan;

GO

--------------------------------------------------------------------------------------------

TRUNCATE TABLE dbo.FactRepayment;
GO

INSERT INTO dbo.FactRepayment
(

    RepaymentID,

    LoanID,

    CustomerID,

    AccountID,

    BranchID,

    DateKey,

    LoanAgeMonths,

    ScheduledPaymentDate,

    ActualPaymentDate,

    ExpectedAmount,

    AmountPaid,

    PaymentStatus,

    PaymentBehaviour,

    ConsecutiveMissedPayments,

    DaysPastDue,

    OutstandingPrincipal

)

SELECT

    RepaymentID,

    LoanID,

    CustomerID,

    AccountID,

    BranchID,

    DateKey,

    LoanAgeMonths,

    TRY_CONVERT(DATE, ScheduledPaymentDate, 103),

    CASE

        WHEN ActualPaymentDate IS NULL

             OR LTRIM(RTRIM(ActualPaymentDate)) = ''

        THEN NULL

        ELSE TRY_CONVERT(DATE, ActualPaymentDate, 103)

    END,

    ExpectedAmount,

    AmountPaid,

    PaymentStatus,

    PaymentBehaviour,

    ConsecutiveMissedPayments,

    DaysPastDue,

    OutstandingPrincipal

FROM stg.FactRepayment;

GO

----------------------------------------------------------

TRUNCATE TABLE dbo.FactComplaint;
GO

INSERT INTO dbo.FactComplaint
(
    ComplaintID,
    CustomerID,
    AccountID,
    BranchID,
    DateKey,
    ComplaintDate,
    ComplaintCategory,
    ComplaintChannel,
    Severity,
    ResolutionStatus,
    ResolutionDays,
    MetSLA,
    ResolutionDate,
    CustomerSatisfaction,
    ComplaintBehaviour,
    RepeatComplaintCount
)

SELECT

    ComplaintID,

    CustomerID,

    AccountID,

    BranchID,

    DateKey,

    CAST(ComplaintDate AS DATE),

    ComplaintCategory,

    ComplaintChannel,

    Severity,

    ResolutionStatus,

    ResolutionDays,

    CASE
        WHEN LOWER(LTRIM(RTRIM(MetSLA))) = 'yes' THEN 1
        ELSE 0
    END AS MetSLA,

    CASE
        WHEN ResolutionDate IS NULL
             OR LTRIM(RTRIM(ResolutionDate)) = ''
        THEN NULL
        ELSE CAST(ResolutionDate AS DATE)
    END AS ResolutionDate,

    CASE
        WHEN LTRIM(RTRIM(ResolutionStatus)) IN ('Pending', 'Escalated')
            THEN NULL
        ELSE CustomerSatisfaction
    END AS CustomerSatisfaction,

    ComplaintBehaviour,

    RepeatComplaintCount

FROM stg.FactComplaint;
GO

SELECT COUNT(*) AS WarehouseRows
FROM dbo.FactComplaint;
GO

SELECT TOP (10) *
FROM dbo.FactComplaint;
GO

---------------------------------------------------------------

