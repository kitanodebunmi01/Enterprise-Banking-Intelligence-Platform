USE EBIEWP;
GO


-- FactTransaction


CREATE NONCLUSTERED INDEX IX_FactTransaction_CustomerID
ON dbo.FactTransaction(CustomerID);
GO

CREATE NONCLUSTERED INDEX IX_FactTransaction_AccountID
ON dbo.FactTransaction(AccountID);
GO

CREATE NONCLUSTERED INDEX IX_FactTransaction_BranchID
ON dbo.FactTransaction(BranchID);
GO

CREATE NONCLUSTERED INDEX IX_FactTransaction_DateKey
ON dbo.FactTransaction(DateKey);
GO

CREATE NONCLUSTERED INDEX IX_FactTransaction_TransactionTypeID
ON dbo.FactTransaction(TransactionTypeID);
GO

--------------------------------------------------------------------------------------------


-- FactLoan


CREATE NONCLUSTERED INDEX IX_FactLoan_CustomerID
ON dbo.FactLoan(CustomerID);
GO

CREATE NONCLUSTERED INDEX IX_FactLoan_AccountID
ON dbo.FactLoan(AccountID);
GO

CREATE NONCLUSTERED INDEX IX_FactLoan_BranchID
ON dbo.FactLoan(BranchID);
GO

CREATE NONCLUSTERED INDEX IX_FactLoan_DateKey
ON dbo.FactLoan(DateKey);
GO

----------------------------------------------------------------------------------


-- FactRepayment


CREATE NONCLUSTERED INDEX IX_FactRepayment_LoanID
ON dbo.FactRepayment(LoanID);
GO

CREATE NONCLUSTERED INDEX IX_FactRepayment_CustomerID
ON dbo.FactRepayment(CustomerID);
GO

CREATE NONCLUSTERED INDEX IX_FactRepayment_BranchID
ON dbo.FactRepayment(BranchID);
GO

CREATE NONCLUSTERED INDEX IX_FactRepayment_DateKey
ON dbo.FactRepayment(DateKey);
GO

---------------------------------------------------------------------------


-- FactComplaint


CREATE NONCLUSTERED INDEX IX_FactComplaint_CustomerID
ON dbo.FactComplaint(CustomerID);
GO

CREATE NONCLUSTERED INDEX IX_FactComplaint_AccountID
ON dbo.FactComplaint(AccountID);
GO

CREATE NONCLUSTERED INDEX IX_FactComplaint_BranchID
ON dbo.FactComplaint(BranchID);
GO

CREATE NONCLUSTERED INDEX IX_FactComplaint_DateKey
ON dbo.FactComplaint(DateKey);
GO

-------------------------------------------------------------------------

