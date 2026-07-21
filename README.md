# Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)

![Status](https://img.shields.io/badge/Status-SQL%20Implementation%20Complete-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQL Server](https://img.shields.io/badge/SQL%20Server-2022-red)
![Power BI](https://img.shields.io/badge/Power%20BI-In%20Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

# Enterprise Banking Analytics Platform

The **Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)** is an end-to-end enterprise banking analytics platform designed to simulate how commercial banks transform operational banking data into trusted business intelligence for executive decision-making.

The platform demonstrates the complete analytics lifecycle—from synthetic data generation and enterprise ETL to dimensional modelling, semantic modelling, SQL analytics and executive reporting.

Built using **Python**, **SQL Server**, and **Power BI**, EBIEWP consolidates customer, account, transaction, loan, repayment and complaint data into an enterprise-grade data warehouse capable of supporting operational reporting, customer intelligence, credit risk monitoring and an Early Warning Engine.

Rather than focusing on dashboard development alone, the project emphasizes enterprise data engineering principles including data quality, dimensional modelling, business rule enforcement and analytical scalability.

---

# Project Objectives

EBIEWP was developed to demonstrate how enterprise banking data platforms enable organizations to:

- Build an enterprise-grade dimensional data warehouse
- Centralize banking data from multiple business domains
- Deliver trusted data for executive decision-making
- Monitor lending performance and customer behaviour
- Improve operational visibility across branch networks
- Detect emerging business risks through early warning indicators
- Support business intelligence through Power BI dashboards
- Demonstrate enterprise SQL Server development and ETL best practices

---

# Key Features

## Enterprise Data Engineering

- Large-scale synthetic banking data generation
- Enterprise ETL pipeline
- Star schema dimensional modelling
- SQL Server data warehouse
- Performance indexing
- Data quality validation

## Banking Analytics

- Customer 360 Analytics
- Branch Performance Monitoring
- Loan Portfolio Analytics
- Repayment Behaviour Analysis
- Complaint Intelligence
- Customer Segmentation
- Revenue Analytics

## Enterprise SQL Layer

- Analytical SQL Views
- Stored Procedures
- Business Rule Enforcement
- Referential Integrity Validation
- Warehouse Health Validation

## Business Intelligence

- Power BI Semantic Model *(In Progress)*
- Executive Dashboards *(In Progress)*
- Early Warning Analytics *(Planned)*

---

# Project Highlights

- Enterprise-grade banking analytics platform built from scratch
- 100M+ synthetic banking transactions
- 100,000 customer records
- 1.13M+ complaint records
- End-to-end ETL pipeline with business rule enforcement
- Star schema dimensional data warehouse
- SQL semantic layer with analytical views and stored procedures
- Comprehensive warehouse validation framework
- Power BI executive dashboards (In Progress)

---

# Enterprise Architecture

```text
Business Requirements
        │
        ▼
Python Data Generation Engine
        │
        ▼
Synthetic Banking Datasets
        │
        ▼
SQL Server ETL Pipeline
        │
        ▼
Enterprise Data Warehouse

├── Dimension Tables
│     ├── DimCustomer
│     ├── DimAccount
│     ├── DimBranch
│     └── DimDate
│
└── Fact Tables
      ├── FactTransaction
      ├── FactLoan
      ├── FactRepayment
      └── FactComplaint
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
        │
        ▼
Early Warning & Decision Intelligence
```

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Programming | Python |
| Data Processing | Pandas |
| Synthetic Data | Faker |
| Database | SQL Server |
| ETL | T-SQL |
| Data Warehouse | Star Schema |
| Semantic Layer | SQL Views & Stored Procedures |
| Business Intelligence | Power BI |
| Version Control | Git & GitHub |

---

# Enterprise Data Warehouse

## Dimension Tables

| Dimension | Purpose |
|-----------|---------|
| DimCustomer | Customer demographics, segmentation and banking profile |
| DimAccount | Customer account portfolio |
| DimBranch | Branch hierarchy and geographic information |
| DimDate | Enterprise calendar dimension |

---

## Fact Tables

| Fact | Purpose |
|------|----------|
| FactTransaction | Banking transaction history |
| FactLoan | Lending portfolio |
| FactRepayment | Loan repayment monitoring |
| FactComplaint | Customer experience and complaint lifecycle analytics |

---

# Project Statistics

| Component | Volume |
|------------|-------:|
| Customers | 100,000 |
| Accounts | 153,035 |
| Branches | 150 |
| Calendar Dates | 3,834 |
| Transactions | 100M+ |
| Active Loans | 4,937 |
| Repayment Records | 33,000+ |
| Complaint Records | 1.13M+ |

---

# SQL Server Implementation

The SQL Server layer transforms the generated banking datasets into an enterprise-grade dimensional warehouse through a structured ETL process.

## SQL Components

- Database Creation
- Dimension Tables
- Fact Tables
- Data Loading
- ETL Transformations
- Primary Keys
- Foreign Keys
- Performance Indexes
- Analytical Views
- Stored Procedures
- Enterprise Validation Framework

---

# Enterprise Data Validation Framework

To ensure analytical reliability, the warehouse includes comprehensive validation covering:

- Dataset validation
- Row count validation
- Duplicate detection
- Mandatory field validation
- Referential integrity validation
- Banking business rule validation
- Semantic layer validation
- Stored procedure validation

The objective is to ensure that Power BI consumes trusted, business-ready data.

---

# Enterprise Business Rules

The platform incorporates realistic banking business rules across multiple domains.

## Customer Analytics

- Customer segmentation
- Multi-account relationships
- Customer lifecycle tracking
- Branch allocation

## Lending

- Income-based loan eligibility
- Outstanding principal monitoring
- Repayment behaviour analysis
- Consecutive missed repayments
- Days Past Due (DPD)
- Loan maturity tracking

## Customer Experience

- Complaint lifecycle management
- SLA monitoring
- Complaint escalation
- Customer satisfaction modelling
- Repeat complaint detection

## Operational Analytics

- Branch performance monitoring
- Revenue tracking
- Customer behaviour analysis
- Early warning indicators

---

# Project Status

| Phase | Status |
|--------|--------|
| Business Requirements | ✅ Complete |
| Enterprise Architecture | ✅ Complete |
| Python Data Generation | ✅ Complete |
| Enterprise Data Warehouse | ✅ Complete |
| SQL Server Implementation | ✅ Complete |
| Enterprise Validation Framework | ✅ Complete |
| Power BI Semantic Model | 🚧 In Progress |
| Executive Dashboards | ⏳ Planned |
| Early Warning Engine | ⏳ Planned |

---

# Project Structure

```text
Enterprise Banking Intelligence & Early Warning Platform
│
├── Data
│
├── Documentation
│
├── Python
│   ├── Generators
│   ├── Utilities
│   └── Validation
│
├── SQL
│   ├── Database
│   ├── ETL
│   ├── Views
│   ├── Stored Procedures
│   └── Validation
│
├── Power BI
│
└── README Assets
```

---

# Data Validation

Each generated dataset undergoes validation before loading into the warehouse.

The SQL implementation further validates:

- Referential Integrity
- Mandatory Fields
- Duplicate Records
- Business Rules
- Semantic Views
- Stored Procedures

Validation screenshots are available throughout this repository.

---

# Next Phase

The next stage of EBIEWP focuses on developing the Power BI semantic model and executive dashboards, including:

- Executive Banking Overview
- Customer 360 Dashboard
- Loan Portfolio Dashboard
- Credit Risk Dashboard
- Branch Performance Dashboard
- Complaint Intelligence Dashboard
- Early Warning Dashboard

---

# Repository Notes

The repository contains source code, validation datasets and documentation.

Large production datasets—including the 100M+ transaction dataset—are intentionally excluded from version control due to their size and can be regenerated locally using the supplied Python generators.

---

# Author

## Ogooluwakitan Odebunmi

Business Intelligence Developer | Data Analytics | SQL Server | Python | Power BI | Banking Analytics | Enterprise Data Warehousing

---

