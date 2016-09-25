#!/usr/bin/env python
# include RPi libraries in to Python code

import RPi.GPIO as GPIO
import time
import cam
import upc
import sensval
import sendingfiles

# provide a loop to display analog data count value on the screen
while True:
    if not(sensval.analog_read() == 0):
        upc.main()
	sendingfiles.main("/root/Desktop/items.csv")
        cam.main()
	sendingfiles.main("/root/Desktop/capture_top.jpg")
	sendingfiles.main("/root/Desktop/capture_mid.jpg")
	sendingfiles.main("/root/Desktop/capture_low.jpg")
        GPIO.cleanup()
    time.sleep(0.05)
    
