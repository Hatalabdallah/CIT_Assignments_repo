# Weather Program Python Project Using the requests library, 
# create a program that will take a city name as input and 
# return the current weather for that city. The program should also save the city 
# name and the current weather to a file. The program should also be able to read the file 
# and print the city name and the current weather. Use this API to get the weather data: 
# https://openweathermap.org/current

import requests
import time

api_key = " 8a1175ba03ed5873fe140746ea42afbe"  # Enter the API key you got from the OpenWeatherMap website
base_url = "http://api.openweathermap.org/data/2.5/weather?"


print("\n\nCURRENT WEATHER CONDITION FOR YOUR CITY!")
time.sleep(2)

city_name = input("Enter city name : ")
time.sleep(1)

complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
response = requests.get(complete_url)
x = response.json() # JavaScript Object Notation (JSON) is a standardized format commonly 
# used to transfer data as text that can be sent over a network. It's used by lots of APIs and Databases,

if x["cod"] != "404":
    y = x["main"]

    current_temperature = y["temp"]
    z = x["weather"]

    weather_description = z[0]["description"]

    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n description = " +
                    str(weather_description))

else:
    print(" City Not Found ")



