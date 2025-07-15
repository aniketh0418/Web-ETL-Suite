# 🔄 MultiFormat-ETL-Pipeline

This project is a simple **ETL (Extract, Transform, Load)** pipeline in Python that processes data from multiple file formats — **CSV**, **JSON**, and **XML**. It converts height (in inches to meters) and weight (in pounds to kilograms), logs each phase, and exports the cleaned data to a single CSV file.

---

## 📌 Features

- ✅ Extracts data from `.csv`, `.json`, and `.xml` files
- 🧪 Transforms height and weight units to metric:
  - Inches → Meters
  - Pounds → Kilograms
- 💾 Loads cleaned data into a CSV file (`transformed_data.csv`)
- 📝 Logs every step in `log_file.txt`

---

## 📦 Requirements

- Python 3.x
- `pandas`

Install dependencies:

```bash
pip install pandas
```

## 🚀 To Run

```bash
git clone https://github.com/aniketh0418/Web-ETL-Suite.git
cd Web-ETL-Suite/MultiFormat-ETL-Pipeline
python etl_code.py
```
