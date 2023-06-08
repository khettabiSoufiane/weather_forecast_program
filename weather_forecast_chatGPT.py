
# Weather forecast program
# Create by soufiane khettabi

# -------------------------

# import the modules
import tkinter as tk
from tkinter import messagebox
import requests

window = tk.Tk()
window.title("Soufiane-Weather forecast")
window.minsize(600, 400)

api_key = "ca467560ba9a8505945e052ea0886e16"

entry_var = tk.StringVar()

def get_data():
    
    """
    Retrieves weather data from the API based on the entered city name.

    Returns:
        temperature (float): The temperature in Celsius.
        humidity (int): The humidity percentage.
        wind_speed (float): The wind speed in km/h.
        pressure (int): The atmospheric pressure in hPa.
        precipitation (float): The precipitation percentage.
    """

    city_name = entry_var.get()
    url_openweathermap = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url_openweathermap)
        
    if response.status_code == 200:
        data = response.json()
        temperature_k = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        
        precipitation = 0  # Default value for precipitation if rain data is not available
        if "rain" in data and "1h" in data["rain"]:
            rain_data = data["rain"]["1h"]
            precipitation = (rain_data / 1.0) * 100
        
        return temperature_k, humidity, wind_speed, pressure, precipitation
    else:
        messagebox.showinfo("Message Error", "Try again please!")

def update_weather_data():

    # Update the weather data labels with the retrieved information

    temperature_k, humidity, wind_speed, pressure, precipitation = get_data()

    temperature_c = temperature_k - 273.15
    temperature_c_formatted = f"{temperature_c:.2f}°C"
    leble_Temperature.config(text=f"Temperature: {temperature_c_formatted}")
    leble_Humidity.config(text=f"Humidity: {humidity} %")
    leble_Wind_Speed.config(text=f"Wind Speed: {wind_speed} km/h")
    leble_Pressure.config(text=f"Pressure: {pressure} hPa")
    leble_Precipitation.config(text=f"Precipitation: {precipitation} %")

frame_input = tk.Frame(window)
leble_location = tk.Label(frame_input, text="Location:", font=20)
entry_location = tk.Entry(frame_input, textvariable=entry_var)
button_location = tk.Button(frame_input, text="Search", font=20, relief=tk.RAISED, width=6, command=update_weather_data)

frame_show = tk.Frame(window)
leble_Temperature = tk.Label(frame_show, text="Temperature: N/A", font=20)
leble_Humidity = tk.Label(frame_show, text="Humidity: N/A", font=20)
leble_Wind_Speed = tk.Label(frame_show, text="Wind Speed: N/A", font=20)
leble_Pressure = tk.Label(frame_show, text="Pressure: N/A", font=20)
leble_Precipitation = tk.Label(frame_show, text="Precipitation: N/A", font=20)

frame_input.grid(column=1, row=0, pady=10, sticky="NE")
leble_location.grid(column=0, row=0)
entry_location.grid(column=1, row=0, padx=20)
button_location.grid(column=2, row=0, padx=40)

frame_show.grid(column=0, row=1, padx=40, sticky="SW")
leble_Temperature.grid(column=0, row=0, pady=20, sticky="W")
leble_Humidity.grid(column=0, row=1, pady=20, sticky="W")
leble_Wind_Speed.grid(column=0, row=2, pady=20, sticky="W")
leble_Pressure.grid(column=0, row=3, pady=20, sticky="W")
leble_Precipitation.grid(column=0, row=4, pady=20, sticky="W")

# Add an additional button to clear the weather data

def clear_weather_data():
    leble_Temperature.config(text="Temperature: N/A")
    leble_Humidity.config(text="Humidity: N/A")
    leble_Wind_Speed.config(text="Wind Speed: N/A")
    leble_Pressure.config(text="Pressure: N/A")
    leble_Precipitation.config(text="Precipitation: N/A")

button_clear = tk.Button(frame_show, text="Clear", font=20, relief=tk.RAISED, width=6, command=clear_weather_data)
button_clear.grid(column=0, row=5, pady=20, sticky="W")

window.mainloop()
