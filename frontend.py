import streamlit as st
import requests

st.title('My iris flower classifier app')

st.write('Select your flower features:')

s_l = st.slider('Select a value for Sepal length', min_value=0, max_value=10, value=1, step=1)
s_w = st.slider('Select a value for Sepal width', min_value=0, max_value=10, value=1, step=1)
p_l = st.slider('Select a value for Petal length', min_value=0, max_value=10, value=1, step=1)
p_w = st.slider('Select a value for Petal width', min_value=0, max_value=10, value=1, step=1)

url = 'https://api15752-cctigceneq-ew.a.run.app/predict'
params = {
        'sepal_length': s_l,
        'sepal_width': s_w,
        'petal_length': p_l,
        'petal_width': p_w
}

response = requests.get(url=url,
             params=params).json()

st.write('The flower belongs to class', str(response["prediction"]))
