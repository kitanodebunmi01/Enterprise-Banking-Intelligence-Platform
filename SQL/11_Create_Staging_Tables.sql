/*
Enterprise Banking Intelligence & Early Warning Platform
Module 11 - Create Staging Tables

Description:

Creates the staging tables used for loading raw
CSV datasets before transformation into the
enterprise data warehouse.
*/

USE EBIEWP;
GO

CREATE TABLE stg.DimDate
(

    DateKey INT,

    [Date] DATE,

    [Year] SMALLINT,

    Quarter TINYINT,

    QuarterName VARCHAR(2),

    MonthNumber TINYINT,

    MonthName VARCHAR(10),

    MonthYear VARCHAR(10),

    YearMonthKey INT,

    WeekNumber TINYINT,

    [Day] TINYINT,

    DayName VARCHAR(10),

    FinancialYear SMALLINT,

    DaysInMonth TINYINT,

    MonthEndDate DATE,

    IsWeekend VARCHAR(5),

    IsMonthStart VARCHAR(5),

    IsMonthEnd VARCHAR(5),

    IsLeapYear VARCHAR(5)

);

GO