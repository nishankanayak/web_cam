import streamlit as st
from PIL import Image

with st.expander("start camera"):
    # start the camera
    cam_img = st.camera_input("camera")

if cam_img:
    # create the pillow image instance
    img = Image.open(cam_img)

    # convert pillow image to greyscale
    grey_img = img.convert("L")

    # display greyscale image on webpage
    st.image(grey_img)