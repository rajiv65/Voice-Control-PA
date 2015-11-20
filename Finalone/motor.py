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

def main(command):
    if command=="on":
    	print "if"
      #check if off and if yes, on. else exit.
    else:
    	print "else"
        #check if on and if yes, off. else exit. 

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.setProperty('voice', "english")
engine.say("Switching on the fan, Sir.")
engine.runAndWait()
#while True: time.sleep(1)



	



