import requests
import json
from urllib.request import urlopen
import time
starttime = time.time()
while True:

  lat = '37.23' # Blacksburg latitude
  lon = '-80.41' # Blacksburg longitude
  key = '57d7073a29e4316cfa13d2b8d2747140' # Your key given after registration
  url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + key

  response = urlopen(url).read().decode('utf-8')
  obj = json.loads(response)
  api_time = obj['dt']
  api_time = str(api_time)
  temp = obj['main']['temp']
  temp = str(temp)
  feels_like = obj['main']['feels_like']
  feels_like = str(feels_like)
  temp_min = obj['main']['temp_min']
  temp_min = str(temp_min)
  temp_max = obj['main']['temp_max']
  temp_max = str(temp_max)
  pressure = obj['main']['pressure']
  pressure = str(pressure)
  humidity = obj['main']['humidity']
  humidity = str(humidity)
  visibility = obj['visibility']
  visibility = str(visibility)
  wind_speed = obj['wind']['speed']
  wind_speed = str(wind_speed)
  wind_deg = obj['wind']['deg']
  wind_deg = str(wind_deg)
  clouds = obj['clouds']['all']
  clouds = str(clouds)

  request_time = str(time.time())
  line = "{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}".format(request_time, api_time, temp, feels_like, temp_min, temp_max, pressure, humidity, visibility, wind_speed, wind_deg, clouds)
  print(line)

  f = open('ResultAPI_April5.txt', 'a')
  f.write(line + '\n')
  f.close()

  time.sleep(600.0 - ((time.time() - starttime) % 600.0))
