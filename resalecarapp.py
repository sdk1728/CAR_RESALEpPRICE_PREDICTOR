import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Car Resale Price Predictor", page_icon="🚗", layout="wide")

# Load the trained model
model = joblib.load('Car_price_predictor')

# Set the background image with 30% transparency
st.markdown(
    """
    <style>
    body {
        background-image: url("wallpaperflare.com_wallpaper.jpg");
        background-size: cover;
        background-color: rgba(255, 255, 255, 0.7); /* 30% transparency */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Get Ahead of the Curve: Anticipate Your Car's Resale Value")

# Create two columns layout for input fields
left_column, right_column = st.columns(2)

# Left Column: Brand, Model Name, Manufacturing Year, and Buying Price
with left_column:
    brand = st.text_input("Brand")
    model_name = st.text_input("Model Name")
    manufacturing_year = st.number_input("Manufacturing Year", min_value=1886, max_value=2030, step=1)
    buying_price = st.number_input("Buying Price", min_value=0.1, step=0.1)

# Right Column: Kilometers, Fuel Type, Transmission, and Seller Type
with right_column:
    kilometers = st.number_input("Kilometers", min_value=0)
    fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG'])
    transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])
    seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual'])

# Create DataFrame for prediction
new_data = pd.DataFrame({
    'Buying_price': [buying_price],
    'Kms_Driven': [kilometers],
    'Owner': [1],  # Assuming owner as 1 for simplicity
    'age': [2023 - manufacturing_year],  # Calculate car age from manufacturing year
    'Fuel_Type_CNG': [1 if fuel_type == 'CNG' else 0],
    'Fuel_Type_Diesel': [1 if fuel_type == 'Diesel' else 0],
    'Fuel_Type_Petrol': [1 if fuel_type == 'Petrol' else 0],
    'Seller_Type_Dealer': [1 if seller_type == 'Dealer' else 0],
    'Seller_Type_Individual': [1 if seller_type == 'Individual' else 0],
    'Transmission_Automatic': [1 if transmission == 'Automatic' else 0],
    'Transmission_Manual': [1 if transmission == 'Manual' else 0],
})

# Submit button to trigger prediction
if st.button("Submit"):
    st.text("Predicting the Price...")
    st.spinner()

    # Run the prediction
    predicted_price = model.predict(new_data)[0]

    # Show the result
    st.success(f"Predicted Price: {round(predicted_price, 2)} lakhs")
