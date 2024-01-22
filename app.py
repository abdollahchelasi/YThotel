# https://www.youtube.com/watch?v=AqtLEgn1RoE


import streamlit as st
from pytube import YouTube 
import re

link = st.text_input("Enter URL : ")

if st.button("Show Qualities"):
  video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", link)
  video_id = video_id_match.group(1) if video_id_match else None

  if video_id:
    video = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    available_streams = video.streams.filter(file_extension="mp4").all()
    
    st.text("Available video qualities:")
    for stream in available_streams:
      st.write(f"* {stream.resolution}")
  else:
    st.error("Invalid YouTube URL.")

if st.button("Download"):
  video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", link)
  video_id = video_id_match.group(1) if video_id_match else None

  if video_id:
    video = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    available_streams = video.streams.filter(file_extension="mp4").all()

    # Select the quality from the dropdown menu
    stream_quality = st.selectbox("Select Video Quality", [str(stream.resolution) for stream in available_streams])

    if stream_quality:
      selected_stream = next((stream for stream in available_streams if str(stream.resolution) == stream_quality), None)

      if selected_stream:
        st.text("Downloading...")
        file_path = selected_stream.download(filename=f"{video.title}.mp4", path=st.get_downloads_path())
        st.text("Download complete!")

        # Display download link and video
        st.markdown(f"**Downloaded video:** [Link](file://{file_path})")
        st.video(file_path, width=selected_stream.width)
      else:
        st.text("Selected video quality is not available.")
    else:
      st.text("No suitable video stream found.")
  else:
    st.error("Invalid YouTube URL.")










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

   







