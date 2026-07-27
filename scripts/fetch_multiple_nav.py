import requests
import pandas as pd
import os

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Output folder
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "raw")

# Mutual fund scheme codes
funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in funds.items():
    print(f"Fetching {fund_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "data" in data:
            df = pd.DataFrame(data["data"])

            file_path = os.path.join(OUTPUT_DIR, f"{fund_name}.csv")
            df.to_csv(file_path, index=False)

            print(f"✅ Saved: {file_path}")
        else:
            print(f"❌ No NAV data found for {fund_name}")
    else:
        print(f"❌ Failed to fetch {fund_name}")