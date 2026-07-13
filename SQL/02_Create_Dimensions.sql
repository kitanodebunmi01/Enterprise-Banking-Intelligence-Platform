/*
Enterprise Banking Intelligence & Early Warning Platform
Module 02 - Create Dimension Tables

Description:

Creates all dimension tables for the Enterprise Banking
Intelligence & Early Warning Platform (EBIEWP).
*/

USE EBIEWP;
GO

CREATE TABLE dbo.DimDate
(
	DateKey INT NOT NULL,

    [Date] DATE NOT NULL,

    [Year] SMALLINT NOT NULL,

    Quarter TINYINT NOT NULL,

    QuarterName VARCHAR(2) NOT NULL,

    MonthNumber TINYINT NOT NULL,

    MonthName VARCHAR(10) NOT NULL,

    MonthYear VARCHAR(10) NOT NULL,

    YearMonthKey INT NOT NULL,

    WeekNumber TINYINT NOT NULL,

    [Day] TINYINT NOT NULL,

    DayName VARCHAR(10) NOT NULL,

    FinancialYear SMALLINT NOT NULL,

    DaysInMonth TINYINT NOT NULL,

    MonthEndDate DATE NOT NULL,

    IsWeekend BIT NOT NULL,

    IsMonthStart BIT NOT NULL,

    IsMonthEnd BIT NOT NULL,

    IsLeapYear BIT NOT NULL

);

GO

-------------------------------------------------------------------------------------

CREATE TABLE dbo.DimBranch
(

    BranchID INT NOT NULL,

    BranchCode VARCHAR(10) NOT NULL,

    BranchName VARCHAR(100) NOT NULL,

    City VARCHAR(50) NOT NULL,

    BranchNumber INT NOT NULL,

    State VARCHAR(30) NOT NULL,

    Region VARCHAR(20) NOT NULL,

    OpeningDate DATE NOT NULL,

    EmployeeCount SMALLINT NOT NULL,

    BranchManagerID VARCHAR(10) NOT NULL,

    BranchManagerName VARCHAR(100) NOT NULL,

    BranchStatus VARCHAR(20) NOT NULL

);

GO

------------------------------------------------------------------------

CREATE TABLE dbo.DimCustomer
(

    CustomerID INT NOT NULL,

    BranchID INT NOT NULL,

    FirstName VARCHAR(50) NOT NULL,

    LastName VARCHAR(50) NOT NULL,

    Gender VARCHAR(10) NOT NULL,

    DateOfBirth DATE NOT NULL,

    Age TINYINT NOT NULL,

    PhoneNumber VARCHAR(20) NOT NULL,

    Email VARCHAR(100) NOT NULL,

    State VARCHAR(30) NOT NULL,

    City VARCHAR(50) NOT NULL,

    CustomerSegment VARCHAR(20) NOT NULL,

    Occupation VARCHAR(100) NOT NULL,

    AnnualIncome DECIMAL(18,2) NOT NULL,

    DateJoined DATE NOT NULL

);

GO

---------------------------------------------------------------------------------

CREATE TABLE dbo.DimAccount
(
    AccountID INT NOT NULL,

    AccountNumber VARCHAR(20) NOT NULL,

    CustomerID INT NOT NULL,

    BranchID INT NOT NULL,

    AccountType VARCHAR(30) NOT NULL,

    Currency CHAR(3) NOT NULL,

    AccountStatus VARCHAR(20) NOT NULL,

    DateOpened DATE NOT NULL,

    DateClosed DATE NULL,

    CurrentBalance DECIMAL(18,2) NOT NULL

);

GO

-------------------------------------------------------------------------------

