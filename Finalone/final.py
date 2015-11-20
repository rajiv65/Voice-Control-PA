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
import multiprocessing
import news
import weather
import alarm
import pdf
import light
import alarm
import fan
import allon
import alloff


r = sr.Recognizer()
inp=""


pnews=0
pweather=0
ppdf=0
palarm1=0
pfan=0
plight=0
pallon=0
palloff=0
'''
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-60)
engine.setProperty('voice', "english")
engine.say("Hello, Sir. What can I do for you today?")
engine.runAndWait()

'''

while True:
     with sr.Microphone() as source:
          print("Say something!")
          audio = r.listen(source)
          try:
             inp=str(r.recognize_google(audio))
             print("You said "+inp)

             if "news" in inp and "stop" not in inp:
                
                category=""
                for i in range(0,len(inp)):
                    if inp[i]!=" ":
                       category+=inp[i] 
                    else: break
                pnews=multiprocessing.Process(target=news.main,args=(category,))
                pnews.start()
             if inp=="stop news":
                print "Stopping news"
                pnews.terminate()

             if inp=="weather":
                pweather=multiprocessing.Process(target=weather.main)
                pweather.start()
             if inp=="stop weather":
                print "Stopping weather update" 
                pweather.terminate()

             if "read" in inp:
                name=""
                mode=""
                namelength=0
             	for i in range(5,len(inp)):
                    if(inp[i]!=" "):
                 	 	name+=inp[i]
                 	 	namelength+=1
                    else: 
                        break	
                for i in range(namelength+6,len(inp)):
                 	mode+=inp[i]
                
                ppdf=multiprocessing.Process(target=pdf.main, args=(name, mode,))
                ppdf.start()
             if inp=="stop PDF":
                print("Stopping reading")
                ppdf.terminate()

             if "alarm" in inp:
                alarmtime=""
             	alarmevent=""
             	timecount=0
             	for i in range(6,len(inp)):
                    if inp[i]!=" ":
                       alarmtime+=inp[i]
                       timecount+=1
                    if inp[i]==" ":
                       break
                for i in range(timecount+6,len(inp)):
                       alarmevent+=inp[i]
                 
                palarm1=multiprocessing.Process(target=alarm.main,args=(alarmtime,alarmevent,))
                palarm1.start()
                
                
             if "fan" in inp:
                command=""
                for i in range(4,len(inp)):
                    command+=inp[i]
                pfan=multiprocessing.Process(target=fan.main,args=(command,))            
                pfan.start()  
             if "light" in inp:
                command=""
                for i in range(6,len(inp)):
                    command+=inp[i]
                plight=multiprocessing.Process(target=light.main,args=(command,))
                plight.start()
             if "motor" in inp:
                command=""
                for i in range(6,len(inp)):
                    command+=inp[i]
                pmotor=multiprocessing.Process(target=motor.main,args=(command,))      
             if inp=="shutdown":
                print "Goodbye, Sir. Hope to hear from you soon"
                sys.exit()      
             if inp=="all on":
                pallon=multiprocessing.Process(target=allon.main)
                pallon.start()
             if inp=="all of":
                palloff=multiprocessing.Process(target=alloff.main)        
                palloff.start()
               
          except sr.UnknownValueError:
                 print("Google Speech Recognition could not understand audio")
          except sr.RequestError as e:
                 print("Could not request results from Google Speech Recognition service; {0}".format(e)) 


