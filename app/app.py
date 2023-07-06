import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from custom_layers import ConvBlock, UpConvBlock
import os
# Register the custom objects
tf.keras.utils.get_custom_objects()['ConvBlock'] = ConvBlock
tf.keras.utils.get_custom_objects()['UpConvBlock'] = UpConvBlock

IMG_SIZE = (256, 256)

# Load the Keras model
with tf.keras.utils.custom_object_scope({'ConvBlock': ConvBlock, 'UpConvBlock': UpConvBlock}):
    model = tf.keras.models.load_model(os.join(os.getcwd() , 'models/polyp_model.h5'))

@st.cache_data
def predict(image):
    # Preprocess the image
    img = np.array(image)
    img = np.expand_dims(img, axis=0)

    # Make prediction
    prediction = model.predict(img)
    prediction = np.squeeze(prediction)
    prediction = np.expand_dims(prediction, axis=-1)


    return prediction

def preprocess(image):
    img = image.convert('RGB').resize(IMG_SIZE)
    return img

# Main Streamlit app
def main():
    st.title("Image Semantic Segmentation")
    st.subheader("Polyp Segmentation") 
    st.write("Made by Nguyen Truc Cuong - HUST")
    gh_link = "[Visit my GitHub](https://github.com/CuongNguyen1701)"
    li_link = "[Visit my LinkedIn profile](https://www.linkedin.com/in/cuong-nguyen-209570237/)"
    links = ":computer: " + gh_link + " --- :male-office-worker: " + li_link
    st.markdown(links, unsafe_allow_html=True)
    
    # Upload and display the input image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        input_image = Image.open(uploaded_image)
        input_image = preprocess(input_image)
        # threshold = st.slider("Threshold", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        prediction_image = None
        
        # Perform prediction when the button is clicked
        if st.button("Predict"):
            prediction_image = predict(input_image)
            
        # Display input and output images side by side
        col1, col2 = st.columns(2, gap="medium")
        col1.header("Input Image (Resized)")
        col1.image(input_image, use_column_width=True)
        if prediction_image is not None:
            col2.header("Prediction")
            col2.image(prediction_image, use_column_width=True)

        # st.session_state.last_threshold = threshold
            


if __name__ == '__main__':
    main()
