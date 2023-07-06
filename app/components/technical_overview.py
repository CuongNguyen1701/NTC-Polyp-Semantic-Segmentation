import streamlit as st
def render_technical_overview():
    st.subheader("Technical Overview")
    st.write("This project is a web application that allows users to upload an endoscopic image and get the segmentation result of the polyp in that image. The application is built using Streamlit, a Python library for building web applications for machine learning and data science. The model is built using TensorFlow and Keras. The model is trained on the Kvasir-SEG dataset, which is a dataset for semantic segmentation of gastrointestinal polyps.")