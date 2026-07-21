# Employee Attrition Risk Analysis

An end-to-end HR analytics project that explores employee attrition patterns using SQL and predicts attrition risk using a Logistic Regression model — built to help HR teams prioritize retention efforts.

## Overview

Employee attrition is costly and hard to act on without data. This project takes raw HR data through cleaning, SQL-based exploratory analysis, and a classification model that scores every employee's risk of leaving — turning raw records into a prioritized, actionable view for HR.

Tested on the **HR Dataset** (rhuebner, Kaggle), the pipeline:
- Cleans and standardizes raw HR records
- Runs 5+ SQL exploratory queries (attrition by department, salary, recruitment source, satisfaction)
- Trains a Logistic Regression model (ROC-AUC 0.80) to score attrition risk
- Buckets every employee into a **Low / Medium / High** risk tier
- Outputs a summary of how many employees are likely to stay vs. leave

## Architecture

| Stage | File | Purpose |
|---|---|---|
| **Cleaning** | `clean_data.py` | Removes duplicates, standardizes columns, fills missing values |
| **SQL Analysis** | `sql_analysis.py` | Runs exploratory SQL queries via SQLite on the cleaned data |
| **Modeling** | `train_model.py` | Trains a Logistic Regression risk model and scores every employee |
| **Export** | `export_for_powerbi.py` | Outputs a Power BI-ready dataset |
| **Orchestration** | `main.py` | Runs the full pipeline end-to-end |

## Key Features

- **SQL-driven exploration** — attrition rate by department, average salary by department, performance score distribution, attrition by recruitment source, and satisfaction/engagement by department
- **Risk scoring** — every employee gets a risk_score (0–1) and a risk_tier (Low/Medium/High) based on Logistic Regression
- **Actionable summary** — the pipeline
