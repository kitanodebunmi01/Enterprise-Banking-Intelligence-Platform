/*
Enterprise Banking Intelligence & Early Warning Platform
Module 01 - Database Creation

Description:

Creates the Enterprise Banking Intelligence &
Early Warning Platform (EBIEWP) SQL Server database.
*/

USE master;
GO

IF DB_ID('EBIEWP') IS NULL
BEGIN

    CREATE DATABASE EBIEWP;

END;
GO

USE EBIEWP;
GO

--------------------------------

USE EBIEWP;
GO

IF NOT EXISTS
(
    SELECT 1
    FROM sys.schemas
    WHERE name = 'stg'
)
BEGIN
    EXEC('CREATE SCHEMA stg');
END;
GO