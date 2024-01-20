# https://www.youtube.com/watch?v=AqtLEgn1RoE



import streamlit as st
from pytube import YouTube 

link = st.text_input("Enter URL : ")

if st.button("Download"):
    videoo = YouTube(link)
    stream = videoo.streams.get_highest_resolution()
    st.text("Downloading...")
    file_path = stream.download()
    st.text("Download complete!")
    # Display video
    st.video(file_path)


    st.download_button(
        label="Download Video",
        filename=f"{video.title}.mp4",
        mime_type="video/mp4",
        data=file_path,
    )
