import streamlit as st
import requests
import os

st.title("🏠 Delhi House Price Predictor")
st.markdown("Enter house details to get the predicted price:")

# Input fields
area = st.number_input("Area(sq ft)", min_value=100, value=1000)
latitude = st.number_input("Latitude", value=12.9)
longitude = st.number_input("Longitude", value=77.5)
bedrooms = st.number_input("Bedrooms", min_value=1, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, value=1)
neworold = st.selectbox("New or Old", ["New Property", "Resale"])
type_of_building = st.selectbox("Type of Building", ["Individual House", "Flat"])

# Furnishing status logic
if "furnished_semi" not in st.session_state:
    st.session_state["furnished_semi"] = False
if "furnished_un" not in st.session_state:
    st.session_state["furnished_un"] = False

def update_semi():
    """If 'Semi-Furnished' is checked, set 'Unfurnished' to False."""
    if st.session_state["furnished_semi"]:
        st.session_state["furnished_un"] = False

def update_unfurnished():
    """If 'Unfurnished' is checked, set 'Semi-Furnished' to False."""
    if st.session_state["furnished_un"]:
        st.session_state["furnished_semi"] = False

# Checkboxes with callback functions
furnished_semi = st.checkbox("Semi-Furnished", key="furnished_semi", on_change=update_semi)
furnished_un = st.checkbox("Unfurnished", key="furnished_un", on_change=update_unfurnished)

# Prediction Button
if st.button("Predict Price"):
    api_url = os.getenv("FLASK_ENV")
    
    # Prepare request data
    data = {
        "area": area,
        "latitude": latitude,
        "longitude": longitude,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "neworold": neworold,
        "type_of_building": type_of_building,
        "Furnished_status_Semi_Furnished": 1 if furnished_semi else 0,
        "Furnished_status_Unfurnished": 1 if furnished_un else 0
    }
    
    # Call Flask API
    response = requests.post(api_url, json=data)
    
    if response.status_code == 200:
        st.success(f"🏡 Predicted Price: ₹{response.json()['prediction']}")
    else:
        st.error("Error in prediction")
