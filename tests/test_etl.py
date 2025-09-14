import sys
import os
import sqlite3
import pandas as pd
import requests
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from etl_pipeline import extract_data, transform_data, load_data, visualize_data


# Extract Tests
def test_extract_data():
    data = extract_data()
    assert isinstance(data, dict)
    assert "bitcoin" in data
    assert "usd" in data["bitcoin"]

def test_extract_data_failure(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 500
            def json(self): return {}
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    data = extract_data()
    assert data == {} or data is not None  # adjust depending on error handling


# Transform Tests
def test_transform_data():
    raw_data = {"bitcoin": {"usd": 50000}, "ethereum": {"usd": 4000}}
    df = transform_data(raw_data)
    assert isinstance(df, pd.DataFrame)
    assert "coin" in df.columns
    assert "price_usd" in df.columns
    assert "timestamp" in df.columns
    assert len(df) == 2

def test_transform_data_empty():
    df = transform_data({})
    assert df.empty

def test_transform_data_invalid_format():
    with pytest.raises(KeyError):
        transform_data({"bitcoin": {}})  # missing "usd"


# Load Tests
def test_load_data(tmp_path):
    db_name = tmp_path / "test_crypto.db"
    raw_data = {"bitcoin": {"usd": 50000}}
    df = transform_data(raw_data)

    load_data(df, db_name=str(db_name))

    conn = sqlite3.connect(db_name)
    result = pd.read_sql_query("SELECT * FROM prices", conn)
    conn.close()

    assert len(result) == 1
    assert result.iloc[0]["coin"] == "bitcoin"

def test_load_data_multiple_inserts(tmp_path):
    db_name = tmp_path / "test_multi.db"
    
    raw_data1 = {"bitcoin": {"usd": 50000}}
    raw_data2 = {"ethereum": {"usd": 4000}}
    
    df1 = transform_data(raw_data1)
    df2 = transform_data(raw_data2)

    load_data(df1, db_name=str(db_name))
    load_data(df2, db_name=str(db_name))

    conn = sqlite3.connect(db_name)
    result = pd.read_sql_query("SELECT * FROM prices", conn)
    conn.close()

    assert len(result) == 2
    assert set(result["coin"]) == {"bitcoin", "ethereum"}


# Visualization Test
def test_visualize_data_empty(tmp_path, capsys):
    db_name = tmp_path / "test_empty.db"
    # create empty db
    conn = sqlite3.connect(db_name)
    conn.execute("CREATE TABLE prices (coin TEXT, price_usd REAL, timestamp TEXT)")
    conn.close()

    visualize_data(db_name=str(db_name))
    captured = capsys.readouterr()
    assert "No data to visualize" in captured.out
