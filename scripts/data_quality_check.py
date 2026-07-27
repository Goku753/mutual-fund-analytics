import os
import pandas as pd

RAW_FOLDER = "data/raw"

print("=" * 80)
print("MUTUAL FUND DATA QUALITY REPORT")
print("=" * 80)

csv_files = sorted([f for f in os.listdir(RAW_FOLDER) if f.endswith(".csv")])

for file in csv_files:

    print("\n" + "=" * 80)
    print(f"Dataset : {file}")
    print("=" * 80)

    path = os.path.join(RAW_FOLDER, file)

    try:
        df = pd.read_csv(path)
    except Exception as e:
        print("Could not read file:", e)
        continue

    # -------------------------------------------------
    # Dataset Shape
    # -------------------------------------------------

    print("\n1. Dataset Shape")
    print("----------------")
    print("Rows    :", df.shape[0])
    print("Columns :", df.shape[1])

    # -------------------------------------------------
    # Column Names
    # -------------------------------------------------

    print("\n2. Column Names")
    print("----------------")

    for col in df.columns:
        print(col)

    # -------------------------------------------------
    # Data Types
    # -------------------------------------------------

    print("\n3. Data Types")
    print("----------------")
    print(df.dtypes)

    # -------------------------------------------------
    # Missing Values
    # -------------------------------------------------

    print("\n4. Missing Values")
    print("----------------")

    missing = df.isnull().sum()

    if missing.sum() == 0:
        print("No Missing Values")
    else:
        print(missing)

    # -------------------------------------------------
    # Duplicate Rows
    # -------------------------------------------------

    print("\n5. Duplicate Rows")
    print("----------------")

    duplicates = df.duplicated().sum()
    print("Duplicate Rows :", duplicates)

    # -------------------------------------------------
    # Empty Strings
    # -------------------------------------------------

    print("\n6. Empty String Values")
    print("----------------")

    object_columns = df.select_dtypes(include="object").columns

    if len(object_columns) == 0:
        print("No Object Columns")
    else:
        for col in object_columns:
            empty = (df[col].astype(str).str.strip() == "").sum()
            print(f"{col} : {empty}")

    # -------------------------------------------------
    # Leading / Trailing Spaces
    # -------------------------------------------------

    print("\n7. Leading / Trailing Spaces in Column Names")
    print("--------------------------------------------")

    bad_columns = []

    for col in df.columns:
        if col != col.strip():
            bad_columns.append(col)

    if len(bad_columns) == 0:
        print("Column Names are Clean")
    else:
        print(bad_columns)

    # -------------------------------------------------
    # Numeric Summary
    # -------------------------------------------------

    print("\n8. Numerical Summary")
    print("----------------")

    numeric = df.select_dtypes(include="number")

    if numeric.empty:
        print("No Numeric Columns")
    else:
        print(numeric.describe())

    # -------------------------------------------------
    # Object Summary
    # -------------------------------------------------

    print("\n9. Categorical Columns")
    print("----------------")

    if len(object_columns) == 0:
        print("No Object Columns")
    else:
        for col in object_columns:

            print(f"\n{col}")
            print("-" * len(col))

            print("Unique Values :", df[col].nunique())

            print(df[col].value_counts().head(10))

    # -------------------------------------------------
    # Sample Records
    # -------------------------------------------------

    print("\n10. First Five Rows")
    print("-------------------")

    print(df.head())

print("\n")
print("=" * 80)
print("DATA QUALITY VALIDATION COMPLETED")
print("=" * 80)