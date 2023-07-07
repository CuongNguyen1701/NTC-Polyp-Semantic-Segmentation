import streamlit as st
def render_navbar(items, icons):
    st.sidebar.header("Navigation 🧭")
    selected = "Image Semantic Segmentation"
    
    for item, icon in zip(items, icons):
        nav_selection = st.sidebar.button(item + " " + icon)
        if nav_selection:
            selected = item
    st.title(selected)
    return selected