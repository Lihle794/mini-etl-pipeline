import requests
import pandas as pd
import sqlite3
from datetime import datetime
import schedule
import time
import matplotlib.pyplot as plt
import seaborn as sns

# --- Extract ---
def extract_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    return response.json()

# --- Transform ---
def transform_data(data):
    records = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for coin, values in data.items():
        records.append({
            "coin": coin,
            "price_usd": values["usd"],
            "timestamp": timestamp
        })

    return pd.DataFrame(records)

# --- Load ---
def load_data(df, db_name="crypto_prices.db"):
    conn = sqlite3.connect(db_name)
    df.to_sql("prices", conn, if_exists="append", index=False)
    conn.close()
    print(f"✅ Data loaded into {db_name} at {datetime.now()}")

# --- ETL Job ---
def etl_job():
    data = extract_data()
    df = transform_data(data)
    load_data(df)

# --- Schedule ETL ---
schedule.every(5).minutes.do(etl_job)

def start_scheduler():
    print("🚀 Mini ETL pipeline started... Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)

# --- Visualization Function (run separately) ---
def visualize_data(db_name="crypto_prices.db"):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT * FROM prices ORDER BY timestamp", conn)
    conn.close()

    if df.empty:
        print("No data to visualize yet.")
        return

    sns.set(style="whitegrid")
    plt.figure(figsize=(10,5))

    for coin in df['coin'].unique():
        coin_df = df[df['coin'] == coin]
        plt.plot(pd.to_datetime(coin_df['timestamp']), coin_df['price_usd'], marker='o', label=coin)

    plt.title("Crypto Prices Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
   
    start_scheduler()
