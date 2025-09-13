# 🗂 Mini ETL Pipeline with SQL + GitHub Copilot

## 📖 Project Overview
This project is a **mini ETL (Extract, Transform, Load) pipeline** built in Python.  
It demonstrates how to fetch data from a public API, clean and transform it with **Pandas**, and load it into a database (**SQLite**).  

I used **GitHub Copilot** to speed up boilerplate code, generate SQL queries, and assist with Pandas transformations.  
The goal is to showcase how AI-assisted coding can make data engineering tasks more efficient. 🚀  

---

## ⚙️ Tech Stack
- **Python 3**  
- **Pandas** – data cleaning & transformation  
- **Requests** – fetching API data  
- **SQLAlchemy** – database interaction  
- **SQLite** – lightweight database for storage  
- **GitHub Copilot** – AI-assisted coding  

---

## 🔄 ETL Workflow
1. **Extract** – Fetch data from a public API (e.g., CoinGecko for crypto prices / OpenWeatherMap for weather).  
2. **Transform** – Clean and format JSON into a structured Pandas DataFrame.  
3. **Load** – Save the transformed data into an SQLite database.  
4. **Query** – Run SQL queries to get insights (latest values, averages, trends).  

---

## 📊 Example Queries
```sql
-- Get the latest record
SELECT * FROM prices ORDER BY date DESC LIMIT 1;

-- Get the maximum recorded value
SELECT MAX(price) FROM prices;

-- Get the average value over the last 7 days
SELECT AVG(price) FROM prices WHERE date >= DATE('now','-7 day');

🚀 How to Run

Clone the repository:

git clone https://github.com/your-username/mini-etl-pipeline.git
cd mini-etl-pipeline


Install dependencies:

pip install -r requirements.txt


Run the pipeline:

python etl_pipeline.py


Explore the SQLite database (etl_data.db) with your favorite SQL tool.

🧑‍💻 Skills Demonstrated

API integration with Python

Data cleaning with Pandas

SQL query writing & database management

AI-assisted development with GitHub Copilot

Documentation & version control with Git + GitHub

🌟 Future Improvements

Add a Streamlit dashboard to visualize data.

Schedule pipeline with Apache Airflow or Prefect.

Deploy on the cloud (AWS RDS + S3).

🏆 About This Project

Built as a one-day showcase project to practice data engineering fundamentals while exploring AI-assisted coding with GitHub Copilot.
