import streamlit as st
def render_navbar(items):
    st.sidebar.header("Navigation")
    selected = "Image Semantic Segmentation"
    for item in items:
        nav_selection = st.sidebar.button(item)
        if nav_selection:
            selected = item
    st.title(selected)
    return selected