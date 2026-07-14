/* 
Before creating the foreign keys, let us also verify that the foreign keys exist
*/

SELECT COUNT(*) AS InvalidCustomer
FROM dbo.FactTransaction ft
LEFT JOIN dbo.DimCustomer dc
ON ft.CustomerID = dc.CustomerID
WHERE dc.CustomerID IS NULL;
GO

SELECT COUNT(*) AS InvalidAccount
FROM dbo.FactTransaction ft
LEFT JOIN dbo.DimAccount da
ON ft.AccountID = da.AccountID
WHERE da.AccountID IS NULL;
GO

SELECT COUNT(*) AS InvalidBranch
FROM dbo.FactTransaction ft
LEFT JOIN dbo.DimBranch db
ON ft.BranchID = db.BranchID
WHERE db.BranchID IS NULL;
GO

SELECT COUNT(*) AS InvalidDate
FROM dbo.FactTransaction ft
LEFT JOIN dbo.DimDate dd
ON ft.DateKey = dd.DateKey
WHERE dd.DateKey IS NULL;
GO

SELECT COUNT(*) AS InvalidTransactionType
FROM dbo.FactTransaction ft
LEFT JOIN dbo.DimTransactionType dtt
ON ft.TransactionTypeID = dtt.TransactionTypeID
WHERE dtt.TransactionTypeID IS NULL;
GO

------------------------------------------------------------------------

USE EBIEWP;
GO


-- FactTransaction

ALTER TABLE dbo.FactTransaction
ADD CONSTRAINT FK_FactTransaction_DimCustomer
FOREIGN KEY (CustomerID)
REFERENCES dbo.DimCustomer(CustomerID);
GO

ALTER TABLE dbo.FactTransaction
ADD CONSTRAINT FK_FactTransaction_DimAccount
FOREIGN KEY (AccountID)
REFERENCES dbo.DimAccount(AccountID);
GO

ALTER TABLE dbo.FactTransaction
ADD CONSTRAINT FK_FactTransaction_DimBranch
FOREIGN KEY (BranchID)
REFERENCES dbo.DimBranch(BranchID);
GO

ALTER TABLE dbo.FactTransaction
ADD CONSTRAINT FK_FactTransaction_DimDate
FOREIGN KEY (DateKey)
REFERENCES dbo.DimDate(DateKey);
GO

ALTER TABLE dbo.FactTransaction
ADD CONSTRAINT FK_FactTransaction_DimTransactionType
FOREIGN KEY (TransactionTypeID)
REFERENCES dbo.DimTransactionType(TransactionTypeID);
GO

------------------------------------------------------------------------------


-- FactLoan


ALTER TABLE dbo.FactLoan
ADD CONSTRAINT FK_FactLoan_DimCustomer
FOREIGN KEY (CustomerID)
REFERENCES dbo.DimCustomer(CustomerID);
GO

ALTER TABLE dbo.FactLoan
ADD CONSTRAINT FK_FactLoan_DimAccount
FOREIGN KEY (AccountID)
REFERENCES dbo.DimAccount(AccountID);
GO

ALTER TABLE dbo.FactLoan
ADD CONSTRAINT FK_FactLoan_DimBranch
FOREIGN KEY (BranchID)
REFERENCES dbo.DimBranch(BranchID);
GO

ALTER TABLE dbo.FactLoan
ADD CONSTRAINT FK_FactLoan_DimDate
FOREIGN KEY (DateKey)
REFERENCES dbo.DimDate(DateKey);
GO

--------------------------------------------------------------------


-- FactRepayment

ALTER TABLE dbo.FactRepayment
ADD CONSTRAINT FK_FactRepayment_FactLoan
FOREIGN KEY (LoanID)
REFERENCES dbo.FactLoan(LoanID);
GO

ALTER TABLE dbo.FactRepayment
ADD CONSTRAINT FK_FactRepayment_DimCustomer
FOREIGN KEY (CustomerID)
REFERENCES dbo.DimCustomer(CustomerID);
GO

ALTER TABLE dbo.FactRepayment
ADD CONSTRAINT FK_FactRepayment_DimAccount
FOREIGN KEY (AccountID)
REFERENCES dbo.DimAccount(AccountID);
GO

ALTER TABLE dbo.FactRepayment
ADD CONSTRAINT FK_FactRepayment_DimBranch
FOREIGN KEY (BranchID)
REFERENCES dbo.DimBranch(BranchID);
GO

ALTER TABLE dbo.FactRepayment
ADD CONSTRAINT FK_FactRepayment_DimDate
FOREIGN KEY (DateKey)
REFERENCES dbo.DimDate(DateKey);
GO

-----------------------------------------------------------------------------


-- FactComplaint


ALTER TABLE dbo.FactComplaint
ADD CONSTRAINT FK_FactComplaint_DimCustomer
FOREIGN KEY (CustomerID)
REFERENCES dbo.DimCustomer(CustomerID);
GO

ALTER TABLE dbo.FactComplaint
ADD CONSTRAINT FK_FactComplaint_DimAccount
FOREIGN KEY (AccountID)
REFERENCES dbo.DimAccount(AccountID);
GO

ALTER TABLE dbo.FactComplaint
ADD CONSTRAINT FK_FactComplaint_DimBranch
FOREIGN KEY (BranchID)
REFERENCES dbo.DimBranch(BranchID);
GO

ALTER TABLE dbo.FactComplaint
ADD CONSTRAINT FK_FactComplaint_DimDate
FOREIGN KEY (DateKey)
REFERENCES dbo.DimDate(DateKey);
GO


