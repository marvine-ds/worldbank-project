# 🌍 World Bank Economic Data Analysis Pipeline

## 📌 Project Overview

This project builds an end-to-end ETL pipeline that extracts macroeconomic data from the World Bank API and stores it in a structured MySQL database for analysis.

The purpose of this project is to track and analyze:

- GDP growth
- Population changes
- Inflation trends
- Unemployment rates
- Differences between countries
- Economic trends over multiple years

The system enables long-term economic performance tracking and cross-country comparisons.

---

## 🎯 Project Objectives

This project is designed to:

- 📈 Identify countries with increasing GDP
- 📉 Detect countries with decreasing unemployment
- 👶 Monitor how population growth evolves over time
- 🌍 Compare economic performance between countries
- 📊 Analyze long-term economic trends
- 📌 Measure the effectiveness of economic strategies

For example, this system helps answer:

- Are countries with rising GDP also reducing unemployment?
- Is population growth accelerating in developing countries?
- Are anti-unemployment strategies producing measurable results?
- Are policies targeting high birth rates working?

---

## 🌎 Why This Matters

### 🏛 For Governments

- Supports evidence-based economic planning
- Helps allocate national resources efficiently
- Tracks whether unemployment-reduction policies are working
- Monitors demographic trends to plan infrastructure and services

### 🌐 For International Organizations (e.g., United Nations)

- Identifies economically vulnerable countries
- Helps prioritize food aid and humanitarian assistance
- Supports poverty reduction targeting
- Assists in allocating development funding strategically

### 📊 For Analysts & Economists

- Enables country-to-country comparisons
- Detects macroeconomic patterns and imbalances
- Tracks progress toward economic development goals

---

## 🏗 System Architecture (ETL Design)


---

## 🔄 Data Flow

1. Fetch official country metadata
2. Extract indicator data from the World Bank API
3. Clean and standardize records
4. Classify aggregates (World, Regions, Income Groups)
5. Load structured data into MySQL using upsert logic

---

## 📊 Indicators Included

- GDP (current US$)
- Total Population
- Inflation (CPI)
- Unemployment Rate

Additional indicators can be added easily in `fetch.py`.

---

## 🗄 Database Design

Table: `world_bank_indicators`

Primary Key:
(country_code, year, indicator_code)

This ensures:
- No duplicate country-year-indicator combinations
- Safe re-execution of the pipeline
- Accurate long-term trend tracking

The table also includes an `is_aggregate` flag to distinguish:

- Real countries
- Aggregates (World, Regions, Income Groups)

---

## 🚀 Key Features

- Metadata-driven country validation
- Automatic API pagination handling
- ISO3 country consistency
- Bulk insert using `executemany()`
- Idempotent upsert strategy
- Modular, scalable architecture

---

## 📈 Strategic Impact

This project enables:

- Measuring whether economic strategies reduce unemployment
- Evaluating whether GDP growth is sustainable
- Monitoring whether population growth aligns with economic expansion
- Supporting smarter global resource allocation

By structuring global economic data in a relational system, this project supports data-driven policy planning and international development prioritization.

---

## 👨‍💻 Author

Marvine Ekina  
Data Analyst | Data Scientist Enthusiast
