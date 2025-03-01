import yfinance as yf
import pandas as pd

def get_stock_data(symbol):
    """Fetch stock data using Yahoo Finance."""
    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period="6mo")  # Fetch 6 months of data
        if df.empty:
            return None
        return df
    except Exception as e:
        print(f"Error fetching stock data: {str(e)}")
        return None

def analyze_stock(df):
    """Analyze stock trends using moving averages."""
    df["SMA_5"] = df["Close"].rolling(window=5).mean()
    df["SMA_20"] = df["Close"].rolling(window=20).mean()

    if df["SMA_5"].iloc[-1] > df["SMA_20"].iloc[-1]:
        return "BUY"
    else:
        return "SELL"
