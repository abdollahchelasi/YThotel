# https://www.youtube.com/watch?v=AqtLEgn1RoE



import streamlit as st
from pytube import YouTube 

link = st.text_input("Enter URL : ")

if st.button("Download"):
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    st.text("Downloading...")
    file_path = stream.download()
    st.text("Download complete!")
    # Display video
    st.video(file_path)
    st.download_button("Download",video)
