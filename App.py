import streamlit as st
import pandas as pd
import numpy as np


st.title("Assignment Week 6")

#product category
product_c = st.text_input("Product Category")
#customer location
customer_country = st.text_input("Country")
customer_state = st.text_input("State")
customer_city = st.text_input("City")
#shipping method 
shipping_method = st.text_input("Shipping Method")
#prediction of delivery time

if st.button("Predict"):
    st.write("The predicted delivery time is 5 days.")



