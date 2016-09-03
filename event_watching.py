#!/usr/bin/env python

#Import for GPIO usage
import RPi.GPIO as GPIO
#Import for system and command line usage
import os
import triggers
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# when a rising edge is detected on port 23, regardless of whatever 
# else is happening in the program, the function upc_meth will be run
# 'bouncetime=300' includes the bounce control written into interrupts2a.py
GPIO.add_event_detect(3, GPIO.FALLING, callback=triggers.main, bouncetime=250)

raw_input("Press Enter when ready\n>")

try:  
    print "Waiting on button press"
    time.sleep(0.01)
    GPIO.wait_for_edge(8, GPIO.FALLING)  
    print "ending."
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
