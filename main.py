import streamlit as st
import requests
API_KEY = "de2a75d1a88024ed8127b638d9773d4d"
lat = "30.4"
lon = "77.9"
city = "bidholi"

def find_current_weather(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    # base_url  = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    weather_data = requests.get(base_url).json()
    try:
        general = weather_data['weather'][0]['main']
        wind = weather_data['wind']['speed']
        icon_id = weather_data['weather'][0]['icon']
        temperature = round(weather_data['main']['temp'])
        icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City Not Found")
        st.stop()
    return general,temperature,icon,wind

def main():
    st.header("Find the Weather")
    general,temperature,icon,wind = find_current_weather(city)
    col_1,col_2 = st.columns(2)
    with col_1:
        st.metric(label = "Temperature",value=f"{temperature}°C")
    with col_2:
        st.write(general)
        st.image(icon)
        wind = wind*(18/5)
        wind = "{:.2f}".format(wind)
        # print(format_float)
        st.metric(label = "Wind Speed",value=f"{wind} Km/hr")
    
    # city = st.text_input("Enter the City").lower()
    # if st.button("Find"):
    #     general,temperature,icon = find_current_weather(city)
    #     col_1,col_2 = st.columns(2)
    #     with col_1:
    #         st.metric(label = "Temperature",value=f"{temperature}°C")
    #     with col_2:
    #         st.write(general)
    #         st.image(icon)
    



    
if __name__ == '__main__':
    main()