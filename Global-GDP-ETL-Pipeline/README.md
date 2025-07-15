# 🌍 Global-GDP-ETL-Pipeline

This Python project performs an ETL (Extract, Transform, Load) process on the **nominal GDP data** of countries. The data is scraped from an archived version of a Wikipedia page using `BeautifulSoup`, transformed into billions of USD, and stored in **CSV**, **JSON**, and **SQLite** formats.

---

## 🔧 Features

- Extracts GDP data of countries from Wikipedia (archived via Wayback Machine)
- Cleans and transforms GDP values from strings to numerical format in **billions USD**
- Saves the final dataset to:
  - `Countries_by_GDP.csv`
  - `Countries_by_GDP.json`
  - `World_Economies.db` (SQLite database)
- Logs every ETL stage in `etl_projec_log.txt`
- Queries and prints countries with GDP >= 100 billion USD

---

## 📦 Requirements

- Python
- `requests`
- `beautifulsoup4`
- `pandas`
- `sqlite3` (standard with Python)

Install required packages:

```bash
pip install requests beautifulsoup4 pandas
```

## 🚀 To Run

```bash
git clone https://github.com/aniketh0418/Web-ETL-Suite.git
cd Web-ETL-Suite/Global-GDP-ETL-Pipeline
python etl_project_gdp.py
```
