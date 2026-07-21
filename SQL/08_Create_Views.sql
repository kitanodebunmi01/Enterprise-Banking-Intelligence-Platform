USE EBIEWP;
GO


-- View: Branch Performance


CREATE VIEW dbo.vw_BranchPerformance
AS

SELECT

    b.BranchID,
    b.BranchCode,
    b.BranchName,
    b.City,
    b.State,
    b.Region,

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    COUNT(ft.FactTransactionKey) AS TotalTransactions,

    SUM(ft.Amount) AS TotalTransactionValue,

    AVG(ft.Amount) AS AverageTransactionValue,

    COUNT(DISTINCT ft.CustomerID) AS ActiveCustomers

FROM dbo.FactTransaction ft

INNER JOIN dbo.DimBranch b
ON ft.BranchID = b.BranchID

INNER JOIN dbo.DimDate d
ON ft.DateKey = d.DateKey

GROUP BY

    b.BranchID,
    b.BranchCode,
    b.BranchName,
    b.City,
    b.State,
    b.Region,

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName;

GO

SELECT TOP (20) *
FROM dbo.vw_BranchPerformance;

-----------------------------------------------------------------------------------------------


-- View: Channel Performance


CREATE VIEW dbo.vw_ChannelPerformance
AS

SELECT

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    tt.Channel,
    tt.TransactionCategory,
    tt.TransactionType,

    COUNT(ft.FactTransactionKey) AS TotalTransactions,

    SUM(ft.Amount) AS TotalTransactionValue,

    AVG(ft.Amount) AS AverageTransactionValue,

    COUNT(DISTINCT ft.CustomerID) AS ActiveCustomers

FROM dbo.FactTransaction ft

INNER JOIN dbo.DimTransactionType tt
ON ft.TransactionTypeID = tt.TransactionTypeID

INNER JOIN dbo.DimDate d
ON ft.DateKey = d.DateKey

GROUP BY

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    tt.Channel,
    tt.TransactionCategory,
    tt.TransactionType;

GO

SELECT TOP (20) *
FROM dbo.vw_ChannelPerformance;

------------------------------------------------------------------------------------------

USE EBIEWP;
GO


/*
View: Complaint Insights
Purpose:
Provides complaint intelligence, customer experience KPIs,
and service quality metrics for executive reporting.
*/

CREATE VIEW dbo.vw_ComplaintInsights
AS

SELECT

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    b.BranchID,
    b.BranchName,
    b.Region,

    COUNT(fc.ComplaintID) AS TotalComplaints,

    CAST(
        AVG(CAST(fc.ResolutionDays AS DECIMAL(10,2)))
        AS DECIMAL(10,2)
    ) AS AverageResolutionDays,

    CAST(

        100.0 *
        SUM(CASE WHEN fc.MetSLA = 1 THEN 1 ELSE 0 END)
        / COUNT(*)

    AS DECIMAL(5,2))

    AS SLACompliancePercent,

    SUM(CASE WHEN fc.CustomerSatisfaction = 'Satisfied' THEN 1 ELSE 0 END)
    AS SatisfiedCustomers,

    SUM(CASE WHEN fc.CustomerSatisfaction = 'Neutral' THEN 1 ELSE 0 END)
    AS NeutralCustomers,

    SUM(CASE WHEN fc.CustomerSatisfaction = 'Unsatisfied' THEN 1 ELSE 0 END)
    AS UnsatisfiedCustomers,

    CAST(

        100.0 *
        SUM(CASE WHEN fc.CustomerSatisfaction='Satisfied' THEN 1 ELSE 0 END)
        / COUNT(*)

    AS DECIMAL(5,2))

    AS SatisfactionRate,

    CAST(

        100.0 *
        SUM(CASE WHEN fc.CustomerSatisfaction='Neutral' THEN 1 ELSE 0 END)
        / COUNT(*)

    AS DECIMAL(5,2))

    AS NeutralRate,

    CAST(

        100.0 *
        SUM(CASE WHEN fc.CustomerSatisfaction='Unsatisfied' THEN 1 ELSE 0 END)
        / COUNT(*)

    AS DECIMAL(5,2))

    AS UnsatisfactionRate,

    SUM(fc.RepeatComplaintCount)
    AS TotalRepeatComplaints,

    CAST(

        100.0 *
        SUM(CASE WHEN fc.RepeatComplaintCount > 0 THEN 1 ELSE 0 END)
        / COUNT(*)

    AS DECIMAL(5,2))

    AS RepeatComplaintRate

FROM dbo.FactComplaint fc

INNER JOIN dbo.DimBranch b

    ON fc.BranchID = b.BranchID

INNER JOIN dbo.DimDate d

    ON fc.DateKey = d.DateKey

GROUP BY

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    b.BranchID,
    b.BranchName,
    b.Region;

GO

SELECT TOP (20) *
FROM dbo.vw_ComplaintInsights;

-------------------------------------------------------------------------------------


-- View: Complaint Category Analysis


CREATE VIEW dbo.vw_ComplaintCategoryAnalysis
AS

SELECT

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    fc.ComplaintCategory,

    COUNT(fc.ComplaintID) AS TotalComplaints,

    CAST(

        AVG(CAST(fc.ResolutionDays AS DECIMAL(10,2)))

    AS DECIMAL(10,2))

    AS AverageResolutionDays,

    CAST(

        100.0 *
        SUM(CASE WHEN fc.MetSLA = 1 THEN 1 ELSE 0 END)
        / COUNT(*)

    AS DECIMAL(5,2))

    AS SLACompliancePercent,

    CAST(

        100.0 *
        SUM(CASE WHEN fc.CustomerSatisfaction='Satisfied' THEN 1 ELSE 0 END)
        / COUNT(*)

    AS DECIMAL(5,2))

    AS SatisfactionRate,

    CAST(

        100.0 *
        SUM(CASE WHEN fc.CustomerSatisfaction='Unsatisfied' THEN 1 ELSE 0 END)
        / COUNT(*)

    AS DECIMAL(5,2))

    AS UnsatisfactionRate

FROM dbo.FactComplaint fc

INNER JOIN dbo.DimDate d

    ON fc.DateKey = d.DateKey

GROUP BY

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    fc.ComplaintCategory;

GO

SELECT TOP (20) *
FROM dbo.vw_ComplaintCategoryAnalysis;

----------------------------------------------------------------------------------------------


-- View: Complaint Channel Analysis


CREATE VIEW dbo.vw_ComplaintChannelAnalysis
AS

SELECT

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    fc.ComplaintChannel,

    COUNT(fc.ComplaintID) AS TotalComplaints,

    CAST(

        AVG(CAST(fc.ResolutionDays AS DECIMAL(10,2)))

    AS DECIMAL(10,2))

    AS AverageResolutionDays,

    CAST(

        100.0 *
        SUM(CASE WHEN fc.MetSLA = 1 THEN 1 ELSE 0 END)
        / COUNT(*)

    AS DECIMAL(5,2))

    AS SLACompliancePercent,

    CAST(

        100.0 *
        SUM(CASE WHEN fc.CustomerSatisfaction='Satisfied' THEN 1 ELSE 0 END)
        / COUNT(*)

    AS DECIMAL(5,2))

    AS SatisfactionRate,

    CAST(

        100.0 *
        SUM(CASE WHEN fc.CustomerSatisfaction='Unsatisfied' THEN 1 ELSE 0 END)
        / COUNT(*)

    AS DECIMAL(5,2))

    AS UnsatisfactionRate

FROM dbo.FactComplaint fc

INNER JOIN dbo.DimDate d

    ON fc.DateKey = d.DateKey

GROUP BY

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    fc.ComplaintChannel;

GO

SELECT TOP (20) *
FROM dbo.vw_ComplaintChannelAnalysis;

------------------------------------------------------------------------------------

/*
View: Loan Portfolio
Purpose:
Provides portfolio-level loan analytics for credit
management and executive reporting.
*/

CREATE VIEW dbo.vw_LoanPortfolio
AS

SELECT

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    b.BranchID,
    b.BranchName,
    b.Region,

    c.CustomerSegment,

    fl.LoanProduct,
    fl.Currency,
    fl.LoanStatus,


    COUNT(fl.LoanID) AS TotalLoans,

    SUM(fl.OriginalLoanAmount) AS TotalOriginalLoanAmount,

    SUM(fl.OutstandingPrincipal) AS TotalOutstandingPrincipal,

    CAST(

        AVG(fl.OriginalLoanAmount)

    AS DECIMAL(18,2))

    AS AverageLoanAmount,

    CAST(

        AVG(fl.MonthlyInstallment)

    AS DECIMAL(18,2))

    AS AverageMonthlyInstallment,

    CAST(

        AVG(fl.InterestRate)

    AS DECIMAL(5,2))

    AS AverageInterestRate

FROM dbo.FactLoan fl

INNER JOIN dbo.DimCustomer c

    ON fl.CustomerID = c.CustomerID

INNER JOIN dbo.DimBranch b

    ON fl.BranchID = b.BranchID

INNER JOIN dbo.DimDate d

    ON fl.DateKey = d.DateKey

GROUP BY

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    b.BranchID,
    b.BranchName,
    b.Region,

    c.CustomerSegment,

    fl.LoanProduct,

    fl.Currency,

    fl.LoanStatus;

GO

SELECT TOP (20) *
FROM dbo.vw_LoanPortfolio;

-------------------------------------------------------------------------------------------------

/*
View: Loan Early Warning
Purpose:
Identifies loans showing early warning signs of potential
default and recommends operational actions.
*/

CREATE VIEW dbo.vw_LoanEarlyWarning
AS

SELECT

    fr.LoanID,

    fl.LoanProduct,

    fl.Currency,

    fl.LoanStatus,

    dc.CustomerID,

    dc.FirstName,

    dc.LastName,

    dc.CustomerSegment,

    db.BranchName,

    db.Region,

    dd.Year,

    dd.MonthName,

    
    -- Risk Indicators
   
    fr.DaysPastDue,

    fr.ConsecutiveMissedPayments,

    fr.PaymentBehaviour,

    fr.OutstandingPrincipal,

    
    -- Risk Classification
    

    CASE

        WHEN
        (

            fr.DaysPastDue >= 60

            OR

            fr.ConsecutiveMissedPayments >= 3

            OR

            fr.PaymentBehaviour='High Risk'
        )

        AND fl.LoanStatus='Active'

        THEN 'High'

        WHEN
        (
            fr.DaysPastDue BETWEEN 30 AND 60

            OR

            fr.ConsecutiveMissedPayments BETWEEN 1 AND 2

            OR

            fr.PaymentBehaviour='Average Payer'
        )
        AND fl.LoanStatus='Active'

        THEN 'Medium'

        ELSE 'Low'

    END

    AS RiskLevel,

    
    -- Early Warning Flag
    

    CASE

        WHEN
        (
            fr.DaysPastDue >=30

            OR

            fr.ConsecutiveMissedPayments >=1

            OR

            fr.PaymentBehaviour IN ('Average Payer', 'High Risk')
        )
        AND fl.LoanStatus='Active'

        THEN 'Yes'

        ELSE 'No'

    END

    AS EarlyWarningFlag,

    
    -- Recommended Action
    

    CASE

        WHEN

            (fr.DaysPastDue >=60)

            AND

            fl.LoanStatus='Active'

        THEN 'Collections / Recovery'

        WHEN
        (
            fr.DaysPastDue BETWEEN 30 AND 60

            OR

            fr.ConsecutiveMissedPayments>=1
        )
        AND fl.LoanStatus='Active'

        THEN 'Relationship Manager Follow-up'

        ELSE 'Continue Monitoring'

    END

    AS RecommendedAction

FROM dbo.FactRepayment fr

INNER JOIN dbo.FactLoan fl

    ON fr.LoanID = fl.LoanID

INNER JOIN dbo.DimCustomer dc

    ON fr.CustomerID = dc.CustomerID

INNER JOIN dbo.DimBranch db

    ON fr.BranchID = db.BranchID

INNER JOIN dbo.DimDate dd

    ON fr.DateKey = dd.DateKey;

GO

SELECT TOP (20) *
FROM dbo.vw_LoanEarlyWarning;

--------------------------------------------------------------------------------------------------------

CREATE VIEW dbo.vw_Customer360
AS

WITH
AccountSummary AS
(

SELECT

    CustomerID,

    COUNT(AccountID) AS TotalAccounts,

    SUM(CurrentBalance) AS TotalCurrentBalance

FROM dbo.DimAccount

GROUP BY CustomerID

),

TransactionSummary AS
(

SELECT

    CustomerID,

    COUNT(FactTransactionKey) AS TotalTransactions,

    SUM(Amount) AS TotalTransactionValue,

    AVG(Amount) AS AverageTransactionValue,

    MAX(
        DATEFROMPARTS
        (
            DateKey / 10000,
            (DateKey % 10000) / 100,
            DateKey % 100
        )
    ) AS LastTransactionDate

FROM dbo.FactTransaction

GROUP BY CustomerID

),

LoanSummary AS
(

SELECT

    CustomerID,

    COUNT(LoanID) AS TotalLoans,

    SUM(OriginalLoanAmount) AS TotalOriginalLoanAmount,

    SUM(OutstandingPrincipal) AS TotalOutstandingPrincipal,

    AVG(InterestRate) AS AverageInterestRate,

    AVG(MonthlyInstallment) AS AverageMonthlyInstallment

FROM dbo.FactLoan

GROUP BY CustomerID

),

LatestRepayment AS
(

SELECT

    CustomerID,

    LoanID,

    PaymentBehaviour,

    DaysPastDue,

    ConsecutiveMissedPayments,

    OutstandingPrincipal,

    ActualPaymentDate,

    ROW_NUMBER() OVER
    (

        PARTITION BY CustomerID

        ORDER BY ActualPaymentDate DESC

    ) AS rn

FROM dbo.FactRepayment

),

RepaymentSummary AS
(

SELECT

    CustomerID,

    LoanID,

    PaymentBehaviour,

    DaysPastDue,

    ConsecutiveMissedPayments,

    ActualPaymentDate

FROM LatestRepayment

WHERE rn = 1

),

ComplaintSummary AS
(

SELECT

    CustomerID,

    COUNT(ComplaintID) AS TotalComplaints,

    SUM(RepeatComplaintCount) AS RepeatComplaints,

    SUM(CASE WHEN MetSLA = 1 THEN 1 ELSE 0 END) AS ComplaintsResolvedWithinSLA,

    SUM(CASE WHEN CustomerSatisfaction = 'Satisfied' THEN 1 ELSE 0 END) AS SatisfiedComplaints,

    SUM(CASE WHEN CustomerSatisfaction = 'Unsatisfied' THEN 1 ELSE 0 END) AS UnsatisfiedComplaints,

    MAX(ComplaintDate) AS LastComplaintDate

FROM dbo.FactComplaint

GROUP BY CustomerID

)

SELECT

    
    -- Customer Profile
    

    dc.CustomerID,
    dc.FirstName,
    dc.LastName,
    dc.Gender,
    dc.Age,
    dc.CustomerSegment,
    dc.Occupation,
    dc.AnnualIncome,
    dc.State,
    dc.City,
    dc.DateJoined,

    
    -- Banking Relationship
    

    ISNULL(acc.TotalAccounts,0) AS TotalAccounts,

    ISNULL(acc.TotalCurrentBalance,0) AS TotalCurrentBalance,

    
    -- Transaction Behaviour
    

    ISNULL(trx.TotalTransactions,0) AS TotalTransactions,

    ISNULL(trx.TotalTransactionValue,0) AS TotalTransactionValue,

    CAST(

        ISNULL(trx.AverageTransactionValue,0)

    AS DECIMAL(18,2))

    AS AverageTransactionValue,

    trx.LastTransactionDate,

    CASE

        WHEN
            ISNULL(repay.ActualPaymentDate,'19000101') >= ISNULL(trx.LastTransactionDate,'19000101')
            AND
            ISNULL(repay.ActualPaymentDate,'19000101') >= ISNULL(comp.LastComplaintDate,'19000101')
        THEN repay.ActualPaymentDate

        WHEN
            ISNULL(comp.LastComplaintDate,'19000101') >= ISNULL(trx.LastTransactionDate,'19000101')
        THEN comp.LastComplaintDate

        ELSE trx.LastTransactionDate

    END
    AS LastCustomerActivityDate,

    CASE

        WHEN
            ISNULL(repay.ActualPaymentDate,'19000101') >= ISNULL(trx.LastTransactionDate,'19000101')
            AND
            ISNULL(repay.ActualPaymentDate,'19000101') >= ISNULL(comp.LastComplaintDate,'19000101')

        THEN 'Loan Repayment'

        WHEN
            ISNULL(comp.LastComplaintDate,'19000101') >= ISNULL(trx.LastTransactionDate,'19000101')

        THEN 'Customer Complaint'

        ELSE 'Financial Transaction'

    END
    AS LastActivitySource,

    
    -- Loan Portfolio
    

    ISNULL(loan.TotalLoans,0) AS TotalLoans,

    ISNULL(loan.TotalOriginalLoanAmount,0) AS TotalOriginalLoanAmount,

    ISNULL(loan.TotalOutstandingPrincipal,0) AS TotalOutstandingPrincipal,

    CAST(

        ISNULL(loan.AverageInterestRate,0)

    AS DECIMAL(5,2))

    AS AverageInterestRate,

    CAST(

        ISNULL(loan.AverageMonthlyInstallment,0)

    AS DECIMAL(18,2))

    AS AverageMonthlyInstallment,

    
    -- Latest Repayment Behaviour
    

    repay.PaymentBehaviour,

    repay.DaysPastDue,

    repay.ConsecutiveMissedPayments,

    
    -- Complaint Behaviour
    

    ISNULL(comp.TotalComplaints,0) AS TotalComplaints,

    ISNULL(comp.RepeatComplaints,0) AS RepeatComplaints,

    ISNULL(comp.ComplaintsResolvedWithinSLA,0)
    AS ComplaintsResolvedWithinSLA,

    ISNULL(comp.SatisfiedComplaints,0)
    AS SatisfiedComplaints,

    ISNULL(comp.UnsatisfiedComplaints,0)
    AS UnsatisfiedComplaints,

    
    -- Derived Customer KPIs
    

    CASE

        WHEN
            ISNULL(acc.TotalCurrentBalance,0) >= 100000000
            OR
            ISNULL(trx.TotalTransactionValue,0) >= 500000000
        THEN 'Platinum'

        WHEN
            ISNULL(acc.TotalCurrentBalance,0) >= 50000000
            OR
            ISNULL(trx.TotalTransactionValue,0) >= 200000000
        THEN 'Gold'

        WHEN
            ISNULL(acc.TotalCurrentBalance,0) >= 10000000
        THEN 'Silver'

        ELSE 'Standard'

    END AS CustomerValueTier,

    CASE

        WHEN ISNULL(trx.TotalTransactions,0) >= 1000
        THEN 'High'

        WHEN ISNULL(trx.TotalTransactions,0) >= 300
        THEN 'Medium'

        ELSE 'Low'

    END AS CustomerEngagementLevel,

    CASE

        WHEN

            ISNULL(repay.DaysPastDue,0) >= 90

            OR

            ISNULL(comp.UnsatisfiedComplaints,0) >= 2

        THEN 'At Risk'

        WHEN

            ISNULL(repay.DaysPastDue,0) >= 30

            OR

            ISNULL(comp.RepeatComplaints,0) >= 1

        THEN 'Watchlist'

        ELSE 'Healthy'

    END AS CustomerHealth

FROM dbo.DimCustomer dc

LEFT JOIN AccountSummary acc

    ON dc.CustomerID = acc.CustomerID

LEFT JOIN TransactionSummary trx

    ON dc.CustomerID = trx.CustomerID

LEFT JOIN LoanSummary loan

    ON dc.CustomerID = loan.CustomerID

LEFT JOIN RepaymentSummary repay

    ON dc.CustomerID = repay.CustomerID

LEFT JOIN ComplaintSummary comp

    ON dc.CustomerID = comp.CustomerID;


SELECT TOP (20) *
FROM dbo.vw_Customer360;

SELECT COUNT(*)
FROM dbo.vw_Customer360;

SELECT
    CustomerID,
    COUNT(*)
FROM dbo.vw_Customer360
GROUP BY CustomerID
HAVING COUNT(*) > 1;

-----------------------------------------------------------------------------------------------------

/*
View: Revenue Analytics
Purpose:
Provides executive-level transaction and customer activity
analytics across time, branch, customer segment and channel.
*/

CREATE VIEW dbo.vw_RevenueAnalytics
AS

SELECT

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    b.BranchID,
    b.BranchName,
    b.Region,

    c.CustomerSegment,

    tt.Channel,


    COUNT(ft.FactTransactionKey) AS TotalTransactions,

    SUM(ft.Amount) AS TotalTransactionValue,

    CAST(
        AVG(ft.Amount)
    AS DECIMAL(18,2))
    AS AverageTransactionValue,

    COUNT(DISTINCT ft.CustomerID) AS ActiveCustomers,

    CAST(
        SUM(ft.Amount)
        /
        NULLIF(COUNT(DISTINCT ft.CustomerID),0)
    AS DECIMAL(18,2))
    AS AverageTransactionValuePerCustomer

FROM dbo.FactTransaction ft

INNER JOIN dbo.DimBranch b
    ON ft.BranchID = b.BranchID

INNER JOIN dbo.DimCustomer c
    ON ft.CustomerID = c.CustomerID

INNER JOIN dbo.DimTransactionType tt
    ON ft.TransactionTypeID = tt.TransactionTypeID

INNER JOIN dbo.DimDate d
    ON ft.DateKey = d.DateKey

GROUP BY

    d.Year,
    d.Quarter,
    d.MonthNumber,
    d.MonthName,

    b.BranchID,
    b.BranchName,
    b.Region,

    c.CustomerSegment,

    tt.Channel;

GO

SELECT TOP (20) *
FROM dbo.vw_RevenueAnalytics;

SELECT COUNT(*)
FROM dbo.vw_RevenueAnalytics;
