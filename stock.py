import streamlit as st
import yfinance as yf
import datetime
st.title("Stock Price Analyser")

# symbol=st.text_input("Please enter Ticker symbol:","AAPL")

symbol= st.selectbox(
    "Please select ticker symbol",
    ("AAPL", "MSFT", "GOOG"),
)

st.write("You selected:", symbol)


col1, col2 = st.columns(2)

with col1:
    start_date=st.date_input("Please enter start date", datetime.date(2023, 10, 1))
    

with col2:
    end_date=st.date_input("Please enter end date", datetime.date(2024, 10, 1))
    


ticker_data=yf.Ticker(symbol)
ticker_df=ticker_data.history(period="1d", start=start_date, end=end_date)
st.dataframe(ticker_df.head())

st.title("Line_chart")
st.line_chart(ticker_df['Open'])
st.line_chart(ticker_df['Volume'])





