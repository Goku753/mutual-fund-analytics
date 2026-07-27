import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

fund_master = pd.read_csv(
    os.path.join(BASE_DIR, "data", "raw", "01_fund_master.csv")
)

nav_history = pd.read_csv(
    os.path.join(BASE_DIR, "data", "raw", "02_nav_history.csv")
)

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing = master_codes - nav_codes

print("=" * 50)
print("AMFI Validation")
print("=" * 50)

print("Fund Master Codes :", len(master_codes))
print("NAV History Codes :", len(nav_codes))
print("Missing Codes :", len(missing))

if len(missing) == 0:
    print("\n✅ All AMFI codes are present.")
else:
    print("\nMissing Codes:")
    print(sorted(missing))