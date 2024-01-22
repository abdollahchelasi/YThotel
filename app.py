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
  # Implementez your existing download logic here using video_id and selected_stream
  # ...









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

   







