
import streamlit as st
import pickle
import pandas as pd
 
# Load trained model

import joblib 
model = joblib.load("")
 
st.set_page_config(
    page_title="Uber Fare Prediction System",
    page_icon="🚕",
    layout="centered"
)
 
st.title("🚕 Uber Fare Prediction System")
 
st.write("Enter ride details below:")
 
# Inputs
 
pickup_latitude = st.number_input(
    "Pickup Latitude",
    value=17.4459
)
 
pickup_longitude = st.number_input(
    "Pickup Longitude",
    value=78.3551
)
 
dropoff_latitude = st.number_input(
    "Dropoff Latitude",
    value=17.2305
)
 
dropoff_longitude = st.number_input(
    "Dropoff Longitude",
    value=78.4318
)
 
passenger_count = st.number_input(
    "Passenger Count",
    min_value=1,
    max_value=8,
    value=2
)
 
distance = st.number_input(
    "Distance (km)",
    min_value=0.0,
    value=10.0
)
 
bearing = st.number_input(
    "Bearing (degrees)",
    min_value=0.0,
    max_value=360.0,
    value=180.0
)
 
airport_dist = st.number_input(
    "Distance to Airport (km)",
    min_value=0.0,
    value=15.0
)
 
charminar_dist = st.number_input(
    "Distance to Charminar (km)",
    min_value=0.0,
    value=10.0
)
 
golconda_dist = st.number_input(
    "Distance to Golconda (km)",
    min_value=0.0,
    value=10.0
)
 
hitec_dist = st.number_input(
    "Distance to Hitec City (km)",
    min_value=0.0,
    value=10.0
)
 
hyd_center_dist = st.number_input(
    "Distance to Hyderabad Center (km)",
    min_value=0.0,
    value=10.0
)
 
hour = st.slider(
    "Hour of Day",
    min_value=0,
    max_value=23,
    value=12
)
 
day = st.slider(
    "Day",
    min_value=1,
    max_value=31,
    value=15
)
 
month = st.slider(
    "Month",
    min_value=1,
    max_value=12,
    value=6
)
 
weekday = st.slider(
    "Weekday (0=Mon)",
    min_value=0,
    max_value=6,
    value=3
)
 
year = st.number_input(
    "Year",
    min_value=2015,
    max_value=2035,
    value=2025
)
 
car_condition = st.selectbox(
    "Car Condition",
    [
        "Excellent",
        "Very Good",
        "Good",
        "Bad"
    ]
)
 
weather = st.selectbox(
    "Weather",
    [
        "clear",
        "cloudy",
        "humid",
        "rainy",
        "stormy",
        "windy"
    ]
)
 
traffic_condition = st.selectbox(
    "Traffic Condition",
    [
        "Flow Traffic",
        "Congested Traffic"
    ]
)
 
vehicle_type = st.selectbox(
    "Vehicle Type",
    [
        "Auto",
        "Go (Mini)",
        "Premier (Sedan)",
        "XL (SUV)",
        "Moto (Bike)"
    ]
)
 
if st.button("Predict"):
 
    input_data = pd.DataFrame({
 
        "pickup_longitude": [pickup_longitude],
        "pickup_latitude": [pickup_latitude],
        "dropoff_longitude": [dropoff_longitude],
        "dropoff_latitude": [dropoff_latitude],
        "passenger_count": [passenger_count],
        "hour": [hour],
        "day": [day],
        "month": [month],
        "weekday": [weekday],
        "year": [year],
        "airport_dist": [airport_dist],
        "charminar_dist": [charminar_dist],
        "golconda_dist": [golconda_dist],
        "hitec_dist": [hitec_dist],
        "hyd_center_dist": [hyd_center_dist],
        "distance": [distance],
        "bearing": [bearing],
        "Car Condition": [car_condition],
        "Weather": [weather],
        "Traffic Condition": [traffic_condition],
        "Vehicle Type": [vehicle_type]
    })
 
    prediction = model.predict(input_data)[0]
 
    st.success(f"💰 Predicted Fare Amount: ₹{prediction:.2f}")
