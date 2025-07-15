# 🎬 Top50-Movies-Scraper

This Python project scrapes the **Top 50 most highly ranked films** from a snapshot of the EverybodyWiki webpage using the **Wayback Machine**, extracts the relevant data using `BeautifulSoup`, and saves it to both a **CSV file** and a **SQLite database**.

---

## 🔧 Features

- Scrapes movie data including:
  - Average Rank
  - Movie Title
  - Year of Release
- Stores data in:
  - A CSV file (`top_50_movies.csv`)
  - An SQLite database (`movies.db`)
- Easy to run and extend

---

## 📦 Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`
- `sqlite3` (comes with Python)


You can install the required packages with:

```bash
pip install requests beautifulsoup4 pandas

## 🚀 To Run

```bash
git clone https://github.com/aniketh0418/Web-ETL-Suite.git
cd Web-ETL-Suite/Top50-Movies-Scrapper
python Top-Movies-Scrapper.py
