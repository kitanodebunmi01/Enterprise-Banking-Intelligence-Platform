/*
Enterprise Banking Intelligence & Early Warning Platform
Module 02 - Create Fact Tables

Description:

Creates all fact tables for the Enterprise Banking
Intelligence & Early Warning Platform (EBIEWP).
*/

USE EBIEWP;
GO

CREATE TABLE dbo.FactTransaction
(

    TransactionID BIGINT NOT NULL,

    AccountID INT NOT NULL,

    CustomerID INT NOT NULL,

    BranchID INT NOT NULL,

    DateKey INT NOT NULL,

    TransactionTypeID TINYINT NOT NULL,

    Amount DECIMAL(18,2) NOT NULL,

    BalanceBefore DECIMAL(18,2) NOT NULL,

    BalanceAfter DECIMAL(18,2) NOT NULL

);

GO

------------------------------------------------------------------------------

CREATE TABLE dbo.FactLoan
(

    LoanID INT NOT NULL,

    CustomerID INT NOT NULL,

    AccountID INT NOT NULL,

    BranchID INT NOT NULL,

    DateKey INT NOT NULL,

    LoanProduct VARCHAR(50) NOT NULL,

    Currency CHAR(3) NOT NULL,

    OriginalLoanAmount DECIMAL(18,2) NOT NULL,

    MonthlyInstallment DECIMAL(18,2) NOT NULL,

    OutstandingPrincipal DECIMAL(18,2) NOT NULL,

    InterestRate DECIMAL(5,2) NOT NULL,

    TenureMonths SMALLINT NOT NULL,

    DisbursementDate DATE NOT NULL,

    MaturityDate DATE NOT NULL,

    LoanStatus VARCHAR(20) NOT NULL

);

GO

--------------------------------------------------------------------

CREATE TABLE dbo.FactRepayment
(

    RepaymentID INT NOT NULL,

    LoanID INT NOT NULL,

    CustomerID INT NOT NULL,

    AccountID INT NOT NULL,

    BranchID INT NOT NULL,

    DateKey INT NOT NULL,

    LoanAgeMonths SMALLINT NOT NULL,

    ScheduledPaymentDate DATE NOT NULL,

    ActualPaymentDate DATE NULL,

    ExpectedAmount DECIMAL(18,2) NOT NULL,

    AmountPaid DECIMAL(18,2) NOT NULL,

    PaymentStatus VARCHAR(20) NOT NULL,

    PaymentBehaviour VARCHAR(30) NOT NULL,

    ConsecutiveMissedPayments TINYINT NOT NULL,

    DaysPastDue SMALLINT NOT NULL,

    OutstandingPrincipal DECIMAL(18,2) NOT NULL

);

GO

-----------------------------------------------------------------------

CREATE TABLE dbo.FactComplaint
(

    ComplaintID INT NOT NULL,

    CustomerID INT NOT NULL,

    AccountID INT NOT NULL,

    BranchID INT NOT NULL,

    DateKey INT NOT NULL,

    ComplaintDate DATE NOT NULL,

    ComplaintCategory VARCHAR(50) NOT NULL,

    ComplaintChannel VARCHAR(30) NOT NULL,

    Severity VARCHAR(20) NOT NULL,

    ResolutionStatus VARCHAR(20) NOT NULL,

    ResolutionDays SMALLINT NOT NULL,

    MetSLA BIT NOT NULL,

    ResolutionDate DATE NULL,

    CustomerSatisfaction VARCHAR(20) NOT NULL,

    ComplaintBehaviour VARCHAR(30) NOT NULL,

    RepeatComplaintCount TINYINT NOT NULL

);

GO

-------------------------------------------------------------------

