# S1.1: Design the "Visualise Data" page of the multipage app.
# Import necessary modules 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header('Visualised data')
  st.set_option('deprecation.showPyplotGlobalUse',False)
  st.subheader('Scatter Plot')
  feature_lst = st.multiselect('Select the x-axis:',
                               ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
  for i in feature_lst:
    st.subheader(f"Scatter plot between {i} and price")
    plt.figure(figsize=(12,6))
    sns.scatterplot(x=i,y='price',data=car_df)
    st.pyplot()
  st.subheader('Visualisation selector')
  plot_types = st.multiselect('Select charts/plots',('Histogram','Boxplot','Correlation Heatmap'))
  if 'Histogram' in plot_types:
    st.subheader('Histogram')
    columns = st.selectbox('Select the columns to create Histogram',('carwidth', 'enginesize', 'horespower'))
    plt.figure(figsize=(12,6))
    plt.title(f"Histogram for {columns}.")
    plt.hist(car_df[columns],bins='sturges',edgecolor='black')
    st.pyplot()
  if 'Boxplot' in plot_types:
    st.subheader('Boxplot')
    columns = st.selectbox('Select the columns to create the Boxplot',('carwidth', 'enginesize', 'horsepower'))
    plt.figure(figsize=(12,6))
    plt.title(f"Boxplot for {columns}")
    sns.boxplot(car_df[columns])
    st.pyplot()
  if 'Correlation Heatmap' in plot_types:
    st.subheader('Correlation Heatmap')
    plt.figure(figsize=(12,6))
    ax = sns.heatmap(car_df.corr(),annot=True)
    bottom,top = ax.get_ylim()
    ax.set_ylim(bottom+0.5,top-0.5)
    st.pytplot()