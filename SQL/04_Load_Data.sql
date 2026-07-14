/*
Enterprise Banking Intelligence & Early Warning Platform
Module 04 - Load Staging Tables

Description:

Loads raw CSV datasets into the staging layer.
*/

USE EBIEWP;
GO

TRUNCATE TABLE stg.DimDate;
GO

BULK INSERT stg.DimDate

FROM 'C:\Users\user\Documents\Documents\Projects\Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)\Data\Dimensions\DimDate.csv'

WITH
(

    FORMAT = 'CSV',

    FIRSTROW = 2,

    FIELDTERMINATOR = ',',

    ROWTERMINATOR = '\n',

    TABLOCK

);

GO

SELECT TOP 5 *
FROM stg.DimDate;

-----------------------------------------------------------------------------------

TRUNCATE TABLE stg.DimBranch;
GO

BULK INSERT stg.DimBranch
FROM 'C:\Users\user\Documents\Documents\Projects\Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)\Data\Dimensions\DimBranch.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
);

GO

SELECT COUNT(*) AS StagingRows
FROM stg.DimBranch;
GO

------------------------------------------------------------------------

TRUNCATE TABLE stg.DimCustomer;
GO

BULK INSERT stg.DimCustomer

FROM 'C:\Users\user\Documents\Documents\Projects\Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)\Data\Dimensions\DimCustomer.csv'

WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
);

GO

SELECT COUNT(*) AS StagingRows
FROM stg.DimCustomer;

GO

------------------------------------------------------------------------------

TRUNCATE TABLE stg.DimAccount;
GO

BULK INSERT stg.DimAccount

FROM 'C:\Users\user\Documents\Documents\Projects\Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)\Data\Dimensions\DimAccount.csv'

WITH
(
    FORMAT='CSV',
    FIRSTROW=2,
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

GO

SELECT COUNT(*) AS StagingRows

FROM stg.DimAccount;

GO

------------------------------------------------------------------------

TRUNCATE TABLE stg.DimTransactionType;
GO

BULK INSERT stg.DimTransactionType

FROM 'C:\Users\user\Documents\Documents\Projects\Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)\Data\Dimensions\DimTransactionType.csv'

WITH
(
    FORMAT='CSV',
    FIRSTROW=2,
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

GO

SELECT COUNT(*) AS StagingRows

FROM stg.DimTransactionType;

GO

-------------------------------------------------------

TRUNCATE TABLE stg.FactTransaction;
GO

BULK INSERT stg.FactTransaction

FROM 'C:\Users\user\Documents\Documents\Projects\Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)\Data\Facts\FactTransaction.csv'

WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
);

GO

SELECT COUNT(*) AS StagingRows
FROM stg.FactTransaction;

GO

----------------------------------------------------------------------------

TRUNCATE TABLE stg.FactLoan;
GO

BULK INSERT stg.FactLoan

FROM 'C:\Users\user\Documents\Documents\Projects\Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)\Data\Facts\FactLoan.csv'

WITH
(
    FORMAT='CSV',
    FIRSTROW=2,
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

GO

SELECT COUNT(*) AS StagingRows

FROM stg.FactLoan;

GO

----------------------------------------------------------------

TRUNCATE TABLE stg.FactRepayment;
GO

BULK INSERT stg.FactRepayment

FROM 'C:\Users\user\Documents\Documents\Projects\Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)\Data\Facts\FactRepayment.csv'

WITH
(
    FORMAT='CSV',
    FIRSTROW=2,
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

GO

SELECT COUNT(*) AS StagingRows

FROM stg.FactRepayment;

GO

----------------------------------------------------------------------------

TRUNCATE TABLE stg.FactComplaint;
GO

BULK INSERT stg.FactComplaint

FROM 'C:\Users\user\Documents\Documents\Projects\Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)\Data\Facts\FactComplaint.csv'

WITH
(
    FORMAT='CSV',
    FIRSTROW=2,
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK
);

GO

SELECT COUNT(*) AS StagingRows

FROM stg.FactComplaint;

GO

----------------------------------------------------------------------




