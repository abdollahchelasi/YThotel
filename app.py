# https://www.youtube.com/watch?v=AqtLEgn1RoE

import streamlit as st
from pytube import YouTube 
import re

link = st.text_input("Enter URL : ")

video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", link)
video_id = video_id_match.group(1) if video_id_match else None

if video_id:
    video = YouTube(f"https://www.youtube.com/watch?v={video_id}")

    # Use a progressive stream with audio
    selected_stream = video.streams.filter(progressive=True, file_extension="mp4").first()

    if selected_stream:
        if st.button("Download"):
            st.text("Downloading...")
            file_path = selected_stream.download(filename=f"{video.title}.mp4", path=st.get_downloads_path())
            st.text("Download complete!")

            # Provide a download link and display the video with audio
            st.markdown(f"**Downloaded video:** [Link](file://{file_path})")
            st.video(file_path)
        else:
            st.text("No suitable video stream found with audio.")
    else:
        st.text("No suitable video streams found.")
else:
    st.text("Invalid YouTube URL.")


































# import streamlit as st
# from pytube import YouTube 

# link = st.text_input("Enter URL : ")

# if st.button("Download"):
#     videoo = YouTube(link)
#     stream = videoo.streams.get_highest_resolution()
#     st.text("Downloading...")
#     file_path = stream.download()
#     st.text("Download complete!")
#     # Display video
#     st.video(file_path)


