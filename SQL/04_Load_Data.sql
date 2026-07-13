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



