import RPi.GPIO as GPIO, time
import urllib2
 
# Setting up variables for site checking
sitewearechecking = "http://www.idg.com.au"
textweshouldfind = "<title>IDG Communications - Australia</title>"
frequencyofchecking = 5 #Every 5 Seconds
siteup = False #True = site is up
 
# Setting up some structures for the Raspberry Pi LED controls
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
 
# Main program
try:
    while True:
        response = urllib2.urlopen(sitewearechecking)
        html = response.read()
        if textweshouldfind in html:
            siteup = True
            GPIO.output(GREEN_LED, True)
            GPIO.output(RED_LED, False)
        else:
            siteup = False
            GPIO.output(RED_LED, True)
            GPIO.output(GREEN_LED, False)
        if siteup == True:
            print "Site is up!"
        else:
            print "Site is down!"
        time.sleep(frequencyofchecking)
 
except KeyboardInterrupt:
    GPIO.cleanup()
