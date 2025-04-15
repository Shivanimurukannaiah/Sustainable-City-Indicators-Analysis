
import streamlit as st
from src.loader import load_city_data
from src.analyzer import compute_scores
from src.visualizer import show_city_scores

st.title("🌍 Sustainable City Indicators Dashboard")

df = load_city_data("data/urban_indicators.csv")
df = compute_scores(df)

st.write("### Urban Indicators Data", df)

st.write("### Sustainability Scores")
fig = show_city_scores(df)
st.plotly_chart(fig)
