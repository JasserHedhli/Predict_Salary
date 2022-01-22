import streamlit as st
from prediction_page import *
from explore_page import *

page = st.sidebar.selectbox("Explore Or Predict", ('Explore', 'Predict'))


if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
