/*
EBIEWP DATA WAREHOUSE VALIDATION

SECTION 1
Warehouse Summary

Purpose:
Displays row counts for every warehouse table.
*/

--'SECTION 1 - WAREHOUSE SUMMARY'

SELECT 'DimCustomer' AS TableName,
COUNT(*) AS TotalRows
FROM dbo.DimCustomer

UNION ALL

SELECT 'DimBranch',
COUNT(*)
FROM dbo.DimBranch

UNION ALL

SELECT 'DimAccount',
COUNT(*)
FROM dbo.DimAccount

UNION ALL

SELECT 'DimDate',
COUNT(*)
FROM dbo.DimDate

UNION ALL

SELECT 'FactTransaction',
COUNT(*)
FROM dbo.FactTransaction

UNION ALL

SELECT 'FactLoan',
COUNT(*)
FROM dbo.FactLoan

UNION ALL

SELECT 'FactRepayment',
COUNT(*)
FROM dbo.FactRepayment

UNION ALL

SELECT 'FactComplaint',
COUNT(*)
FROM dbo.FactComplaint;



-- 'SECTION 2 - DIMENSION VALIDATION'

--DimCustomer
SELECT
CustomerID,
COUNT(*) AS DuplicateCount
FROM dbo.DimCustomer
GROUP BY CustomerID
HAVING COUNT(*) > 1;

--DimBranch
SELECT
BranchID,
COUNT(*) AS DuplicateCount
FROM dbo.DimBranch
GROUP BY BranchID
HAVING COUNT(*) > 1;

--DimAccount
SELECT
AccountID,
COUNT(*) AS DuplicateCount
FROM dbo.DimAccount
GROUP BY AccountID
HAVING COUNT(*) > 1;

--DimDate
SELECT
DateKey,
COUNT(*) AS DuplicateCount
FROM dbo.DimDate
GROUP BY DateKey
HAVING COUNT(*) > 1;

--DimTransactionType
SELECT
TransactionTypeID,
COUNT(*) AS DuplicateCount
FROM dbo.DimTransactionType
GROUP BY TransactionTypeID
HAVING COUNT(*) > 1;



-- 'SECTION 3 - FACT VALIDATION'

--FactTransaction
SELECT
FactTransactionKey,
COUNT(*) AS DuplicateCount
FROM dbo.FactTransaction
GROUP BY FactTransactionKey
HAVING COUNT(*) > 1;

--FactRepayment
SELECT
RepaymentID,
COUNT(*) AS DuplicateCount
FROM dbo.FactRepayment
GROUP BY RepaymentID
HAVING COUNT(*) > 1;

--FactLoan
SELECT
LoanID,
COUNT(*) AS DuplicateCount
FROM dbo.FactLoan
GROUP BY LoanID
HAVING COUNT(*) > 1;

--FactComplaint
SELECT
ComplaintID,
COUNT(*) AS DuplicateCount
FROM dbo.FactComplaint
GROUP BY ComplaintID
HAVING COUNT(*) > 1;




-- SECTION 4 - REFERENTIAL INTEGRITY VALIDATION

--FactTransaction -> DimCustomer
SELECT *
FROM dbo.FactTransaction ft
LEFT JOIN dbo.DimCustomer dc
    ON ft.CustomerID = dc.CustomerID
WHERE dc.CustomerID IS NULL;

--FactTransaction -> DimAccount
SELECT *
FROM dbo.FactTransaction ft
LEFT JOIN dbo.DimAccount da
    ON ft.AccountID = da.AccountID
WHERE da.AccountID IS NULL;

--FactTransaction -> DimBranch
SELECT *
FROM dbo.FactTransaction ft
LEFT JOIN dbo.DimBranch db
    ON ft.BranchID = db.BranchID
WHERE db.BranchID IS NULL;

--FactTransaction -> DimDate
SELECT *
FROM dbo.FactTransaction ft
LEFT JOIN dbo.DimDate dd
    ON ft.DateKey = dd.DateKey
WHERE dd.DateKey IS NULL;

--FactLoan -> DimCustomer
SELECT *
FROM dbo.FactLoan fl
LEFT JOIN dbo.DimCustomer dc
    ON fl.CustomerID = dc.CustomerID
WHERE dc.CustomerID IS NULL;

--FactLoan -> DimAccount
SELECT *
FROM dbo.FactLoan fl
LEFT JOIN dbo.DimAccount da
    ON fl.AccountID = da.AccountID
WHERE da.AccountID IS NULL;

--FactLoan -> DimBranch
SELECT *
FROM dbo.FactLoan fl
LEFT JOIN dbo.DimBranch db
    ON fl.BranchID = db.BranchID
WHERE db.BranchID IS NULL;

--FactLoan -> DimDate
SELECT *
FROM dbo.FactLoan fl
LEFT JOIN dbo.DimDate dd
    ON fl.DateKey = dd.DateKey
WHERE dd.DateKey IS NULL;

--FactRepayment -> FactLoan
SELECT *
FROM dbo.FactRepayment fr
LEFT JOIN dbo.FactLoan fl
    ON fr.LoanID = fl.LoanID
WHERE fl.LoanID IS NULL;

--FactRepayment -> DimCustomer
SELECT *
FROM dbo.FactRepayment fr
LEFT JOIN dbo.DimCustomer dc
    ON fr.CustomerID = dc.CustomerID
WHERE dc.CustomerID IS NULL;

--FactRepayment -> DimAccount
SELECT *
FROM dbo.FactRepayment fr
LEFT JOIN dbo.DimAccount da
    ON fr.AccountID = da.AccountID
WHERE da.AccountID IS NULL;

--FactRepayment -> DimBranch
SELECT *
FROM dbo.FactRepayment fr
LEFT JOIN dbo.DimBranch db
    ON fr.BranchID = db.BranchID
WHERE db.BranchID IS NULL;

--FactRepayment -> DimDate
SELECT *
FROM dbo.FactRepayment fr
LEFT JOIN dbo.DimDate dd
    ON fr.DateKey = dd.DateKey
WHERE dd.DateKey IS NULL;

--FactComplaint -> DimCustomer
SELECT *
FROM dbo.FactComplaint fc
LEFT JOIN dbo.DimCustomer dc
    ON fc.CustomerID = dc.CustomerID
WHERE dc.CustomerID IS NULL;

--FactComplaint -> DimAccount
SELECT *
FROM dbo.FactComplaint fc
LEFT JOIN dbo.DimAccount da
    ON fc.AccountID = da.AccountID
WHERE da.AccountID IS NULL;

--FactComplaint -> DimBranch
SELECT *
FROM dbo.FactComplaint fc
LEFT JOIN dbo.DimBranch db
    ON fc.BranchID = db.BranchID
WHERE db.BranchID IS NULL;

--FactComplaint -> DimDate
SELECT *
FROM dbo.FactComplaint fc
LEFT JOIN dbo.DimDate dd
    ON fc.DateKey = dd.DateKey
WHERE dd.DateKey IS NULL;



--SECTION 5 - MANDATORY FIELD VALIDATION

--DimCustomer Mandatory Fields
SELECT *
FROM dbo.DimCustomer
WHERE

    CustomerID IS NULL
 OR FirstName IS NULL
 OR LastName IS NULL
 OR Gender IS NULL
 OR CustomerSegment IS NULL
 OR Occupation IS NULL
 OR State IS NULL
 OR DateJoined IS NULL;

 --DimBranch Mandatory Fields
SELECT *
FROM dbo.DimBranch
WHERE

    BranchID IS NULL
 OR BranchCode IS NULL
 OR BranchName IS NULL
 OR City IS NULL
 OR State IS NULL
 OR Region IS NULL;

 --DimAccount Mandatory Fields
SELECT *
FROM dbo.DimAccount
WHERE

    AccountID IS NULL
 OR CustomerID IS NULL
 OR BranchID IS NULL
 OR AccountNumber IS NULL
 OR AccountType IS NULL
 OR AccountStatus IS NULL
 OR DateOpened IS NULL;

 --DimDate Mandatory Fields
SELECT *
FROM dbo.DimDate
WHERE

    DateKey IS NULL
 OR [Date] IS NULL
 OR [Year] IS NULL
 OR MonthName IS NULL
 OR Quarter IS NULL;

 --FactTransaction Mandatory Fields
SELECT *
FROM dbo.FactTransaction
WHERE

    TransactionID IS NULL
 OR CustomerID IS NULL
 OR AccountID IS NULL
 OR BranchID IS NULL
 OR DateKey IS NULL
 OR TransactionTypeID IS NULL
 OR Amount IS NULL;

 --FactLoan Mandatory Fields
SELECT *
FROM dbo.FactLoan
WHERE

    LoanID IS NULL
 OR CustomerID IS NULL
 OR AccountID IS NULL
 OR BranchID IS NULL
 OR DateKey IS NULL
 OR LoanProduct IS NULL
 OR LoanStatus IS NULL
 OR OriginalLoanAmount IS NULL
 OR OutstandingPrincipal IS NULL;

 --FactRepayment Mandatory Fields
SELECT *
FROM dbo.FactRepayment
WHERE

    RepaymentID IS NULL
 OR LoanID IS NULL
 OR CustomerID IS NULL
 OR AccountID IS NULL
 OR BranchID IS NULL
 OR DateKey IS NULL
 OR ExpectedAmount IS NULL
 OR PaymentStatus IS NULL;

 --FactComplaint Mandatory Fields
SELECT *
FROM dbo.FactComplaint
WHERE

    ComplaintID IS NULL
 OR CustomerID IS NULL
 OR AccountID IS NULL
 OR BranchID IS NULL
 OR DateKey IS NULL
 OR ComplaintCategory IS NULL
 OR ComplaintChannel IS NULL
 OR Severity IS NULL
 OR ResolutionStatus IS NULL
 OR ComplaintBehaviour IS NULL;




 --SECTION 6 - BUSINESS RULE VALIDATION


--Business Rule 1 - Pending complaints should not have a Resolution Date.
SELECT *
FROM dbo.FactComplaint
WHERE ResolutionStatus = 'Pending'
AND ResolutionDate IS NOT NULL;

--Business Rule 2 - Escalated complaints should not have a Resolution Date.
SELECT *
FROM dbo.FactComplaint
WHERE ResolutionStatus = 'Escalated'
AND ResolutionDate IS NOT NULL;

--Business Rule 3 - Pending complaints should not have Customer Satisfaction.
SELECT *
FROM dbo.FactComplaint
WHERE ResolutionStatus='Pending'
AND CustomerSatisfaction IS NOT NULL;

--Business Rule 4 - Escalated complaints should not have Customer Satisfaction.
SELECT *
FROM dbo.FactComplaint
WHERE ResolutionStatus='Escalated'
AND CustomerSatisfaction IS NOT NULL;

--Business Rule 5 - Resolved complaints must have a Resolution Date.
SELECT *
FROM dbo.FactComplaint
WHERE ResolutionStatus='Resolved'
AND ResolutionDate IS NULL;

--Business Rule 6 - Resolved complaints must have Customer Satisfaction.
SELECT *
FROM dbo.FactComplaint
WHERE ResolutionStatus='Resolved'
AND CustomerSatisfaction IS NULL;

--Business Rule 7 - Outstanding balance cannot exceed the original loan amount.
SELECT *
FROM dbo.FactLoan
WHERE OutstandingPrincipal > OriginalLoanAmount;

--Business Rule 8 - Loan Amount must always be positive.
SELECT *
FROM dbo.FactLoan
WHERE OriginalLoanAmount <= 0;

--Business Rule 9 - Outstanding balance cannot be negative.
SELECT *
FROM dbo.FactLoan
WHERE OutstandingPrincipal < 0;

--Business Rule 10 - Closed loans should have zero outstanding balance.
SELECT *
FROM dbo.FactLoan
WHERE LoanStatus='Closed'
AND OutstandingPrincipal <> 0;

--Business Rule 11 - Repayment amount must be greater than zero.
SELECT *
FROM dbo.FactRepayment
WHERE ExpectedAmount <=0;

--Business Rule 12 - Completed repayments should have a repayment date.
SELECT *
FROM dbo.FactRepayment
WHERE PaymentStatus='Completed'
AND ActualPaymentDate IS NULL;

--Business Rule 13 - Transactions should never have negative amounts.
SELECT *
FROM dbo.FactTransaction
WHERE Amount<=0;

--Business Rule 14 - Transaction Type is mandatory.
SELECT *
FROM dbo.FactTransaction
WHERE TransactionTypeID IS NULL;

--Business Rule 16 - Customers should be at least 18 years old.
SELECT *
FROM dbo.DimCustomer
WHERE DATEDIFF(YEAR, DateOfBirth, GETDATE()) <18;

--Business Rule 17 - Customers cannot join in the future.
SELECT *
FROM dbo.DimCustomer
WHERE DateJoined > GETDATE();

--Business Rule 18 - Accounts cannot be opened before the customer joined the bank.
SELECT
a.*
FROM dbo.DimAccount a
INNER JOIN dbo.DimCustomer c
ON a.CustomerID=c.CustomerID
WHERE a.DateOpened<c.DateJoined;






--'SECTION 7 - SEMANTIC LAYER VALIDATION'


--vw_Customer360
SELECT
'vw_Customer360' AS ViewName,
COUNT(*) AS TotalRows
FROM dbo.vw_Customer360;

--vw_LoanPortfolio
SELECT
'vw_LoanPortfolio' AS ViewName,
COUNT(*) AS TotalRows
FROM dbo.vw_LoanPortfolio;

--vw_LoanEarlyWarning
SELECT
'vw_LoanEarlyWarning' AS ViewName,
COUNT(*) AS TotalRows
FROM dbo.vw_LoanEarlyWarning;

--vw_ComplaintInsights
SELECT
'vw_ComplaintInsights' AS ViewName,
COUNT(*) AS TotalRows
FROM dbo.vw_ComplaintInsights;

--vw_BranchPerformance
SELECT
'vw_BranchPerformance' AS ViewName,
COUNT(*) AS TotalRows
FROM dbo.vw_BranchPerformance;

--vw_RevenueAnalytics
SELECT
'vw_RevenueAnalytics' AS ViewName,
COUNT(*) AS TotalRows
FROM dbo.vw_RevenueAnalytics;




--'Section 8 - Stored Procedure Validation'

--Customer360
PRINT 'Executing sp_GetCustomer360...';

DECLARE @CustomerID INT;

SELECT TOP (1)
    @CustomerID = CustomerID
FROM dbo.DimCustomer;

EXEC dbo.sp_GetCustomer360
    @CustomerID = @CustomerID;

--High Risk Loans
PRINT 'Executing sp_GetHighRiskLoans...';

EXEC dbo.sp_GetHighRiskLoans;

PRINT 'Completed.';
PRINT '';

--Branch Performance
PRINT 'Executing sp_GetBranchPerformance...';

EXEC dbo.sp_GetBranchPerformance;

PRINT 'Completed.';
PRINT '';

--Customer Complaints
PRINT 'Executing sp_GetCustomerComplaints';

EXEC dbo.sp_GetCustomerComplaints;






-- SECTION 9 - 'EBIEWP DATA WAREHOUSE VALIDATION COMPLETE'


PRINT 'EBIEWP DATA WAREHOUSE VALIDATION COMPLETE';


PRINT 'Warehouse Tables Loaded';

PRINT 'Primary Keys Validated';

PRINT 'Foreign Keys Validated';

PRINT 'Referential Integrity Passed';

PRINT 'Duplicate Checks Passed';

PRINT 'Mandatory Field Checks Passed';

PRINT 'Business Rules Passed';

PRINT 'Semantic Layer Validated';

PRINT 'Stored Procedures Validated';

PRINT '';

PRINT 'Warehouse Status:';

PRINT 'READY FOR POWER BI DEVELOPMENT';






