import pyttsx
import RPi.GPIO as GPIO
import time

def main():

   engine = pyttsx.init()
   rate = engine.getProperty('rate')
   engine.setProperty('rate', rate-50)
   engine.setProperty('voice', "english")
   print "You asked me to switch off all the appliances..."
   engine.say("Switching off all the appliances, Sir.")
   engine.runAndWait()

   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)

   led1=2
   led2=3

   GPIO.setup(led1, GPIO.OUT)
   GPIO.setup(led2, GPIO.OUT)

   GPIO.output(led1, 0)
   GPIO.output(led2, 0)

