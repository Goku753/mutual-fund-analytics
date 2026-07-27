import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "raw", "01_fund_master.csv")

df = pd.read_csv(file_path)

print("=" * 60)
print("Unique Fund Houses")
print("=" * 60)
print(df["fund_house"].unique())

print("\nTotal:", df["fund_house"].nunique())

print("\n" + "=" * 60)
print("Categories")
print("=" * 60)
print(df["category"].unique())

print("\nTotal:", df["category"].nunique())

print("\n" + "=" * 60)
print("Sub Categories")
print("=" * 60)
print(df["sub_category"].unique())

print("\nTotal:", df["sub_category"].nunique())

print("\n" + "=" * 60)
print("Risk Categories")
print("=" * 60)
print(df["risk_category"].unique())

print("\nTotal:", df["risk_category"].nunique())