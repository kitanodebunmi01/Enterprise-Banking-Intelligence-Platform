# Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)

# SQL Server Implementation Guide

---

# Overview

This folder contains the complete SQL Server implementation of the Enterprise Banking Intelligence & Early Warning Platform (EBIEWP).

The SQL layer transforms synthetic banking datasets generated in Python into an enterprise-grade dimensional data warehouse capable of supporting executive reporting, business intelligence, operational analytics and future early warning capabilities.

The implementation follows a structured enterprise data warehousing approach, including database design, ETL, dimensional modelling, semantic modelling, performance optimization and comprehensive data validation.

---

# SQL Architecture

```text
Python Data Generation
        │
        ▼
CSV Datasets
        │
        ▼
SQL Server ETL
        │
        ▼
Enterprise Data Warehouse

├── Dimension Tables
├── Fact Tables
├── Relationships
├── Indexes
        │
        ▼
Semantic Layer

├── SQL Views
└── Stored Procedures
        │
        ▼
Power BI Semantic Model
        │
        ▼
Executive Dashboards
```

---

# SQL Development Workflow

The SQL implementation was completed using the following workflow.

| Script | Purpose |
|----------|----------|
| 01_Create_Database.sql | Creates the EBIEWP SQL Server database |
| 02_Create_Dimensions.sql | Creates all dimension tables |
| 03_Create_Facts.sql | Creates all fact tables |
| 04_Load_Data.sql | Loads generated CSV datasets into SQL Server |
| 05_Create_Primary_Keys.sql | Creates primary keys |
| 06_Create_Foreign_Keys.sql | Creates warehouse relationships |
| 07_Create_Indexes.sql | Optimizes query performance |
| 08_Create_Views.sql | Builds analytical SQL views |
| 09_Create_Stored_Procedures.sql | Creates reusable reporting procedures |
| 10_Data_Validation.sql | Performs enterprise warehouse validation |

---

# Enterprise Data Warehouse

## Dimension Tables

| Table | Description |
|--------|-------------|
| DimCustomer | Customer demographics and segmentation |
| DimAccount | Customer banking accounts |
| DimBranch | Branch hierarchy and geography |
| DimDate | Enterprise calendar dimension |

---

## Fact Tables

| Table | Description |
|--------|-------------|
| FactTransaction | Customer transaction history |
| FactLoan | Lending portfolio |
| FactRepayment | Loan repayment behaviour |
| FactComplaint | Complaint lifecycle analytics |

---

# ETL Pipeline

The SQL ETL process performs the following operations before data is loaded into the warehouse.

- Import source datasets
- Data cleansing
- Data standardization
- Business rule enforcement
- Surrogate key mapping
- Warehouse loading

Business rules are enforced during the ETL process to ensure that the warehouse contains trusted, analysis-ready data.

---

# Semantic Layer

The semantic layer exposes warehouse data through analytical SQL views and stored procedures.

## SQL Views

- Customer 360
- Loan Portfolio
- Loan Early Warning
- Complaint Insights
- Branch Performance
- Revenue Analytics

---

## Stored Procedures

Reusable stored procedures were developed to simplify analytical queries and support reporting.

Examples include:

- Customer 360
- Branch Performance
- High Risk Loans
- Customer Complaints

---

# Performance Optimization

The warehouse has been optimized using:

- Primary Keys
- Foreign Keys
- Clustered Indexes
- Non-Clustered Indexes
- Star Schema Design

These optimizations improve query performance for analytical workloads and Power BI reporting.

---

# Enterprise Validation Framework

The SQL implementation includes a comprehensive validation framework.

## Validation Categories

- Dataset Validation
- Row Count Validation
- Duplicate Detection
- Referential Integrity
- Mandatory Field Validation
- Banking Business Rules
- Semantic Layer Validation
- Stored Procedure Validation

The objective is to ensure that only trusted, business-ready data is exposed to downstream reporting tools.

---

# SQL Folder Structure

```text
SQL
│
├── 01_Create_Database.sql
├── 02_Create_Dimensions.sql
├── 03_Create_Facts.sql
├── 04_Load_Data.sql
├── 05_Create_Primary_Keys.sql
├── 06_Create_Foreign_Keys.sql
├── 07_Create_Indexes.sql
├── 08_Create_Views.sql
├── 09_Create_Stored_Procedures.sql
├── 10_Data_Validation.sql
│
└── README.md
```

---

# Implementation Status

| Component | Status |
|-----------|--------|
| Database | ✅ Complete |
| ETL | ✅ Complete |
| Data Warehouse | ✅ Complete |
| Primary Keys | ✅ Complete |
| Foreign Keys | ✅ Complete |
| Indexes | ✅ Complete |
| SQL Views | ✅ Complete |
| Stored Procedures | ✅ Complete |
| Validation Framework | ✅ Complete |
| Power BI Integration | 🚧 In Progress |

---

# Next Phase

The next phase of the project focuses on developing the Power BI semantic model and executive dashboards using the validated SQL Server warehouse as the primary analytical source.
