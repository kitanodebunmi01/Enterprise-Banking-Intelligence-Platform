USE EBIEWP;
GO

/*
Stored Procedure: Customer360 Lookup
Name: sp_GetCustomer360
Purpose:
Returns a complete 360-degree customer profile for a
specified customer.
*/

CREATE PROCEDURE dbo.sp_GetCustomer360

    @CustomerID INT

AS

BEGIN

    SET NOCOUNT ON;

    SELECT *

    FROM dbo.vw_Customer360

    WHERE CustomerID = @CustomerID;

END;
GO

-- Testing

EXEC dbo.sp_GetCustomer360

@CustomerID = 100000055;

EXEC dbo.sp_GetCustomer360

@CustomerID = 100098768;

----------------------------------------------------------------------------------------------

USE EBIEWP;
GO

/*
Stored Procedure: Get High Risk Loans
Name: sp_GetHighRiskLoans

Purpose:
Returns loans based on the selected Risk Level with
optional filtering by Branch, Region and Loan Product.

Default Risk Level = High
*/

CREATE PROCEDURE dbo.sp_GetHighRiskLoans

    @RiskLevel NVARCHAR(20) = 'High',

    @BranchName NVARCHAR(100) = NULL,

    @Region NVARCHAR(100) = NULL,

    @LoanProduct NVARCHAR(100) = NULL

AS

BEGIN

    SET NOCOUNT ON;

    SELECT

        LoanID,

        CustomerID,

        FirstName,

        LastName,

        CustomerSegment,

        BranchName,

        Region,

        LoanProduct,

        Currency,

        LoanStatus,

        DaysPastDue,

        ConsecutiveMissedPayments,

        PaymentBehaviour,

        OutstandingPrincipal,

        RiskLevel,

        EarlyWarningFlag,

        RecommendedAction

    FROM dbo.vw_LoanEarlyWarning

    WHERE

        RiskLevel = @RiskLevel

        AND (@BranchName IS NULL OR BranchName LIKE '%' + @BranchName + '%')

        AND (@Region IS NULL OR Region LIKE '%' + @Region + '%')

        AND (@LoanProduct IS NULL OR LoanProduct LIKE '%' + @LoanProduct + '%')

    ORDER BY

        DaysPastDue DESC,

        OutstandingPrincipal DESC,

        CustomerID;

END;
GO

-- Testing

EXEC dbo.sp_GetHighRiskLoans;

EXEC dbo.sp_GetHighRiskLoans
    @RiskLevel = 'Medium';

EXEC dbo.sp_GetHighRiskLoans
    @Region = 'South West';

EXEC dbo.sp_GetHighRiskLoans
    @LoanProduct = 'Mortgage';

EXEC dbo.sp_GetHighRiskLoans
    @BranchName = 'Victoria Island';

EXEC dbo.sp_GetHighRiskLoans
    @RiskLevel = 'Medium',
    @BranchName = 'Victoria Island',
    @LoanProduct = 'Mortgage';

---------------------------------------------------------------------------------------------

USE EBIEWP;
GO

/*
Stored Procedure: Get Branch Performance
Name: sp_GetBranchPerformance

Purpose:
Returns branch transaction performance with optional
filters for Branch, Region, Year, Quarter and Month.
*/

CREATE PROCEDURE dbo.sp_GetBranchPerformance

    @BranchName NVARCHAR(100) = NULL,
    @Region NVARCHAR(100) = NULL,
    @Year INT = NULL,
    @Quarter NVARCHAR(10) = NULL,
    @Month NVARCHAR(20) = NULL

AS

BEGIN

    SET NOCOUNT ON;

    SELECT

        BranchID,
        BranchCode,
        BranchName,
        City,
        State,
        Region,

        Year,
        Quarter,
        MonthNumber,
        MonthName,

        TotalTransactions,
        TotalTransactionValue,
        AverageTransactionValue,
        ActiveCustomers

    FROM dbo.vw_BranchPerformance

    WHERE

        (@BranchName IS NULL OR BranchName LIKE '%' + @BranchName + '%')

        AND (@Region IS NULL OR Region LIKE '%' + @Region + '%')

        AND (@Year IS NULL OR Year = @Year)

        AND (@Quarter IS NULL OR Quarter = @Quarter)

        AND (@Month IS NULL OR MonthName LIKE '%' + @Month + '%')

    ORDER BY

        Year DESC,
        MonthNumber DESC,
        TotalTransactionValue DESC,
        BranchName;

END;
GO

-- Testing

EXEC dbo.sp_GetBranchPerformance
    @Month = 'June';

-----------------------------------------------------------------------------------------

USE EBIEWP;
GO

/*
Stored Procedure: Get Customer Complaints
Name: sp_GetCustomerComplaints

Purpose:
Returns customer complaint records with optional filters
for Branch, Complaint Category, Complaint Channel,
Severity, Resolution Status, SLA Compliance and Time.
*/

CREATE PROCEDURE dbo.sp_GetCustomerComplaints

    @BranchName NVARCHAR(100) = NULL,
    @ComplaintCategory NVARCHAR(100) = NULL,
    @ComplaintChannel NVARCHAR(100) = NULL,
    @Severity NVARCHAR(20) = NULL,
    @ResolutionStatus NVARCHAR(20) = NULL,
    @MetSLA BIT = NULL,
    @Year INT = NULL,
    @Month NVARCHAR(20) = NULL

AS

BEGIN

    SET NOCOUNT ON;

    SELECT

        fc.ComplaintID,

        fc.CustomerID,

        c.FirstName,

        c.LastName,

        c.CustomerSegment,

        fc.AccountID,

        b.BranchCode,

        b.BranchName,

        b.Region,

        fc.ComplaintDate,

        d.Year,

        d.Quarter,

        d.MonthName,

        fc.ComplaintCategory,

        fc.ComplaintChannel,

        fc.Severity,

        fc.ResolutionStatus,

        fc.ResolutionDays,

        fc.MetSLA,

        fc.ResolutionDate,

        fc.CustomerSatisfaction,

        fc.ComplaintBehaviour,

        fc.RepeatComplaintCount

    FROM dbo.FactComplaint fc

        INNER JOIN dbo.DimCustomer c
            ON fc.CustomerID = c.CustomerID

        INNER JOIN dbo.DimBranch b
            ON fc.BranchID = b.BranchID

        INNER JOIN dbo.DimDate d
            ON fc.DateKey = d.DateKey

    WHERE

        (@BranchName IS NULL
            OR b.BranchName LIKE '%' + @BranchName + '%')

        AND (@ComplaintCategory IS NULL
            OR fc.ComplaintCategory LIKE '%' + @ComplaintCategory + '%')

        AND (@ComplaintChannel IS NULL
            OR fc.ComplaintChannel LIKE '%' + @ComplaintChannel + '%')

        AND (@Severity IS NULL
            OR fc.Severity = @Severity)

        AND (@ResolutionStatus IS NULL
            OR fc.ResolutionStatus = @ResolutionStatus)

        AND (@MetSLA IS NULL
            OR fc.MetSLA = @MetSLA)

        AND (@Year IS NULL
            OR d.Year = @Year)

        AND (@Month IS NULL
            OR d.MonthName LIKE '%' + @Month + '%')

    ORDER BY

        fc.ComplaintDate DESC,
        fc.Severity DESC,
        fc.ResolutionDays DESC;

END;
GO

-- Testing

EXEC dbo.sp_GetCustomerComplaints;

EXEC dbo.sp_GetCustomerComplaints
    @Severity = 'High';

EXEC dbo.sp_GetCustomerComplaints
    @ComplaintChannel = 'Mobile App';

