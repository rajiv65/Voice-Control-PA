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
import RPi.GPIO as GPIO

def main():
   engine = pyttsx.init()
   rate = engine.getProperty('rate')
   engine.setProperty('rate', rate-50)
   engine.setProperty('voice', "english")
   print "You asked me to switch on all the appliances..."
   engine.say("Switching on all the appliances, Sir.")
   engine.runAndWait()

   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)

   led1=2
   led2=3

   GPIO.setup(led1, GPIO.OUT)
   GPIO.setup(led2, GPIO.OUT)

   GPIO.output(led1, 1)
   GPIO.output(led2, 1)
