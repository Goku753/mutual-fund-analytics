import sqlite3
import pandas as pd

conn = sqlite3.connect("database/mutual_fund.db")

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("Tables:")
print(tables)

for table in tables["name"]:
    rows = pd.read_sql(f"SELECT COUNT(*) AS total_rows FROM '{table}'", conn)
    print(f"{table}: {rows.iloc[0]['total_rows']} rows")

conn.close()