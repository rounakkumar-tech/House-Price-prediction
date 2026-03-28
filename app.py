import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Load model
model = joblib.load("xgboost_model.pkl")

# Header
st.title("🏠 House Price Prediction System")
st.markdown("### Predict house prices using Machine Learning")

# Sidebar inputs
st.sidebar.header("Enter House Details")

area = st.sidebar.number_input(
    "Area (sq ft)",
    min_value=500,
    max_value=10000,
    value=1500
)

bedrooms = st.sidebar.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.sidebar.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

floors = st.sidebar.number_input(
    "Floors",
    min_value=1,
    max_value=5,
    value=1
)

year_built = st.sidebar.number_input(
    "Year Built",
    min_value=1900,
    max_value=2026,
    value=2015
)

location = st.sidebar.selectbox(
    "Location",
    ["Urban", "Suburban", "Rural"]
)

condition = st.sidebar.selectbox(
    "Condition",
    ["Poor", "Fair", "Good", "Excellent"]
)

garage = st.sidebar.selectbox(
    "Garage",
    ["Yes", "No"]
)

# Main prediction button
if st.button("🔍 Predict Price"):

    inp = {
        'Area': [area],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms],
        'Floors': [floors],
        'YearBuilt': [year_built],
        'Location': [location],
        'Condition': [condition],
        'Garage': [garage]
    }

    df_in = pd.DataFrame.from_dict(inp)

    df_enc = pd.get_dummies(df_in, columns=['Location', 'Condition', 'Garage'])

    df_enc = df_enc.reindex(columns=model.feature_names_in_, fill_value=0)

    price_pred = model.predict(df_enc)[0]

    st.success(f'Predicted house price: ${price_pred:,.2f}')

    st.write('Input features:')
    st.write(df_enc.T)