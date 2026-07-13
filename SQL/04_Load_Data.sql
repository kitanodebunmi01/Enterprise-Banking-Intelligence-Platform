/*
Enterprise Banking Intelligence & Early Warning Platform
Module 04 - Load Staging Tables

Description:

Loads raw CSV datasets into the staging layer.
*/

USE EBIEWP;
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