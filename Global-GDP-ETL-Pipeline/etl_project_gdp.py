from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import requests
from datetime import datetime

url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
db_name = "World_Economies.db"
table_name = "Countries_by_GDP"
csv_path = "Countries_by_GDP.csv"
json_path = "Countries_by_GDP.json"
log_file_path = "etl_projec_log.txt"
df = pd.DataFrame()

def log(msg):
    timestamp_format = "%Y-%h-%d-%H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file_path, "a") as f:
        f.write(timestamp + ":" + msg + "\n")

log("ETL Job Started...")

log("Data Extraction Started...")

html_page = requests.get(url).text 
data = BeautifulSoup(html_page, "html.parser")

tables = data.find_all("tbody")
rows = tables[2].find_all("tr")

for row in rows:
    col = row.find_all("td")
    if len(col)!=0:
        if col[0].find("a") is not None and "—" not in col[2]:
            data_dict = {
                "Country": col[0].a.contents[0],
                "GDP_USD_millions": col[2].contents[0]
            }
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)

log("Data Extraction Ended...")

log("Data Transformation Started...")

list1 = list(df["GDP_USD_millions"])
list2 = []
for item in list1:
    new_item = list(item.split(","))
    new_item = float("".join(new_item))
    new_item = round(new_item/1000, 2)
    list2.append(new_item)
df["GDP_USD_millions"] = list2
df = df.rename(columns = {"GDP_USD_millions":"GDP_USD_billions"})

log("Data Transformation Ended...")

log("Data Loading Started...")

df.to_csv(csv_path)

df.to_json(json_path)

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists="replace", index=False)

log("Data Loading Ended...")

log("ETL Job Ended...")

query_output = pd.read_sql(f"SELECT * FROM {table_name} WHERE GDP_USD_billions >= 100", conn)
print(query_output)
conn.close()