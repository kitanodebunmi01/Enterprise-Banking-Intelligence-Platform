# Enterprise Banking Intelligence & Early Warning Platform (EBIEWP)

## Overview

The Enterprise Banking Intelligence & Early Warning Platform (EBIEWP) is an end-to-end banking analytics project that simulates an enterprise-grade data warehouse used by commercial banks to monitor customer behaviour, lending performance, operational efficiency and revenue risk.

The platform generates realistic synthetic banking data using business-driven rules and prepares it for SQL analytics, Power BI dashboards and an Early Warning Engine capable of identifying emerging risks before they become critical.

This project demonstrates enterprise-scale data engineering, dimensional modelling, business intelligence and banking analytics using Python, SQL Server and Power BI.

---

# Enterprise Architecture

```text
Business Requirements
        │
        ▼
Enterprise Data Model
        │
        ▼
Python Data Generation Engine
        │
        ▼
Enterprise Data Warehouse

├── DimCustomer
├── DimBranch
├── DimAccount
├── DimDate
├── FactTransaction
├── FactLoan
├── FactRepayment
└── FactComplaint
        │
        ▼
SQL Server Analytics Layer
        │
        ▼
Power BI Semantic Model
        │
        ▼
Executive Intelligence Dashboards
        │
        ▼
Early Warning & Revenue Protection Engine
```

---

# Technologies

- Python
- Pandas
- SQL Server
- Power BI
- Power Query
- Git
- GitHub

---

# Project Statistics

| Component         |     Volume |
| ----------------- | ---------: |
| Customers         |    100,000 |
| Accounts          |    153,035 |
| Branches          |        150 |
| Calendar Dates    |      3,834 |
| Transactions      |      100M+ |
| Active Loans      |      4,937 |
| Repayment Records |    33,000+ |
| Complaint Records | **1.13M+** |


---

# Project Progress

## ✅ Phase 1 – Planning & Foundation

- [x] Business Requirements Document (BRD)
- [x] Enterprise Data Model
- [x] Enterprise Data Warehouse Architecture
- [x] Project Documentation
- [x] GitHub Repository
- [x] Folder Structure

---

## ✅ Phase 2 – Enterprise Data Warehouse

### Dimensions

- [x] DimCustomer
- [x] DimBranch
- [x] DimAccount
- [x] DimDate

### Fact Tables

- [x] FactTransaction
- [x] FactLoan
- [x] FactRepayment
- [x] FactComplaint

---

## 🚧 Phase 3 – Analytics Layer

- [ ] SQL Server Data Warehouse
- [ ] SQL Analytical Views
- [ ] Early Warning SQL Engine

---

## ⏳ Phase 4 – Business Intelligence

- [ ] Power BI Semantic Model
- [ ] Executive Dashboard
- [ ] Retail Banking Dashboard
- [ ] Credit Risk Dashboard
- [ ] Branch Performance Dashboard
- [ ] Early Warning Dashboard

---

# Project Structure

```text
Enterprise Banking Intelligence & Early Warning Platform
│
├── Data
│   ├── Dimensions
│   │   ├── DimCustomer.csv
│   │   ├── DimBranch.csv
│   │   ├── DimAccount.csv
│   │   └── DimDate.csv
│   │
│   ├── Facts
│   │   ├── FactTransaction_100.csv
│   │   ├── FactLoan_100.csv
│   │   └── FactRepayment_100.csv
│   │
│   └── Reference
│
├── Documentation
│
├── Python
│   ├── Generators
│   ├── Utilities
│   └── Data Validation
│
├── Power BI
│   ├── Validation
│   └── Dashboards
│
└── README Assets
```

---

# Enterprise Business Rules

The synthetic banking data generation engine incorporates realistic business rules including:

- Salary-based retail loan eligibility
- Minimum account age before lending
- Segment-specific loan products
- Income-based lending limits
- Behaviour-driven repayment profiles
- Consecutive missed repayment tracking
- Days Past Due (DPD)
- Outstanding principal reduction
- Loan maturity logic
- Payment behaviour deterioration
- Multi-account customer relationships
- Multi-currency account support
- Branch-specific customer allocation
- Behaviour-driven complaint profiles
- Customer complaint frequency modelling
- Complaint trend simulation
- Complaint severity modelling
- Category-driven complaint channels
- Resolution SLA tracking
- Customer satisfaction modelling
- Repeat complaint detection

---

# Current Datasets

| Dataset           |            Records | Status     |
| ----------------- | -----------------: | ---------- |
| DimCustomer       |            100,000 | ✅ Complete |
| DimBranch         |                150 | ✅ Complete |
| DimAccount        |            153,035 | ✅ Complete |
| DimDate           |              3,834 | ✅ Complete |
| FactTransaction   |              100M+ | ✅ Complete |
| FactLoan          | 4,937 Active Loans | ✅ Complete |
| FactRepayment     |            33,000+ | ✅ Complete |
| **FactComplaint** |         **1.13M+** | ✅ Complete |


---

# Data Validation

Every generated dataset is validated before being integrated into the enterprise warehouse.

## Customer Validation

![DimCustomer Validation](README%20Assets/Validation/DimCustomer_Validation.jpg)

---

## Branch Validation

![DimBranch Validation](README%20Assets/Validation/DimBranch_Validation.jpg)

---

## Account Validation

![DimAccounts Validation](README%20Assets/Validation/DimAccounts_Validation.jpg)

---

## Date Validation

![DimDate Validation](README%20Assets/Validation/DimDate_Validation.jpg)

---

## Loan Validation

![FactLoan Validation](README%20Assets/Validation/FactLoan_Validation.jpg)

---

## Repayment Validation

![FactRepayment Validation](README%20Assets/Validation/FactRepayment_Validation.jpg)

---

## Transaction Validation

![FactTransaction Validation](README%20Assets/Validation/FactTransaction_Validation.jpg)

---

## Complaint Validation

![FactComplaint Validation](README%20Assets/Validation/FactComplaint_Validation.jpg)

---


# Enterprise Data Warehouse

## Dimension Tables

| Dimension | Purpose |
|-----------|---------|
| DimCustomer | Customer demographics, segmentation and banking profile |
| DimBranch | Branch operations and geographic hierarchy |
| DimAccount | Enterprise banking account portfolio |
| DimDate | Enterprise calendar dimension |

---

## Fact Tables

| Fact Table | Purpose |
|------------|---------|
| FactTransaction | Customer transaction history |
| FactLoan | Enterprise lending portfolio |
| FactRepayment | Loan repayment behaviour and credit monitoring |
| FactComplaint | Customer experience, complaint lifecycle, SLA monitoring and service quality analytics |

---

# Early Warning Engine

The platform is being developed to proactively identify emerging banking risks before they become business-critical.

### Planned Detection Rules

- Loan repayment deterioration
- Consecutive missed repayments
- High Days Past Due (DPD)
- Complaint escalation trends
- Repeat complaint behaviour
- SLA breaches
- Declining account activity
- Customer churn indicators
- Branch underperformance
- Revenue leakage
- Customer profitability decline

---

# Project Roadmap

| Layer                         | Status     |
| ----------------------------- | ---------- |
| Business Requirements         | ✅ Complete |
| Enterprise Data Model         | ✅ Complete |
| Python Data Generation Engine | ✅ Complete |
| Enterprise Data Warehouse     | ✅ Complete |
| SQL Server Warehouse          | 🚧 Next    |
| Analytical SQL Views          | ⏳ Planned  |
| Power BI Semantic Model       | ⏳ Planned  |
| Executive Dashboards          | ⏳ Planned  |
| Early Warning Engine          | ⏳ Planned  |


---

# Project Progress Diagram

Business Requirements        ✅
        │
Enterprise Data Model        ✅
        │
Python Data Generation       ✅
        │
Enterprise Warehouse         ✅
        │
SQL Server                   🚧
        │
Power BI                     ⏳
        │
Early Warning Engine         ⏳

---



# Repository Notes

Only lightweight validation datasets are stored in this repository.

Production datasets (including the 100M+ transaction table) are generated locally using the supplied Python generators and are intentionally excluded from version control due to their size.

---

# Author

**Ogooluwakitan Odebunmi**

Business Intelligence Developer | Data Analytics | SQL | Python | Power BI | Banking Analytics

---