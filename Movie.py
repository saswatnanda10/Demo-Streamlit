from urllib import request
import pandas as pd 
import numpy as np 
import streamlit as st 
import requests

#from api import movieApi
#st.title("Balloonified Search")
st.markdown("<h1 style='text-align: center; color: red;'>SearchMe.com</h1>", unsafe_allow_html=True)
#Accepting input
movie=st.text_input("Please enter the name of the movie")

#resp=requests.get("http://www.omdbapi.com/?t=Spiderman-&plot=full")

if movie:
    try:
        st.balloons()
        st.write("1 result(s) found")
        url=f"http://www.omdbapi.com/?t={movie}&apikey=eca150c1"
        resp=requests.get(url)
        resp=resp.json()
        #st.write(resp)
        c1,c2=st.columns([1,3])
        with c1:
            st.image(resp['Poster'])
        with c2:
            st.subheader(resp['Title'])
            st.caption(f"Genre: {resp['Genre']}, Year: {resp['Year']}")
            st.write(resp['Plot'])
            st.text(f"Rating: {resp['imdbRating']}")
            st.progress(float(resp['imdbRating'])/10)  
            st.text(f"Box Office: {resp['BoxOffice']}")

    except:
        st.error("No such movie found")
