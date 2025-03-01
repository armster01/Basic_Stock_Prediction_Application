import streamlit as st
import pandas as pd
from utils import get_stock_data, analyze_stock

st.title("📈 Stock Prediction & Analysis")

symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, AMZN)")

if st.button("Get Prediction"):
    stock_data = get_stock_data(symbol)
    
    if stock_data is not None:
        suggestion = analyze_stock(stock_data)
        
        st.write(f"### Stock Analysis for {symbol}")
        st.write(f"📌 Suggestion: **{suggestion}**")
        st.line_chart(stock_data["Close"])  # Plot stock closing prices
    else:
        st.error("Failed to fetch stock data. Please check the stock symbol.")
