import streamlit as st
import joblib
import numpy as np
import pandas as pd
from pycaret.classification import *

# Load the model
model = load_model('./src/models/speciesPrediction')

# Define Streamlit app
st.title("Iris Species Prediction")

# Instructions
st.write("Enter the following features to predict the Iris species:")

# Create input fields for each feature
sepal_length = st.number_input('Sepal Length (cm)', value=0.0)
sepal_width = st.number_input('Sepal Width (cm)', value=0.0)
petal_length = st.number_input('Petal Length (cm)', value=0.0)
petal_width = st.number_input('Petal Width (cm)', value=0.0)

# Collect features into an array
features = pd.DataFrame({'sepal_length':[sepal_length], 'sepal_width':[sepal_width], 'petal_length':[petal_length], 'petal_width':[petal_width]})
# Prediction button
if st.button('Predict'):
    prediction = predict_model(model, data=features)
    species = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
    print(prediction)
    st.success(f"Prediction: {prediction['prediction_label'].iloc[0]}")
    #st.write(f'Prediction: {species[int(prediction[0])]}')
