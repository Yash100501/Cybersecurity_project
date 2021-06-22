import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
temp_city_max = ((api_data['main']['temp_max']) - 273.15)
temp_city_min = ((api_data['main']['temp_min']) - 273.15)
weather_desc = api_data['weather'][0]['description']

hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']

date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("------------------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("------------------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Maximum temperature is: {:.2f} deg C".format(temp_city_max))
print ("Minimum temperature is: {:.2f} deg C".format(temp_city_min))
print ("Current weather description  :",format(weather_desc))

print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

with open('readme.txt', 'w') as f:
    f.write("-------------------------------------------------")
    f.write('\n')
    f.write("Weather Stats for - {}  || {} ".format(location.upper(), date_time))
    f.write('\n')
    f.write("-------------------------------------------------")
    f.write('\n')
    f.write('\n')
    f.write("Current temperature is: {:.2f} deg C".format(temp_city))
    f.write('\n')
    f.write("Maximum temperature is: {:.2f} deg C".format(temp_city_max))
    f.write("\n")
    f.write("Minimum temperature is: {:.2f} deg C".format(temp_city_min))
    f.write("\n")
    f.write("Minimum temperature is: {:.2f} deg C".format(temp_city_min))
    f.write("\n")
    f.write("Current weather description  : ")
    f.write(format(weather_desc))
    f.write("\n")
    f.write("Current Humidity      :")
    f.write(str(hmdt))
    f.write(" %")
    f.write("\n")
    f.write("Current wind speed    :")
    f.write(format(wind_spd))
    f.write(" kmph")