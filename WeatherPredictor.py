#BY ABHINAV SANTOSH PANDEY

import requests
import os
from datetime import datetime

abhi_api = os.environ['weather_report']
location = input("Enter the city name: ")

c_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+abhi_api
api_link = requests.get(c_api_link)
api_data = api_link.json()
#print(api_data)


temperature_city = ((api_data['main']['temp']) - 273.15)
weather_condition = api_data['weather'][0]['description']
humidity_city = api_data['main']['humidity']
wind_speedcity = api_data['wind']['speed']
dateandtime = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("**************************************************************")
print ("**************************************************************")
print ("Weather for  - {}  || {}".format(location.upper(), dateandtime))
print ("**************************************************************")
print ("**************************************************************")

print ("Current temperature is: {:.2f} deg C".format(temperature_city))
print ("Current weather condition is  :",weather_condition)
print ("Current Humidity is    :",humidity_city, '%')
print ("Current wind speed is   :",wind_speedcity ,'kmph')
