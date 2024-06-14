import streamlit as st
import requests
API_KEY="02e1b10fa379451696a64f7b4b1b3010"


def find_current_weather(city):
    base_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    weather_data=requests.get(base_url).json()
    
    try:
        general=weather_data["weather"][0]["main"]
        temperature=round(weather_data["main"]["temp"])-273
        i=weather_data["weather"][0]["icon"]
        icon=f"https://openweathermap.org/img/wn/{i}@2x.png"
    except KeyError:
        st.error("city not found")
        st.stop()
    return general ,temperature,icon
def main():
    st.header("Find the Weather")
    city=st.text_input("Enter the city").lower()
    if st.button("Find"):
        general,temperature,icon=find_current_weather(city)
        col1,col2=st.columns(2)
        with col1:
            st.metric(label="Temperature",value=str(temperature)+" "+"°C")
        with col2:
            st.write(general)
            st.image(icon)
if __name__=='__main__':
    main()