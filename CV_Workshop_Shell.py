import streamlit as st
import requests

visionKey = "KEY"
visionEndpoint = "ENDPOINT"

# Computer Vision API Call
def get_image_features(img_url):
    analyze_url = f"{visionEndpoint}/vision/v3.1/analyze"


# Streamlit webapp
st.title('Computer Vision Workshop')

