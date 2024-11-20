import streamlit as st
import pandas as pd
import pickle

# load the model from disk.
with open('car_pred_model', 'rb') as f:
    model = pickle.load(f)

cars_df=pd.read_csv("./cars24-car-price.csv")

st.title("Car re-sale price prediction...!!!")

st.dataframe(cars_df.head())

col1, col2 = st.columns(2)

fuel_type=col1.selectbox("select the fuel type:",["Diesel","Petrol","CNG", "LPG","Electric"])
engine=col1.slider("set the engine power:", 500,5000,step=100)
transmission_type=col2.selectbox("select the transmission type:",["Manual","Automatic"])
seats=col2.selectbox("select number of seats:",[4,5,7,9,11])


encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
    }

if st.button("Get price"):
        encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
        encoded_transmission_type = encode_dict['transmission_type'][transmission_type]
        # call the model.predict() function
        input_data = [2012.0,2,120000,encoded_fuel_type,encoded_transmission_type,19.7,engine,46.3,seats]
        pred = model.predict([input_data])[0]

st.write(pred)
