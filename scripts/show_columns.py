import sqlite3
import pandas as pd

conn = sqlite3.connect("database/mutual_fund.db")

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

for table in tables["name"]:
    print("\n" + "="*60)
    print(table)
    print("="*60)

    df = pd.read_sql(f'SELECT * FROM "{table}" LIMIT 5', conn)

    print(df.columns.tolist())

conn.close()