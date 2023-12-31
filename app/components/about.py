import streamlit as st
from PIL import Image
def render_about():
    avatar = Image.open("assets/me.jpg")
    competition = Image.open("assets/busitech.png")
    st.subheader("Nguyen Truc Cuong") 
    st.image(avatar, caption="", width=200)
    st.write("Hi! I am Cuong, a student at Hanoi University of Science and Technology, currently studying Computer Science as part of the HEDSPI program.")
    st.write("I am proficient in English with an IELTS score of 7.5 and I am also learning Japanese as my third language.")
    st.write("I am interested in Machine Learning and Computer Vision. I also have some experience in Web Development. ")
    st.write("I have participated in a few competitions namely the Junctionx Hanoi 2023 hackathon, Busitech Bootcamp 2023 (Runner-up Prize), and Student Creative Ideas Challenge - SCIC 2023 (2nd Prize).")
    st.image(competition, caption="Busitech 2023", width=500)
    st.subheader("Other Projects")
    st.write("This is my other deployed project, it is my first AI project. I used ReactJS for front-end and FastAPI for back-end.")
    st.markdown("[Fake Image Classifier](https://cinnamon-ai-entrance-test-ntc.vercel.app/)")
    