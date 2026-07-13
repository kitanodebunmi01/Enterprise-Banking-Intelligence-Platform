/*
Enterprise Banking Intelligence & Early Warning Platform
Module 02 - Create Dimension Tables

Description:

Creates all dimension tables for the Enterprise Banking
Intelligence & Early Warning Platform (EBIEWP).
*/

USE EBIEWP;
GO

CREATE TABLE dbo.DimDate
(
	DateKey INT NOT NULL,

    [Date] DATE NOT NULL,

    [Year] SMALLINT NOT NULL,

    Quarter TINYINT NOT NULL,

    QuarterName VARCHAR(2) NOT NULL,

    MonthNumber TINYINT NOT NULL,

    MonthName VARCHAR(10) NOT NULL,

    MonthYear VARCHAR(10) NOT NULL,

    YearMonthKey INT NOT NULL,

    WeekNumber TINYINT NOT NULL,

    [Day] TINYINT NOT NULL,

    DayName VARCHAR(10) NOT NULL,

    FinancialYear SMALLINT NOT NULL,

    DaysInMonth TINYINT NOT NULL,

    MonthEndDate DATE NOT NULL,

    IsWeekend BIT NOT NULL,

    IsMonthStart BIT NOT NULL,

    IsMonthEnd BIT NOT NULL,

    IsLeapYear BIT NOT NULL

);

GO