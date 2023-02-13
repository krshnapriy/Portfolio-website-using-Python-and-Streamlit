from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Krishnapriya V S",page_icon="📍",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_4kx2q32n.json")
lottie_bullet = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_owsUdW27XG.json")

img_profile = Image.open("images/dp.png")

img_webpagehome = Image.open("images/1.jpeg")
img_webpageabt = Image.open("images/2.jpeg")
img_webpageform = Image.open("images/3.jpeg")
img_webpagegame = Image.open("images/4.jpeg")

img_reacthome = Image.open("images/5.jpeg")
img_reactinstr = Image.open("images/6.jpeg")
img_reactcountdown = Image.open("images/7.jpeg")
img_reactgame = Image.open("images/8.jpeg")

img_bookmenu = Image.open("images/9.jpeg")
img_bookhome = Image.open("images/10.jpeg")
img_bookcart = Image.open("images/11.jpeg")
img_bookpay = Image.open("images/12.jpeg")
img_bookmenu1 = Image.open("images/13.jpeg")

with st.container():
    image_column, text_column = st.columns((1,6))
    with image_column:
        st.image(img_profile)

    with text_column:
        st.subheader("Hi, I am Krishnapriya 👋")
        st.title("A Designing enthusiast")
        st.write("Passionate about crafting clean and user-friendly experiences")



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(
            """
            I'm Krishnapriya V S. I'm an Indian based web designer currently persuing my B-Tech Engineering 
            degree. I'm 18 years of age and is passionate about crafting clean and user-friendly experiences 
            for all. Though right now I'm focused more on completing my undergraduate degree, Web designing 
            is one profession which I easily love.

            I stay at Trivandrum with my parents both of whom are well - qualified engineers. My parent's love
            for their profession made me choose engineering as my path for career. I have been fortunate enough
            to receive a great educational exposure that enables me to have good knowledge of various technological
            advancements and front-end techniques in my field of interest. I love spending time on fixing little
            details and optimizing web apps. Also I like working in a team,one can learn faster and more. In my 
            free time, I am a freelance writer.
            """
        )

    with right_column:
        st_lottie(lottie_coding,height=400,key="coding")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    bullet,image1_column,image2_column, text_column = st.columns((1,1,1,3))

    with bullet:
        st_lottie(lottie_bullet,height=50,key="tick1")
    with image1_column:
        st.image(img_webpagehome)
        st.image(img_webpagegame)
        
    with image2_column:
        st.image(img_webpageabt)  
        st.image(img_webpageform)

    with text_column:
        st.subheader("Personal Website")
        st.write(
            """
            Created a website displaying all personal information made solely using HTML , CSS and Javascript inluded with a feedback form and simple math quiz game.

            """
        )

    st.write("##")
    st.write("##")
    bullet,image1_column,image2_column, text_column = st.columns((1,1,1,3))

    with bullet:
        st_lottie(lottie_bullet,height=50,key="tick2")

    with image1_column:
        st.image(img_reacthome)
        st.image(img_reactcountdown)
        
    with image2_column:
        st.image(img_reactinstr)  
        st.image(img_reactgame)

    with text_column:
        st.subheader("React JS Game")
        st.write(
            """
            Implemented a simple game using React JS and tailwind CSS framework for designing.
            """
        )

    st.write("##")
    st.write("##")
    bullet,image1_column,image2_column, text_column = st.columns((1,1,1,3))

    with bullet:
        st_lottie(lottie_bullet,height=50,key="tick3")

    with image1_column:
        st.image(img_bookmenu1)
        st.image(img_bookcart)
        
    with image2_column:
        st.image(img_bookhome)  
        st.image(img_bookpay)

    with text_column:
        st.subheader("Book Management System")
        st.write(
            """
            Made using Javascript implementing all the necessary OOP concepts. GUI – Swing components was used to design the front end of the system and JDBC to connect to databases.
            """
        )

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("📬 Get In Touch With Me !")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/krishnapriyavs247@gmail.com" method="POST">
        <input type="HIDDEN" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your e-mail" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)

        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

        local_css("style/style.css")

    with right_column:
        st.empty()
