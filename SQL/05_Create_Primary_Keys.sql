/*
Checking there are no duplicates first before setting our PK and FK
*/

ALTER TABLE dbo.FactTransaction
ADD FactTransactionKey BIGINT IDENTITY(1,1);
GO

SELECT COUNT(*) AS TotalRows,
       COUNT(DISTINCT TransactionID) AS UniqueRows,
       COUNT(DISTINCT FactTransactionKey) AS UniqueTransactionKey
FROM dbo.FactTransaction;
GO

SELECT COUNT(*) AS TotalRows,
       COUNT(DISTINCT LoanID) AS UniqueRows
FROM dbo.FactLoan;
GO

SELECT COUNT(*) AS TotalRows,
       COUNT(DISTINCT RepaymentID) AS UniqueRows
FROM dbo.FactRepayment;
GO

SELECT COUNT(*) AS TotalRows,
       COUNT(DISTINCT ComplaintID) AS UniqueRows
FROM dbo.FactComplaint;
GO

SELECT COUNT(*) AS TotalRows,
       COUNT(DISTINCT DateKey) AS UniqueRows
FROM dbo.DimDate;
GO

SELECT COUNT(*) AS TotalRows,
       COUNT(DISTINCT BranchID) AS UniqueRows
FROM dbo.DimBranch;
GO

SELECT COUNT(*) AS TotalRows,
       COUNT(DISTINCT CustomerID) AS UniqueRows
FROM dbo.DimCustomer;
GO

SELECT COUNT(*) AS TotalRows,
       COUNT(DISTINCT AccountID) AS UniqueRows
FROM dbo.DimAccount;
GO

SELECT COUNT(*) AS TotalRows,
       COUNT(DISTINCT TransactionTypeID) AS UniqueRows
FROM dbo.DimTransactionType;
GO

--------------------------------------------------------------------

USE EBIEWP;
GO


-- DIMENSIONS


ALTER TABLE dbo.DimDate
ADD CONSTRAINT PK_DimDate
PRIMARY KEY (DateKey);
GO

ALTER TABLE dbo.DimBranch
ADD CONSTRAINT PK_DimBranch
PRIMARY KEY (BranchID);
GO

ALTER TABLE dbo.DimCustomer
ADD CONSTRAINT PK_DimCustomer
PRIMARY KEY (CustomerID);
GO

ALTER TABLE dbo.DimAccount
ADD CONSTRAINT PK_DimAccount
PRIMARY KEY (AccountID);
GO

ALTER TABLE dbo.DimTransactionType
ADD CONSTRAINT PK_DimTransactionType
PRIMARY KEY (TransactionTypeID);
GO


-- FACTS


ALTER TABLE dbo.FactTransaction
ADD CONSTRAINT PK_FactTransaction
PRIMARY KEY (FactTransactionKey);
GO

ALTER TABLE dbo.FactLoan
ADD CONSTRAINT PK_FactLoan
PRIMARY KEY (LoanID);
GO

ALTER TABLE dbo.FactRepayment
ADD CONSTRAINT PK_FactRepayment
PRIMARY KEY (RepaymentID);
GO

ALTER TABLE dbo.FactComplaint
ADD CONSTRAINT PK_FactComplaint
PRIMARY KEY (ComplaintID);
GO