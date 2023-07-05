import streamlit as st #app

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px #interactive
import plotly.graph_objects as go
from urllib.request import urlopen
import json

#Setup
df = pd.read_csv("data/mpg.csv")
unique_years = pd.unique(df['year'])

#App
st.title("Intro to streamlit")
st.header("MPG data exploration")

#Options
if_show_df = st.sidebar.checkbox("Show DataFrame")

alltext = "All"
years = [alltext] + sorted(unique_years)
selected_year = st.sidebar.selectbox("Choose a year", years)

if if_show_df:
    st.subheader("This is my dataset")
    st.dataframe(data = df)
    left_column, middle_columns, right_column = st.columns([3, 1, 1])
if selected_year == alltext:
    reduced_df = df
else:
    reduced_df = df[df["year"] == selected_year]
m_fig, ax = plt.subplots(figsize = (10, 8))
ax.scatter(reduced_df["displ"], reduced_df["hwy"])
ax.set_title("Engine size vs mileage")
st.pyplot(m_fig)

st.write("Still working")
