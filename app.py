# https://www.youtube.com/watch?v=AqtLEgn1RoE

import streamlit as st
from pytube import YouTube

link = st.text_input("Enter URL : ")

if st.button("Download"):
    video = YouTube(link)
    available_streams = video.streams.filter(file_extension="mp4").all()
    stream_quality = st.selectbox("Select Video Quality", [str(stream.resolution) for stream in available_streams])

    if stream_quality:
        selected_stream = next((stream for stream in available_streams if str(stream.resolution) == stream_quality), None)
        if selected_stream:
            st.text("Downloading...")
            file_path = selected_stream.download(filename=f"{video.title}.mp4", path=st.get_downloads_path())
            st.text("Download complete!")

            # Provide a download link and display the video with audio
            st.markdown(f"**Downloaded video:** [Link](file://{file_path})")

            # Only allow 720p and 360p
            if str(selected_stream.resolution) == "1280x720":
                st.video(file_path, width=600)
            elif str(selected_stream.resolution) == "640x360":
                st.video(file_path, width=400)
            else:
                st.text("Selected video quality is not available.")
        else:
            st.text("Selected video quality is not available.")
    else:
        st.text("No suitable video stream found.")
else:
    st.text("Invalid YouTube URL.")


