import requests
import pandas as pd
import os

scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)
data = response.json()

history = data["data"]
df = pd.DataFrame(history)

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create the full output path
output_path = os.path.join(BASE_DIR, "data", "raw", "HDFC_Top100_NAV.csv")

df.to_csv(output_path, index=False)

print(df.head())
print(f"Saved Successfully to:\n{output_path}")