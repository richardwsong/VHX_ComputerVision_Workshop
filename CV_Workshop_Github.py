import streamlit as st
import requests

visionKey = "KEY"
visionEndpoint = "ENDPOINT"

def get_image_features(img_url):
    analyze_url = f"{visionEndpoint}/vision/v3.1/analyze"

    headers = {
        'Ocp-Apim-Subscription-Key': visionKey
    }

    params = {
        'visualFeatures': 'Categories,Description,Color',
        'language': 'en',
    }

    data = {'url': img_url}

    response = requests.post(analyze_url, headers=headers, params=params, json=data)


    if response.status_code != 200:
        st.write("Error:", response.status_code)
        st.write(response.text)
        return None
    else:
        return response.json()

# Streamlit webapp
st.title('Computer Vision Workshop')

img_url = st.text_input('Enter Image URL')

if img_url:
    st.header('Original Image')
    st.image(img_url, use_column_width=True)

    parsed = get_image_features(img_url)

    if parsed:
        st.header('JSON Response')
        st.json(parsed)

        st.header('Image Caption')
        try:
            caption = parsed['description']['captions'][0]['text']
            st.write(caption)
        except (KeyError, IndexError) as e:
            st.write("Couldn't find a caption for this image.")
