from urllib2 import urlopen
from json import loads
import codecs
import time
import pyttsx
import os
import atexit
import sys
import signal
import speech_recognition as sr
import thread






def get_weather_details():
    url = "http://api.openweathermap.org/data/2.5/weather?q=gandhinagar&APPID=0161c61999369a6dc6090163da35d4ba&units=metric"
    return loads(urlopen(url).read())

def main():
   engine = pyttsx.init()
   rate = engine.getProperty('rate')
   engine.setProperty('rate', rate-70)
   engine.setProperty('voice', "english")
   main=""
   description=""
   temp=0
   pressure=0
   humidity=0
   windspeed=0
   cloudy=0

   weather_details = get_weather_details()
   main=weather_details["weather"][0]['main']
   description=weather_details["weather"][0]['description']
   temp=weather_details["main"]['temp']
   pressure=(weather_details["main"]['pressure'])/1000
   humidity=weather_details["main"]['humidity']
   windspeed=weather_details["wind"]['speed']
   cloudy=weather_details['clouds']['all']
      
   engine.say("Today's weather report. Mainly"+main+".")
   engine.say("description"+description+".")
   engine.say("Temperature"+str(temp)+"degree celsius.")
   if temp>30:
      engine.say("It's quite a hot day. Maybe you should conaider turning on the AC.")
   if temp<=25:
      engine.say("It has dropped quite a bit. Get ready because winter is coming.")  
   engine.say("Pressure"+str(pressure)+"barometer.")
   engine.say("Humidity"+str(humidity)+"percentage.")
   if humidity>40:
      engine.say("You should wear light clothes today else risk getting soaked in sweat.")
   if humidity<40:
      engine.say("That's pretty good. Hit the gym. Sweat it out.")
   engine.say("Wind speed"+str(windspeed)+"meters per second")
   engine.say("Clouds"+str(cloudy)+"percentage.")
   if cloudy<30:
      engine.say("So, no rain today either.")
   print "Today's weather report."
   engine.runAndWait()

