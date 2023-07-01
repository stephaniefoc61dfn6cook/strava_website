import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from test import get_user_data2


st.set_page_config(page_title="fitness", page_icon=":flexed_biceps:", layout="wide")

#-- website header

with st.container():
    st.header("click bellow to connect your strava account")
    if st.button("connect strava"):
        get_user_data2()



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#-- load assets
bike = load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_1s5rotap.json')
azuki = Image.open("azuki .png")

#---header
with st.container():
    st.subheader("This is fitness coin test")
    st.title("our mission is to empower community through fitness")
    st.write("[Click here to learn more >](https://opensea.io)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what we do")
        st.write("we rug everyone")

    with right_column:
        st_lottie(bike, height= 300, key="biking")


#-- container with picture


# with st.container():
#     st.write("---")
#     st.header("this is my azuki")
#     st.write("##")
#     image_column, text_column = st.columns((1,2))
#     with image_column:
#         st.image(azuki)
#     with text_column:
#         st.subheader("this is best azuki ever")
#         st.write("text")
#         st.markdown("[watch video](https://www.youtube.com/watch?v=VqgUkExPvLY&t=188s)")
