# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xtuvs4NdbTpNAxufGBqQ01ut_z5HwCHd
"""

import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import plotly.express as px
import matplotlib.pyplot as plt

# load the saved LSTM model
model = load_model('lstm_model.h5')

# function to make predictions using the loaded model
def predict_temperature(data):
    # slice the data to only include the last months
    data = data[-60:]
    # reshape the input data to match the expected input shape of the model
    data = data.reshape((1, data.shape[0], 1))
    # make the prediction
    prediction = model.predict(data)
    # return the predicted temperature value
    return prediction[0][0]

# set up the Streamlit app
st.set_page_config(page_title="Dengue Cases in Sri Lanka Predictor")
st.title("Dengue Cases Predictor")
st.write("This app predicts the next Dengue Cases in Sri Lanka")

# load the temperature data
data = pd.read_csv('Dengue_Data (2010-2020).csv', parse_dates='Date')
data.set_index('Date', inplace = True)

# display the current dengue cases data
st.subheader("Current Dengue Cases in Sri Lanka")
st.write(data.tail())

# get the latest dengue cases 
latest_case = data['Value'].iloc[-1]

# get the date of the latest dengue cases
latest_date = data.index[-1]

# make predictions for the next 30 days
predicted_temps = []
for i in range(5):
    next_date = latest_date + pd.Timedelta(days=1)
    pred_case = pred_case(np.array(data['Date']))
    pred_case.append(pred_case)
    latest_date = next_date
    data.loc[next_date] = pred_case

# display the predicted temperature values for the next 30 days
st.subheader("Next 12 Months' Dengue Cases")
st.write(data.tail(12)['Value'])


fig = px.line(data.tail(12), y='', title="Predicted Dengue Cases Graph for the next 12 Months")
st.plotly_chart(fig)

# plot the predicted temperature values
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(data['Value'], label='Actual')
ax.plot(data['Value'].tail(12), label='Predicted')
ax.set_xlabel('Year')
ax.set_ylabel('Dengue Cases')
ax.set_title('Actual vs Predicted Dengue Cases in Sri Lanka')
ax.legend()
st.pyplot(fig)
