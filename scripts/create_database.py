import os
import sqlite3
import pandas as pd

# Folders
DATA_FOLDER = "data/raw"      # Change to data/processed if using cleaned files
DB_FOLDER = "database"
DB_NAME = "mutual_fund.db"

os.makedirs(DB_FOLDER, exist_ok=True)

db_path = os.path.join(DB_FOLDER, DB_NAME)

# Connect to SQLite
conn = sqlite3.connect(db_path)

print("=" * 70)
print("CREATING DATABASE")
print("=" * 70)

csv_files = sorted([f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")])

for file in csv_files:
    table_name = os.path.splitext(file)[0]

    print(f"\nImporting {file}")

    path = os.path.join(DATA_FOLDER, file)

    df = pd.read_csv(path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"Table Created: {table_name}")
    print(f"Rows Imported: {len(df)}")

print("\nAll CSV files imported successfully!")

# Show all tables
print("\nDATABASE TABLES")
tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print(tables)

conn.close()

print("\nDatabase created successfully.")