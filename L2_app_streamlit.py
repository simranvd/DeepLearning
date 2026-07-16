#command: streamlit run L2_app_streamlit.py

import streamlit as st
import pandas as pd
import numpy as np

# Display a simple welcome message
st.title("Welcome to My Streamlit App")
st.write("This is a simple Streamlit application")

df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']})  

st.write(df)  

dfr = pd.DataFrame(
    np.random.randn(20,3),columns=['Column 1', 'Column 2', 'Column 3'])
st.line_chart(dfr)