import streamlit as st
from PIL import Image

st.subheader("Color to greyscale convertor")

upload_img=st.file_uploader("Upload Image")

with st.expander("start camera"):
    cam_img = st.camera_input("camera")   # start the camera

if cam_img:
    img = Image.open(cam_img)             # create the pillow image instance
    grey_img = img.convert("L")           # convert pillow image to greyscale
    st.image(grey_img)                    # display greyscale image on webpage

if upload_img:
    img1=Image.open(upload_img)
    grey_img1=img1.convert("L")
    st.image(grey_img1)