# 📘 CSV-to-SQLite-Loader

This project demonstrates how to load a CSV file into a SQLite database using Python and `pandas`. It also runs a set of SQL queries to extract insights and appends a new instructor record to the existing table. Ideal for learning basic data ingestion and manipulation with SQL.

---

## 📌 Features

- Loads data from a CSV file into a SQLite databases
- Creates and replaces a table (`instructor`) on every run
- Executes SQL queries:
  - Select all records
  - Select first names
  - Count total records
  - Filter based on country code
- Appends a new row to the table programmatically
- Uses `pandas` and `sqlite3` only — no external dependencies

---

## 📦 Requirements

- Python
- `pandas`
- `sqlite3` (comes with Python)

Install necessary packages:

```bash
pip install pandas
```

## 🚀 To Run

```bash
git clone https://github.com/aniketh0418/Web-ETL-Suite.git
cd Web-ETL-Suite/CSV-to-SQLite-Loader
python db_code.py
```
