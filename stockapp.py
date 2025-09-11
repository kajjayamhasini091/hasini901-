import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import date, timedelta

# App Title
st.title("📈 Stock Trend Prediction Web App")

# Sidebar Input
st.sidebar.header("Stock Prediction Settings")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, RELIANCE.NS)", "AAPL")
start_date = st.sidebar.date_input("Start Date", date(2020, 1, 1))
end_date = st.sidebar.date_input("End Date", date.today())
days_to_predict = st.sidebar.slider("Days to Predict Ahead", 1, 30, 7)

# Fetch stock data
st.subheader(f"Stock Data for {ticker}")
data = yf.download(ticker, start=start_date, end=end_date)

if data.empty:
    st.error("❌ No data found. Please check the ticker symbol.")
else:
    st.write(data.tail())

    # Plot Closing Price
    st.subheader("Closing Price Trend")
    st.line_chart(data['Close'])

    # Prepare data for prediction
    df = data.reset_index()
    df['Days'] = np.arange(len(df))  # Days as numeric feature

    X = df[['Days']]
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)

    # Predict future days
    future_days = np.arange(len(df), len(df) + days_to_predict).reshape(-1, 1)
    future_preds = model.predict(future_days)

    # Show prediction
    st.subheader(f"Predicted Closing Prices for Next {days_to_predict} Days")
    future_dates = pd.date_range(end_date + timedelta(days=1), periods=days_to_predict)
    forecast_df = pd.DataFrame({'Date': future_dates, 'Predicted_Close': future_preds})
    st.write(forecast_df)

    # Plot prediction
    st.subheader("Prediction Trend")
    fig, ax = plt.subplots()
    ax.plot(df['Date'], y, label="Historical")
    ax.plot(forecast_df['Date'], forecast_df['Predicted_Close'], label="Prediction", linestyle="dashed")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    st.pyplot(fig)
