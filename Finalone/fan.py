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

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def main(command):
    if command=="on":
       engine = pyttsx.init()
       rate = engine.getProperty('rate')
       engine.setProperty('rate', rate-50)
       engine.setProperty('voice', "english")
       print "You asked me to switch on the fan..."
       engine.say("Switching on the fan, Sir.")
       engine.runAndWait()
       led=3
       GPIO.setup(led, GPIO.OUT)
       GPIO.output(led, 1)
    if command=="off":
       engine = pyttsx.init()
       rate = engine.getProperty('rate')
       engine.setProperty('rate', rate-50)
       engine.setProperty('voice', "english")
       print "You asked me to switch off the fan..."
       engine.say("Switching off the fan, Sir.")
       engine.runAndWait()
       led=3
       GPIO.setup(led, GPIO.OUT)
       GPIO.output(led, 0)

