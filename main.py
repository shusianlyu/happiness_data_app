import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")

# Add two selectboxes
x_axis = st.selectbox("Select the data for the X-axis",
                      options=["GDP", "Happiness", "Generosity"])
y_axis = st.selectbox("Select the data for the y-axis",
                      options=["GDP", "Happiness", "Generosity"])

# Load the dataframe
df = pd.read_csv("happy.csv")

# Add subheader
st.subheader(f"{x_axis} and {y_axis}")

# Get the x and y value
x_list = df[x_axis.lower()]
y_list = df[y_axis.lower()]

# Create and add the plot to the page
figure = px.scatter(x=x_list, y=y_list, labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)

