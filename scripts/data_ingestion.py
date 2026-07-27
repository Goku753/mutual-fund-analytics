import os
import pandas as pd

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data", "raw")

files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".csv")])

print(f"\nFound {len(files)} CSV files.\n")

for file in files:

    print("=" * 80)
    print(f"Dataset : {file}")

    path = os.path.join(DATA_DIR, file)

    try:
        df = pd.read_csv(path)

        print("\nShape")
        print(df.shape)

        print("\nData Types")
        print(df.dtypes)

        print("\nFirst 5 Rows")
        print(df.head())

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nDuplicate Rows")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}")
        print(e)