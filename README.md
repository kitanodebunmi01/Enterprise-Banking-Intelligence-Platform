# Enterprise Banking Intelligence & Early Warning Platform

## Overview

This project simulates a large-scale banking analytics environment designed to proactively identify customer attrition, loan default risk, branch underperformance, and operational issues before they become critical.


## Enterprise Architecture Roadmap

```text
Business Requirements
        │
        ▼
Enterprise Data Model
        │
        ▼
Data Warehouse

├── DimCustomer
├── DimBranch
├── DimAccount
├── FactTransactions
├── FactLoans
├── FactComplaints
├── FactDigitalBanking
└── FactRevenue
        │
        ▼
Power BI Semantic Model
        │
        ▼
Executive Intelligence Dashboard
        │
        ▼
Early Warning & Revenue Protection
```

## Technologies

- Python
- Power BI
- SQL
- GitHub
- Power Query

## 📌 Project Progress

### ✅ Phase 1 – Planning & Foundation

- [x] Business Requirements Document (BRD)
- [x] Data Warehouse Architecture
- [x] Enterprise Data Model
- [x] Project Folder Structure
- [x] GitHub Repository
- [x] Project Documentation

---

### 🚧 Phase 2 – Data Warehouse Development

#### ✅ Module 1 – DimCustomer

- [x] Customer Identity
- [x] Customer Demographics
- [x] Customer Contact Information
- [x] Customer Segmentation
- [x] Customer Income Generation
- [x] Customer Join Date
- [x] Power BI Validation

---

#### ✅ Module 2 – DimBranch

- [x] Branch Identity
- [x] Geographic Hierarchy
- [x] Branch Opening Timeline
- [x] Employee Allocation
- [x] Branch Management
- [x] Branch Operational Status
- [x] Power BI Validation

---

#### ✅ Module 3 – DimAccount

- [x] Account Identity
- [x] Multi-Account Customer Portfolio
- [x] Account Type Generation
- [x] Multi-Currency Support
- [x] Account Status
- [x] Account Opening Date
- [x] Current Balance Generation
- [x] Enterprise Validation


## 📂 Project Structure

```
Enterprise Banking Intelligence & Early Warning Platform
├── Data
│   ├── Dimensions
│   │   ├── DimCustomer.csv
│   │   ├── DimBranch.csv
│   │   └── DimAccount.csv
│   │
│   ├── Facts
│   │
│   └── Reference
│
├── Documentation
│
├── PowerBI
│   ├── Validation
│   └── Dashboards
│
├── Python
│   ├── Generators
│   ├── Utilities
│   └── Data Validation
│
└── README Assets
```

## 📊 Current Datasets

| Dataset | Records | Status |
|----------|--------:|--------|
| DimCustomer | 100,000 | ✅ Complete |
| DimBranch | 150 | ✅ Complete |
| DimAccount | 160,040 | ✅ Complete |


## ✅ Data Quality & Validation

Every generated dataset is validated in Power BI before being integrated into the warehouse.

### DimCustomer Validation

![DimCustomer Validation](README%20Assets/Validation/DimCustomer_Validation.jpg)

---

### DimBranch Validation

![DimBranch Validation](README%20Assets/Validation/DimBranch_Validation.jpg)

---

### DimAccounts Validation

![DimAccounts Validation](README%20Assets/Validation/DimAccounts_Validation.jpg)


## 🏗️ Completed Data Warehouse Dimensions

| Dimension | Purpose |
|-----------|---------|
| DimCustomer | Customer demographics, segmentation and profile |
| DimBranch | Banking network and branch operations |
| DimAccount | Enterprise banking account portfolio, lifecycle, status, balances and currencies |


## 🏦 Enterprise Banking Data Warehouse Progress

| Layer | Status |
|-------|--------|
| Business Requirements | ✅ Complete |
| Enterprise Data Model | ✅ Complete |
| Data Warehouse Design | ✅ Complete |
| DimCustomer | ✅ Complete |
| DimBranch | ✅ Complete |
| DimAccount | ✅ Complete |
| FactTransactions | 🚧 Next Module |
| FactLoans | ⏳ Planned |
| FactComplaints | ⏳ Planned |
| FactDigitalBanking | ⏳ Planned |
| FactRevenue | ⏳ Planned |
| Early Warning Engine | ⏳ Planned |
| Executive Power BI Dashboard | ⏳ Planned |