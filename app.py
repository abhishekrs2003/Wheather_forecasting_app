import streamlit as st
import pandas as pd
import numpy as np

# Page title
st.title("Weather Forecasting App")

# Load CSV file
data = pd.read_csv("data/weather_data.csv")

data['datetime'] = pd.to_datetime(data['date'])
st.line_chart(data, x='datetime', y="rain")

st.subheader("Froecasted Whether metrics for Tommorow")
col1,col2 = st.columns(2)
col1.metric("Temperature ", np.round(data["temperature_2m"].mean(),2))
col2.metric("Rain", np.round(data["rain"].mean(),2))
