import streamlit as st
import numpy as np
import pandas as pd

m = st.number_input("Enter number of rows:", min_value=1, step=1)
k = st.number_input("Enter number of columns:", min_value=2, step=1)

map_data = pd.DataFrame(
    np.random.randn(m, k) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)