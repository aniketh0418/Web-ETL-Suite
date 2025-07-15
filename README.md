# 🧩 Web-ETL-Suite

Web-ETL-Suite is a collection of Python ETL pipelines that scrape data from archived web pages, transform it into clean formats, and load it into CSV, JSON, and databases. A hands-on toolkit to turn messy web data into structured, usable datasets — one script at a time. Web data doesn't stay messy for long, not with this Python-powered ETL suite.

---

## 📦 Contents

Each subfolder is a self-contained ETL project with its own script, README, and output files:

### 🔹 [`Top50-Movies-Scraper`](./Top50-Movies-Scraper)
Scrapes the Top 50 most highly ranked films from an archived webpage, stores them in a DataFrame, and saves to CSV and SQLite.

### 🔹 [`MultiFormat-ETL-Pipeline`](./MultiFormat-ETL-Pipeline)
Reads and consolidates data from multiple file formats (CSV, JSON, XML), transforms it, and loads it into a unified CSV. Demonstrates flexible data ingestion.

### 🔹 [`Global-GDP-ETL-Pipeline`](./Global-GDP-ETL-Pipeline)
Extracts country-wise nominal GDP data from an archived Wikipedia page, converts values from millions to billions, and stores the data in multiple formats.

### 🔹 [`Global-Banks-ETL`](./Global-Banks-ETL)
Scrapes the largest banks by market capitalization, applies currency conversion using custom exchange rates, and runs SQL queries for insights.

---

## 🎯 Purpose

This suite was built to:
- Demonstrate real-world ETL processes using Python
- Practice web scraping with BeautifulSoup
- Explore data transformation techniques
- Utilize logging and modular code design
- Build SQL-backed workflows with SQLite

---

## 🚀 How to Use

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/Web-ETL-Suite.git
cd Web-ETL-Suite
