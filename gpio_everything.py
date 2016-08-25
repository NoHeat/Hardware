#!/usr/bin/env python

#Import for GPIO usage
import RPi.GPIO as GPIO
#Import for system and command line usage
import os
import sys
#Import to R/W CSV
import csv
#Import for regular expression (used in parse_scanner_data)
import re
#Import for base 64 algorithms
import base64
#Import for hashes (ApiKey, ApiSecret)
import hashlib
import hmac
#Import used to fetch internet resources
import urllib2
#Import to use API
import json
#Import to interpret strings as binary
import struct
#Import to wait for I/O completion
import select
#Import for TCP/IP Usage
import socket

#GPIO Initial Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


#Environment Paths to change at a later time
cam_path = "/home/pi/Desktop/capture_"
upc_path = "/home/pi/Desktop/codes"

# GPIO 23 set up as input, pulled up to avoid false detection.
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#METHOD DEFINITIONS

#Definition for correct UPC format

def parse_scanner_data(scanner_data):
    upc_chars = []
    for i in range(0, len(scanner_data), 16):
        chunk = scanner_data[i:i+16]

        # The chunks we care about will match
        # __  __  __  __  __  __  __  __  01  00  __  00  00  00  00  00
        if chunk[8:10] != '\x01\x00' or chunk[11:] != '\x00\x00\x00\x00\x00':
            continue

        digit_int = struct.unpack('>h', chunk[9:11])[0]
        upc_chars.append(str((digit_int - 1) % 10))

    return ''.join(upc_chars)

#Definition for scanner usage

def upc_meth(channel):
    f = open('/dev/input/event2', 'rb')
    while True:
        print 'Waiting for scanner data'
        # Wait for binary data from the scanner and then read it
        scan_complete = False
        scanner_data = ''
        while True:
            rlist, _wlist, _elist = select.select([f], [], [], 0.1)
            if rlist != []:
                new_data = ''
                while not new_data.endswith('\x01\x00\x1c\x00\x01\x00\x00\x00'):
                    new_data = rlist[0].read(16)
                    scanner_data += new_data
                # There are 4 more keystrokes sent after the one we matched against,
                # so we flush out that buffer before proceeding:
                [rlist[0].read(16) for i in range(4)]
                scan_complete = True
            if scan_complete:
                barcode = parse_scanner_data(scanner_data)
                print "Scanned barcode '{0}'".format(barcode)
                break

#Definition for camera operation

def cam_meth(channel):
    print "Cameras"
    GPIO.output(11, True)
    GPIO.output(12, True)
    GPIO.output(15, True)
    GPIO.output(16, True)
    GPIO.output(21, True)
    GPIO.output(22, True)
    
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(12, True)
    cmd = "raspistill -o " + cam_path + "top.jpg"
    os.system(cmd)
    
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(12, True)
    cmd = "raspistill -o " + cam_path + "mid.jpg"
    os.system(cmd)
    
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(12, False)
    cmd = "raspistill -o " + cam_path + "low.jpg"
    os.system(cmd)
    
    GPIO.output(11, False)
    GPIO.output(12, False)
    GPIO.output(15, False)
    GPIO.output(16, False)
    GPIO.output(21, False)
    GPIO.output(22, False)
    
#Definition for camera capture operation
def capture(cam):
    cmd = "raspistill -o " + cam_path + cam + ".jpg"
    os.system(cmd)
 
raw_input("Press Enter when ready\n>")

# when a falling edge is detected on port 23, regardless of whatever 
# else is happening in the program, the function cam_meth will be run
GPIO.add_event_detect(23, GPIO.RISING, callback=cam_meth, bouncetime=200)

# when a rising edge is detected on port 23, regardless of whatever 
# else is happening in the program, the function upc_meth will be run
# 'bouncetime=300' includes the bounce control written into interrupts2a.py
GPIO.add_event_detect(24, GPIO.FALLING, callback=upc_meth, bouncetime=200)

while(True):
    pass
     
GPIO.cleanup() 
