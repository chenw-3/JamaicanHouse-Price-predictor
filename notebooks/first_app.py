import streamlit as st
import numpy as np 
import pandas as pd
import pickle
import string

#load model:
model = open('price_model.pkl', 'rb')

def main():
    # Title
    st.title('Hi there! Welcome to the Jamaican House Price Predictor')

    # header
    st.header('Fill out the following then press submit to get a rough estimate of what your house could be sold for!')

    # no. of beds slider
    beds = st.slider(label='Number of Bedrooms', max_value=10)

    # no. of bathrooms slider
    baths = st.slider(label='Number of Bathrooms', max_value=10)

    #Total sqft slider
    size = st.number_input(label='Total size of the house in Sqft', max_value=10000)

    #region slider
    location = st.slider(label='Kingston', max_value=20)

    

    inputs = [[beds, baths, size, location]]

    if st.button(label='Submit'): #button
        result = model.predict(inputs)
        updated_results = result.flatten().astype(int)
        st.success('Your house could be listed at JMD{} million'.format(updated_results))


if __name__ =='__main__':
    main()

