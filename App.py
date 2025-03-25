import streamlit as st
import pandas as pd
import numpy as np


st.title("My first app")
st.write("Hello World") 

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=("col1", "col2")
)

st.write(df)

st.write("Below is a dataframe with a button")

if st.button("Say hello"):
    st.write("Hello!")      
    
st.write("Below is a dataframe with a checkbox")

if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"]
    )
    st.write(chart_data)

