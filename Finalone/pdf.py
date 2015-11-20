import pyPdf
import pyttsx
import sys

pdfname=""


def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content

def onStart(name):
   print 'Started reading'

def onWord(name, location, length):
   global pdfname
   f = open(pdfname+'.txt','w')
   f.write(str(location)+" "+str(length)+"\n")
   f.close()

def onEnd(name, completed):
   print 'Done reading'
   

def main(first_arg,second_arg):
   global pdfname
   engine = pyttsx.init()
   pdfname=first_arg
   if second_arg=='start':
      f = open(first_arg+'.txt','w')
      f.write("0 0")
      f.close() 
   try:
       content= getPDFContent(first_arg+'.pdf').encode("ascii", "ignore")
   except IOError:
       print "no such file"
       engine.say("Sorry. No such file.")
       engine.runAndWait()
       sys.exit()

   newcontent=""

   r=open(first_arg+'.txt','r+')
   filecontent=r.read()

   location=""
   length=""
   offset=0

   for char in filecontent:
       if char!=" ":
          location+=char
          offset+=1
       else:
            break 

   offset+=1


   for x in range(offset,len(filecontent)-2):
       length+=filecontent[x]


   location=int(location)


   for i in range(location,len(content)-location):
       newcontent+=content[location+i-1]


   rate = engine.getProperty('rate')
   engine.setProperty('rate', rate-60)
   engine.setProperty('voice', "english")
   engine.connect('started-utterance', onStart)
   engine.connect('started-word', onWord)
   engine.connect('finished-utterance', onEnd)
   engine.say(newcontent)
   engine.runAndWait()
