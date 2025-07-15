import sqlite3
import pandas as pd

conn = sqlite3.connect("staff.db")
table_name = "instructor"
attribute_list = ["ID", "F_NAME", "L_NAME", "CITY", "C_CODE"]

file_path = "INSTRUCTOR.csv"
df = pd.read_csv(file_path, names = attribute_list)

df.to_sql(table_name, conn, if_exists = "replace", index = False)

query_statements = ["SELECT * FROM instructor", "SELECT F_NAME FROM instructor", "SELECT COUNT(*) FROM instructor", "SELECT L_NAME FROM instructor WHERE C_CODE = 'IN'"]
for query_statement in query_statements:
    query_output = pd.read_sql(query_statement, conn)
    print(query_statement)
    print(query_output)

data_dict = {"ID": [100],
            "F_NAME": ["John"],
            "L_NAME": ["Doe"],
            "CITY": ["Paris"],
            "C_CODE": ["FR"]}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists = "append", index = False)
print("Data appended to 'instructor' table in 'staff' database successfully.")
conn.close()