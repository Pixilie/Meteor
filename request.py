import requests
import json

city = "Paris"
API = "33f784258bbf921ad48a2b9b3d06d4c6"
units = "metric"
lang = "fr"

url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API + "&units=" + units + "&lang=" + lang

response = requests.get(url)

meteo = (response.json())

print(meteo)
