import time
import sys
from urllib2 import urlopen
from json import loads
import codecs
import time
import pyttsx
import os
import speech_recognition as sr
import thread
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

      
def main(response,event):
   engine = pyttsx.init()
   rate = engine.getProperty('rate')
   engine.setProperty('rate', rate-60)
   engine.setProperty('voice', "english")

   print("Reminder has been set for %s hrs" % response)
   
   led=4
   GPIO.setup(led, GPIO.OUT)

   alarm = int(response)
   awake = 0
    # Loop to continuously check time, buzz the buzzer for the set alarm time
   while True:
            # Continually get's the time as an integer value
       curr_time = int(time.strftime("%H%M"))

            # Buzzes the buzzer when the time reaches the set alarm time
       if curr_time == alarm:
          GPIO.output(led, 1)
          engine.say("You've set an alarm. It's time for"+event+".")
          break

   engine.runAndWait()
   time.sleep(10)
   GPIO.output(led,0)
   print ("Done")


