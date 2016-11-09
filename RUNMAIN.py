#!/usr/bin/env python
# include RPi libraries in to Python code

import RPi.GPIO as GPIO
import time
import cam
import upc
import sensval
import os
import sendingfiles
import sendingfiles1
import sendingtrigger

# provide a loop to display analog data count value on the screen
while True:
    if not(sensval.analog_read() == 0):
        upc.main()
	print "1"
	os.system('python pycsv_withindexer.py dbitems.db /root/Desktop/GitReps/Hardware')
	print "1.5"
	sendingfiles1.main("/root/Desktop/GitReps/Hardware/dbitems.db")
	print "2"
	upc.clearcsv()
        print "3"
	sendingtrigger.main()
	cam.main()
	sendingfiles.main("/root/Desktop/capture_top.jpg")
	sendingfiles.main("/root/Desktop/capture_mid.jpg")
	sendingfiles.main("/root/Desktop/capture_low.jpg")
	print "Files sent!"
        GPIO.cleanup()
    time.sleep(0.05)
    
