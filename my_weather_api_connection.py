import requests
import streamlit as st
from streamlit.connections import ExperimentalBaseConnection

class MyWeatherAPIConnection(ExperimentalBaseConnection[dict]):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def _connect(self, city: str) -> dict:
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"  # Use "imperial" for Fahrenheit.
        }

        try:
            response = requests.get(self.base_url, params=params)

            if response.status_code == 200:
                weather_data = response.json()
                return weather_data
            else:
                st.error("Error: Unable to fetch weather data from the API.")
                return None

        except requests.RequestException as e:
            st.error(f"Error: Unable to connect to the API. {e}")
            return None

    def query(self, city: str) -> dict:
        return self._connect(city)
