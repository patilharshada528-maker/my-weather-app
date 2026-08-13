import requests
import streamlit as st
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY= os.getenv('WEATHER_API_KEY')

st.set_page_config(page_title='Weather App',page_icon='⛅')

st.title('🌦️Weather App')

st.write('Enter the city name and click on the button to get the Weather data ')
city = st.text_input('Enter the city name')
#if(len(city) == 0):
    #st.warning('Enter a valid city name')

API_URL =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

if(st.button('Fetch Weather Data')):
    response = requests.get(API_URL)
    
    if(response.status_code == 200):
        st.success('Weather data fetch succesfully !') #Inbuillt feature for success msg
        data = response.json()
        #Display all data
        #st.write(data)
        #print(data)

        #Extract the weather data in variables
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        # 0 means index of the dictionary in the list [{}]
        weather = data['weather'][0]['main']
        country = data['sys']['country']
        name = data['name']
        
        #for displaying on browser
        #st.write(temperature,humidity,wind_speed,weather)
        #print(temperature,humidity,wind_speed,weather)
        
        st.subheader(f'Weather for {name}, {country}')
        
        #special function to display=metric & create 4 columns
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        
        col1.metric('Temperature',f'🌡️{temperature}°C')
        col2.metric('Humidity',f'💧{humidity}%')
        col3.metric('Wind Speed',f'🍃{wind_speed}m/s')
        col4.metric('Weather',f'🌤️{weather}')
    else:
        st.error('City Not Found') #Inbulit function to display error