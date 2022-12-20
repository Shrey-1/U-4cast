import calendar  # Core Python Module
from datetime import datetime  # Core Python Module

import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu

import streamlit as st
import requests
import pandas as pd

import visualise as vs
import analysis as an
import model as md

API_KEY = "de2a75d1a88024ed8127b638d9773d4d"
lat = "30.4"
lon = "77.9"
city = "bidholi"

df = pd.read_csv("data/data.csv") #importing the dataset

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
        st.error("Data Not Found")
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
    options=["Prediction", "Analysis", "Visualization"],
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
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Temperature", value=f"{temperature}°C")
        with col2:
            st.metric(label="Humidity", value=f"{pressure} %")
        with col3:
            st.metric(label="Barometric Pressure", value=f"{humidity} hPa")
        
        st.subheader("Forecast")
        st.image("data\Figure_2.png")
        # gh1 = md.plot_forecast(df)
        # st.plotly_chart(gh1)

        "---"
        submitted = st.form_submit_button("Refresh")

if selected == "Visualization":
    st.header("Weather Visualization")
    # st.subheader("Weather Data")
    gh1 = vs.date_vs_avg_temp(df)
    st.plotly_chart(gh1)
    gh2 = vs.date_vs_max_min_temp(df)
    st.plotly_chart(gh2)
    gh3 = vs.date_vs_humidity(df)
    st.plotly_chart(gh3)
    gh4 = vs.rainstatus(df)
    st.plotly_chart(gh4)
    gh5 = vs.weather(df)
    st.plotly_chart(gh5)
    gh6 = vs.pastweek_temp(df)
    st.plotly_chart(gh6)
    # gh7 = vs.pastweek_aqi(df)
    # st.plotly_chart(gh7)

if selected == "Analysis":
    st.subheader("Cleaned Data")
    st.write(df)
    st.subheader("Highest Temperature Recorded")
    gh1 = an.max_temp_date(df)
    gh2 = an.max_temp(df)
    st.write(gh1, ":", gh2)
    st.subheader("Lowest Temperature Recorded")
    gh1 = an.min_temp_date(df)
    gh2 = an.min_temp(df)
    st.write(gh1, ":", gh2)
    col1, col2 = st.columns(2)
    st.subheader("Rain Status")
    gh3 = an.rain_status(df)
    st.write(gh3)
    st.subheader("Weather Count")
    gh4 = an.weather_count(df)
    st.write(gh4)
    # st.subheader("Storm Chances")
    # gh5 = an.storm_chances(df)
    # st.write(gh5)