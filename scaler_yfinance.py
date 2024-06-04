import datetime

import pandas as pd
import yfinance as yf
import streamlit as st
import datetime
st.header('Stock Market analysis',divider='rainbow')

ticker_symbol = st.text_input('Enter stock Symbol','MSFT', key = 'placeholder')
ticker_data = yf.Ticker(ticker_symbol)

# Make multiple changeable col header;
col1,col2 = st.columns(2)
with col1:
    start_date = st.date_input('Input the Start date:', datetime.date(2019, 1, 1))
with col2:
    end_date = st.date_input('Input the Start date:', datetime.date(2024, 7, 6))

ticker_df = ticker_data.history(period = '1d', start = start_date,end = end_date )
st.dataframe(ticker_df)

st.write('Daily closing Price line chart')
st.line_chart(ticker_df['Close'])

st.write('Daily traded volume Price line chart')
st.line_chart(ticker_df['Volume'])