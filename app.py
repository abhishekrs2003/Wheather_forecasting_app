import streamlit as st
import pandas as pd

# Page title
st.title("Weather Forecasting App")

# Load CSV file
df = pd.read_csv("data/weather_data.csv")

# Show dataframe
st.subheader("Weather Dataset")
st.dataframe(df)

# Basic information
st.subheader("Dataset Information")
st.write(df.describe())

# Show temperature chart
st.subheader("Temperature Chart")
st.line_chart(df["temperature_2m"])

# Show rain chart
st.subheader("Rain Chart")
st.bar_chart(df["rain"])

# Select columns
st.subheader("Custom Column Viewer")

column = st.selectbox(
    "Select a column",
    df.columns
)

st.write(df[column])

# Success message
st.success("Weather data loaded successfully!")