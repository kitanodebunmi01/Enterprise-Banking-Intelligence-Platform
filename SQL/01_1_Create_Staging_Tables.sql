/*
Enterprise Banking Intelligence & Early Warning Platform
Module 11 - Create Staging Tables

Description:

Creates the staging tables used for loading raw
CSV datasets before transformation into the
enterprise data warehouse.
*/

USE EBIEWP;
GO

CREATE TABLE stg.DimDate
(

    DateKey INT,

    [Date] DATE,

    [Year] SMALLINT,

    Quarter TINYINT,

    QuarterName VARCHAR(2),

    MonthNumber TINYINT,

    MonthName VARCHAR(10),

    MonthYear VARCHAR(10),

    YearMonthKey INT,

    WeekNumber TINYINT,

    [Day] TINYINT,

    DayName VARCHAR(10),

    FinancialYear SMALLINT,

    DaysInMonth TINYINT,

    MonthEndDate DATE,

    IsWeekend VARCHAR(5),

    IsMonthStart VARCHAR(5),

    IsMonthEnd VARCHAR(5),

    IsLeapYear VARCHAR(5)

);

GO

---------------------------------------------------------------------------

CREATE TABLE stg.DimBranch
(

    BranchID INT,

    BranchCode VARCHAR(10),

    BranchName VARCHAR(100),

    City VARCHAR(50),

    BranchNumber INT,

    State VARCHAR(30),

    Region VARCHAR(20),

    OpeningDate DATE,

    EmployeeCount SMALLINT,

    BranchManagerID VARCHAR(10),

    BranchManagerName VARCHAR(100),

    BranchStatus VARCHAR(20)

);

GO

---------------------------------------------------------------

CREATE TABLE stg.DimCustomer
(

    CustomerID INT,

    BranchID INT,

    FirstName VARCHAR(50),

    LastName VARCHAR(50),

    Gender VARCHAR(10),

    DateOfBirth DATE,

    Age TINYINT,

    PhoneNumber VARCHAR(20),

    Email VARCHAR(100),

    State VARCHAR(30),

    City VARCHAR(50),

    CustomerSegment VARCHAR(20),

    Occupation VARCHAR(100),

    AnnualIncome DECIMAL(18,2),

    DateJoined DATE

);

GO

----------------------------------------------------------------------

CREATE TABLE stg.DimAccount
(

    AccountID INT,

    AccountNumber VARCHAR(20),

    CustomerID INT,

    BranchID INT,

    AccountType VARCHAR(30),

    Currency CHAR(3),

    AccountStatus VARCHAR(20),

    DateOpened DATE,

    DateClosed DATE,

    CurrentBalance DECIMAL(18,2)

);

GO

------------------------------------------------------------------------

CREATE TABLE stg.DimTransactionType
(

    TransactionTypeID TINYINT,

    TransactionCode VARCHAR(20),

    TransactionCategory VARCHAR(30),

    TransactionType VARCHAR(50),

    Direction VARCHAR(10),

    Channel VARCHAR(30)

);

GO

-----------------------------------------------------

