import streamlit as st
from PIL import Image
def render_about():
    avatar = Image.open("assets/me.jpg")
    st.subheader("Nguyen Truc Cuong") 
    st.image(avatar, caption="", width=200)
    st.write("HUSTer")