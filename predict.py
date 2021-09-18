# S2.1: Import the necessary Python modules and create the 'prediction()' function as directed above.
# Importing the necessary Python modules.
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error, mean_squared_error, mean_squared_log_error
# Define the 'prediction()' function.
@st.cache()
def prediction(car_df,car_width, engine_size, horse_power, drive_wheel_fwd, car_comp_buick):
  X = car_df.iloc[:,:-1]
  y = car_df['price']
  X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
  lin_reg = LinearRegression()
  lin_reg.fit(X_train,y_train)
  score = lin_reg.score(X_train,y_train)
  price = lin_reg.predict([[car_width,engine_size,horse_power,drive_wheel_fwd,car_comp_buick]])
  price = price[0]
  y_test_pred = lin_reg.predict(X_test)
  test_r2_score = r2_score(y_test,y_test_pred)
  test_mae = mean_absolute_error(y_test,y_test_pred)
  test_mse = np.sqrt(mean_squared_error(y_test,y_test_pred))
  test_msle = mean_squared_log_error(y_test,y_test_pred)
  return price,score,test_r2_score,test_mae,test_mse,test_msle

# S2.2: Define the 'app()' function as directed above.
def app(car_df):
  st.markdown("<p style='color:blue;font-size:25px'> This app uses <b>Linear regression</b> to predict the price of a car based on your inputs.",unsafe_allow_html=True)
  st.subheader('Select values')
  car_wid = st.slider('Car width',float(car_df['carwidth'].min()),float(car_df['carwidth'].max()))
  eng_size = st.slider('Engine size',int(car_df['enginesize'].min()),int(car_df['enginesize'].max()))
  hor_pow = st.slider('Horse power',int(car_df['horsepower'].min()),int(car_df['horsepower'].max()))
  drw_fwd = st.radio('Forward drive wheel car?',('Yes','No'))
  if drw_fwd == 'No':
    drw_fwd = 0
  else:
    drw_fwd = 1
  com_bui = st.radio('Is the car manufactured by buick?',('Yes','No'))
  if com_bui == 'No':
    com_bui = 0
  else:
    com_bui = 1
  if st.button('Predict'):
    st.subheader('Predicted results:') 
    price,score, car_r2,car_mae,car_mse,car_msle = prediction(car_df,car_wid,eng_size,hor_pow,drw_fwd,com_bui)
    st.success('The prediction price of the car: ${:,}'.format(int(price)))
    st.info('Accuracy of the model is: {:2.2%}'.format(score))
    st.info(f"R2 score of the model is: {car_r2:.3f}")
    st.info(f"Mean absolute error for the model is: {car_mae:.3f}")
    st.info(f"Mean squared error for the model is: {car_mse:.3f}")
    st.info(f"Mean sqaured log error for the model is: {car_msle:.3f}")