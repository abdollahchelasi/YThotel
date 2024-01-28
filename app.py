# https://www.youtube.com/watch?v=AqtLEgn1RoE

import streamlit as st
from pytube import YouTube 
import re

st.set_page_config(page_title="VeTube - Garden City Hotel Dubai",page_icon="logo.png",)

with open('c.css') as f:
    st.markdown(f"<style> {f.read()} </style>",unsafe_allow_html=True)


c1, c2=st.columns(2)

with c1:

    st.image("logo.png",width=110)
    st.text("Garden City Hotel Dubai")
    st.divider()


with c2:
    st.header("ve TUBE")
    st.text("Download Video YouTube")
    st.write("""
Search the YouTube video link and the video will be sent to you
""")
    
    
  

link = st.text_input("Enter URL : ",)

st.button("Search",link)

video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", link)
video_id = video_id_match.group(1) if video_id_match else None



if video_id:
   video = YouTube(f"https://www.youtube.com/watch?v={video_id}")
   available_streams = video.streams.filter(file_extension="mp4").all()
   stream_quality = st.selectbox("Select Video Quality", [str(stream.resolution) for stream in available_streams])

   if st.button("Download"):
       selected_stream = next((stream for stream in available_streams if str(stream.resolution) == stream_quality), None)
       if selected_stream:
           st.text("Downloading...")
           file_path = selected_stream.download()
           st.text("Download complete!")
           st.divider()
           st.text("Click to download the video and wait a few moments for the download to take effect")
           
           # Display video
           st.video(file_path)
       else:
           st.text("Selected video quality is not available.")
else:
   st.error("Search YouTube video link .")




with st.expander(label="Garden City Hotel Dubai",expanded=True):
    
    st.video("city.mp4",)

    st.write("""
Garden City Hotel is a New and Fresh & clean Hotel right in the middle of the Trading Places of Deira, Dubai in United Arab Emirates. Your place to rest during your budget value shopping,  satisfying all your needs from the shops around the Naif and Deira area. We provide a safe & secure environment for you, a Home away from Home, enjoying the personal services from our colleagues.
            
""")
    st.divider()

    st.write("""
# A D D R E S S

GARDEN CITY HOTEL

35 A st Naif Dubai, United Arab Emirates

Phone: +00971-4-8808831          
 
""")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.image('logo.png',width=60)

    
    
    with c2:
        st.markdown("[Whatsapp](https://wa.me/+971502259313)")

    with c3:
        st.markdown("[Website](https://www.gardencityhoteldubai.com)")
    
        st.markdown("[Email](info@gardencityhoteldubai.com)")


st.divider()

st.markdown("[Powered by -> ABDOLLAH CHELASI](https://abdollahchelasi.streamlit.app)")
