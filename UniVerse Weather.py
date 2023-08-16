import requests
import sqlite3
import gradio as gr

# AccuWeather API key
API_KEY = "t8y3bNsmXjXnGAGvQpwOm5EIJ0arxyQ5"


def fetch_weather_data(city_name):
  url = f"http://dataservice.accuweather.com/currentconditions/v1/{city_name}?apikey={API_KEY}"
  response = requests.get(url)
  weather_data = response.json()[0]  # Assuming the first result is relevant

  temperature = weather_data["Temperature"]["Metric"]["Value"]
  humidity = weather_data["RelativeHumidity"]
  description = weather_data["WeatherText"]

  # Store data in SQLite database
  conn = sqlite3.connect("weather.db")
  cursor = conn.cursor()

  cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data
                    (city TEXT, temperature REAL, humidity INTEGER, description TEXT)'''
                 )

  cursor.execute("INSERT INTO weather_data VALUES (?, ?, ?, ?)",
                 (city_name, temperature, humidity, description))

  conn.commit()
  conn.close()

  return f"Weather data for {city_name} stored successfully."


# Create a Gradio interface
iface = gr.Interface(
    fn=fetch_weather_data,
    inputs="text",  # City name input
    outputs="text"  # Output message
)

# Launch the interface
iface.launch()
