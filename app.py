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

    # Add download button
    st.download_button(
        label="Download Video",
        filename=f"{video.title}.mp4",
        mime_type="video/mp4",
        data=file_path,
    )



















# import streamlit as st
# from pytube import YouTube

# link = st.text_input("Enter URL : ")

# if st.button("Download"):
#     try:
#         video = YouTube(link)
#         stream = video.streams.get_highest_resolution()
#         st.text("Downloading...")
#         file_path = stream.download()
#         st.text("Download complete!")
#         # Display video
#         st.video(file_path)
#     except:
#         st.error("Please enter a valid YouTube URL.")

   







