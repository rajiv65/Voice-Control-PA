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

def call_the_articles_category(category):
    url = "http://api.nytimes.com/svc/topstories/v1/"+category+".json?api-key=f2534c05939f85bd82ab204e8a9005b9:19:73425794 "
    return loads(urlopen(url).read())

def main(category):

   engine = pyttsx.init()
   rate = engine.getProperty('rate')
   #engine.setProperty('rate', rate+50)
   engine.setProperty('voice', "english")
   engine.say("Going to read "+category+" news.")
   articles_category = call_the_articles_category(category)

   title=[]
   abstract=[]

   for i in range(0,10):
      title.append(articles_category["results"][i]['title'].encode('ascii', 'replace'))
      abstract.append(articles_category["results"][i]['abstract'].encode('ascii', 'replace'))

   for i in range(0,10):  
      print(title[i])
      engine.say(title[i])
      engine.say(abstract[i])

   print "Going to read "+category+" news."
   engine.runAndWait()  
   
