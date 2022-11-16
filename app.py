import calendar  # Core Python Module
from datetime import datetime  # Core Python Module

import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu

import streamlit as st
import requests
API_KEY = "de2a75d1a88024ed8127b638d9773d4d"
lat = "30.4"
lon = "77.9"
city = "bidholi"

def find_current_weather(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    weather_data = requests.get(base_url).json()
    try:
        general = weather_data['weather'][0]['description']
        wind = weather_data['wind']['speed']
        icon_id = weather_data['weather'][0]['icon']
        temperature = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City Not Found")
        st.stop()
    return general,temperature,icon,wind,humidity,pressure

page_title = "U-4cast"
page_icon = ":sun_with_face:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Prediction", "Visualization", "Analysis"],
    icons=["pencil-fill", "bar-chart-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)

if selected == "Prediction":
    with st.form("entry_form", clear_on_submit=True):
        general,temperature,icon,wind,pressure,humidity = find_current_weather(city)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header(f"Bidholi")
        with col4:
            st.image(icon)
        "---"
        st.subheader(f"Current Weather: {general}" )
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Temperature", value=f"{temperature}°C")
        with col2:
            st.metric(label="Humidity", value=f"{humidity}%")
        with col3:
            st.metric(label="Pressure", value=f"{pressure} hPa")
        with col4:
            wind = wind*(18/5)
            wind = "{:.2f}".format(wind)
            st.metric(label="Wind", value=f"{wind} Km/hr")

        # st.image(icon)

        "---"
        submitted = st.form_submit_button("Refresh")

if selected == "Visualization":
    st.header("Weather Visualization")

if selected == "Analysis":
    st.header("Weather Analysis")