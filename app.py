import streamlit as st
from my_weather_api_connection import MyWeatherAPIConnection
import plotly.graph_objects as go

# Streamlit App
def main():
    st.title("My Weather API - Weather App")

    # User input for API key and city name
    api_key = st.text_input("Enter your API key:", type="password")
    city_name = st.text_input("Enter the city name:")

    if api_key and city_name:
        # Initialize the MyWeatherAPIConnection with the API key
        weather_api_connection = MyWeatherAPIConnection(api_key)

        # Fetch weather data for the specified city using the query method
        weather_data = weather_api_connection.query(city_name)

        if weather_data:
            st.write("Weather Data:")
            st.write("City:", weather_data["name"])
            st.write("Temperature:", weather_data["main"]["temp"], "°C")
            st.write("Humidity:", weather_data["main"]["humidity"], "%")
            st.write("Wind Speed:", weather_data["wind"]["speed"], "m/s")
            st.write("Weather Description:", weather_data["weather"][0]["description"])

            # Create a radar chart for weather parameters
            st.write("Weather Parameters:")
            parameters = ["Temperature", "Humidity", "Wind Speed"]
            parameter_values = [
                weather_data["main"]["temp"],
                weather_data["main"]["humidity"],
                weather_data["wind"]["speed"]
            ]

            fig_radar = go.Figure()

            fig_radar.add_trace(go.Scatterpolar(
                r=parameter_values,
                theta=parameters,
                fill='toself',
                line=dict(color='blue'),
                connectgaps=True
            ))

            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True),
                ),
                showlegend=False
            )

            st.plotly_chart(fig_radar)

        else:
            st.error("Error: Unable to fetch weather data for the provided city.")

if __name__ == "__main__":
    main()
