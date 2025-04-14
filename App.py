import streamlit as st
import requests

# Set up the FastAPI backend URL
BASE_URL = "http://127.0.0.1:8000"  # Update if hosted elsewhere

# Streamlit UI for user input
st.title("Product Recommendation System")

# User Input
user_id = st.text_input("Enter User ID (e.g., U001):")
product_id = st.text_input("Enter Product ID (e.g., P001):")

# Fetch Recommendations for User
if st.button("Get Recommendations for User"):
    if user_id:
        response = requests.get(f"{BASE_URL}/recommend/user/{user_id}")
        if response.status_code == 200:
            recommendations = response.json()["recommendations"]
            st.write("Recommended Products for User:", recommendations)
        else:
            st.error("Error fetching recommendations.")

# Fetch Similar Products
if st.button("Get Similar Products"):
    if product_id:
        response = requests.get(f"{BASE_URL}/recommend/product/{product_id}")
        if response.status_code == 200:
            similar_products = response.json()["similar_products"]
            st.write("Similar Products:", similar_products)
        else:
            st.error("Error fetching similar products.")
