# 🗂 Mini ETL Pipeline: Crypto Prices with GitHub Copilot

## 📖 Project Overview
This project is a **mini ETL (Extract, Transform, Load) pipeline** built in Python.  
It fetches cryptocurrency prices (Bitcoin and Ethereum) from the **CoinGecko API**, transforms the data into a clean format using **Pandas**, and stores it in a **SQLite database**.  

The pipeline runs automatically every 5 minutes using **Python’s schedule library**, and data can be visualized with **Matplotlib & Seaborn**.  

**GitHub Copilot** was used to speed up coding for API requests, SQL integration, and data transformation.  

---

## ⚙️ Tech Stack
- **Python 3**  
- **Pandas** – data cleaning & transformation  
- **Requests** – API requests  
- **SQLite** – local database  
- **SQLAlchemy** (optional for future expansion)  
- **schedule** – automatic ETL scheduling  
- **Matplotlib & Seaborn** – data visualization  
- **GitHub Copilot** – AI-assisted coding  

---

## 🔄 ETL Workflow
1. **Extract** – Fetch latest crypto prices from CoinGecko API.  
2. **Transform** – Format JSON into a structured Pandas DataFrame with columns: `coin`, `price_usd`, `timestamp`.  
3. **Load** – Append data to SQLite database `crypto_prices.db`.  
4. **Schedule** – Pipeline runs every 5 minutes automatically.  
5. **Visualize** – Use `visualize_data()` to generate line charts of prices over time.  

---

## 📊 Example Queries
You can query the database using Python or SQLite:

```sql
-- Latest 5 records
SELECT * FROM prices ORDER BY timestamp DESC LIMIT 5;

-- Maximum price
SELECT MAX(price_usd) FROM prices;

-- Average price over last 7 days
SELECT AVG(price_usd) FROM prices WHERE timestamp >= DATE('now','-7 day');
🚀 How to Run
1️⃣ Setup
bash
Copy code
git clone https://github.com/your-username/mini-etl-pipeline.git
cd mini-etl-pipeline
python3 -m venv venv
source venv/bin/activate       # Linux/Mac
# venv\Scripts\activate        # Windows
pip install -r requirements.txt
2️⃣ Start ETL Scheduler
bash
Copy code
python etl_pipeline.py
The pipeline fetches and stores crypto prices every 5 minutes.

Stop with Ctrl+C when needed.

3️⃣ Visualize Data (Optional)
python
Copy code
from etl_pipeline import visualize_data
visualize_data()
Generates a line chart of Bitcoin and Ethereum prices over time.

🧑‍💻 Skills Demonstrated
API integration with Python

Data cleaning & transformation using Pandas

Database interaction with SQLite

Automated pipelines with schedule

Data visualization with Matplotlib & Seaborn

AI-assisted coding with GitHub Copilot

Documentation & GitHub version control

🌟 Future Improvements
Add Streamlit dashboard for interactive charts

Deploy on cloud database (PostgreSQL on AWS RDS or Heroku)

Schedule using Airflow or Prefect for professional ETL workflows

Expand to more cryptocurrencies or additional financial data

🏆 About This Project
Built as a one-day showcase project to practice data engineering fundamentals while demonstrating AI-assisted coding with GitHub Copilot.
