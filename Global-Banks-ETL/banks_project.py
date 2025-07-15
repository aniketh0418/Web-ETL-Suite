from bs4 import BeautifulSoup
import pandas as pd
import requests
import sqlite3
from datetime import datetime

url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
db_name = "banks.db"
table_name = "Largest_banks"
conn = sqlite3.connect(db_name)
df = pd.DataFrame()
csv_path = "Largest_banks_data.csv"
log_file_path = "code_log.txt"
json_file_path = "Largest_banks_data.json"
exchange_rate_path = "exchange_rate.csv"

def log(msg):
    timestamp_format = "%Y-%h-%d-%H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file_path, "a") as f:
        f.write(timestamp + ":" + msg + "\n")

def extract(df, url):
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, "html.parser")

    tables = data.find_all("tbody")
    rows = tables[0].find_all("tr")

    for row in rows:
        col = row.find_all("td")
        if len(col)!=0:
            if col[1].find("a") is not None and "—" not in col[2]:
                name_attribute = col[1].find_all("a")[1]
                data_dict = {"Name": name_attribute.contents[0],
                            "MC_USD_Billion": float(col[2].get_text(strip=True))}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)
    return df

def transform(df, exchange_rate_path):
    dataframe = pd.read_csv(exchange_rate_path)
    dict = dataframe.set_index("Currency").to_dict()["Rate"]
    df["MC_GBP_Billion"] = [round(x*dict["GBP"], 2) for x in df["MC_USD_Billion"]]
    df["MC_EUR_Billion"] = [round(x*dict["EUR"], 2) for x in df["MC_USD_Billion"]]
    df["MC_INR_Billion"] = [round(x*dict["INR"], 2) for x in df["MC_USD_Billion"]]
    return df

def load(df, table_name, connection, csv_path, json_path):
    df.to_csv(csv_path)
    df.to_json(json_path)
    df.to_sql(table_name, connection, if_exists="replace", index=False)

queries = ["SELECT * FROM Largest_banks", "SELECT AVG(MC_GBP_Billion) FROM Largest_banks", "SELECT NAME from Largest_banks LIMIT 5"]
def run_queries(queries, connection):
    for query in queries:
        query_output = pd.read_sql(query, connection)
        print(query_output)

log("ETL Job Started...")
log("Data extraction Started...")
df = extract(df, url)
log("Data Extraction Ended...")
log("Data Tranformaiton Started...")
df = transform(df, exchange_rate_path)
log("Data Transformation Ended...")
log("Data Loading Started...")
load(df, table_name, conn, csv_path, json_file_path)
log("Data Loading Ended...")
log("ETL Job Ended...")
log("Running Queries...")
run_queries(queries, conn)
log("Queries Run...")
conn.close()