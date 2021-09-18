# S6.3: Divide the web page into three columns to add more widgets.
import streamlit as st
import pandas as pd
import numpy as np
def app(car_df):
    # Displaying orginal dataset
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.expander("View Dataset"):
        st.table(car_df)

    st.subheader('Columsn Description')
    beta_col1,beta_col2 = st.columns(2)
    with beta_col1:
      if st.checkbox('Show all the column names'):
        st.table(list(car_df.columns))
    with beta_col2:
      if st.checkbox('View data columns'):
        column_data = st.selectbox('Select columns',('enginesize','horsepower','carwidth','price'))
        if column_data == 'carwidth':
          st.write(car_df['carwidth'])
        elif column_data == 'enginesize':
          st.write(car_df['enginesize'])
        elif column_data == 'horsepower':
          st.write(car_df['horsepower'])
        else:
          st.write(car_df['price'])
    # Display descriptive statistics.
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(car_df.describe())    
    