# 🏦 Global-Banks-ETL

This Python-based ETL pipeline scrapes data on the **largest banks by market capitalization** from an archived Wikipedia page. It transforms the data into multiple currencies using real-world exchange rates, saves it in various formats, and runs SQL queries for insights.

---

## 📌 Features

- ✅ **Extracts** the names and market caps (in USD) of top banks from a Wikipedia archive
- 🔄 **Transforms** market cap data to GBP, EUR, and INR using a user-provided exchange rate CSV
- 💾 **Loads** the data into:
  - CSV file (`Largest_banks_data.csv`)
  - JSON file (`Largest_banks_data.json`)
  - SQLite database (`banks.db`)
- 📊 Executes sample SQL queries and prints results
- 📝 Logs every step to `code_log.txt`

---

## 📦 Requirements

- Python
- `pandas`
- `requests`
- `beautifulsoup4`
- `sqlite3` (comes with Python)

Install necessary packages:

```bash
pip install pandas requests beautifulsoup4
```

## 🚀 To Run

```bash
git clone https://github.com/aniketh0418/Web-ETL-Suite.git
cd Web-ETL-Suite/Global-Banks-ETL
python banks_project.py
```

## 🌐 Data Source - https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks
