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
       print "You asked me to switch on the light..."
       engine = pyttsx.init()
       rate = engine.getProperty('rate')
       engine.setProperty('rate', rate-60)
       engine.setProperty('voice', "english")
       engine.say("Switching on the light, Sir.")
       engine.runAndWait()
       led=2
       GPIO.setup(led, GPIO.OUT)
       GPIO.output(led, 1)
    if command=="off":
       print "You asked me to switch off the light..."
       engine = pyttsx.init()
       rate = engine.getProperty('rate')
       engine.setProperty('rate', rate-50)
       engine.setProperty('voice', "english")
       engine.say("Switching off the light, Sir.")
       engine.runAndWait()
       led=2
       GPIO.setup(led, GPIO.OUT)
       GPIO.output(led, 0)


