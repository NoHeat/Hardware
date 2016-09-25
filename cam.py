#!/usr/bin/env python

#Import for GPIO usage
import RPi.GPIO as GPIO
import os
import sys

#Definition for camera operation

def main():
    print "Cameras"
    # cam_path = "/home/pi/Desktop/capture_"
    cam_path = "/root/Desktop/capture_"
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)

    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)

    GPIO.output(11, True)
    GPIO.output(12, True)
    GPIO.output(15, True)
    GPIO.output(16, True)
    GPIO.output(21, True)
    GPIO.output(22, True)
    
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(12, True)
    cmd1 = "raspistill -o " + cam_path + "top.jpg"
    print cmd1
    os.system(cmd1)
    
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(12, True)
    cmd2 = "raspistill -o " + cam_path + "mid.jpg"
    print cmd2
    os.system(cmd2)
    
##    GPIO.setmode(GPIO.BOARD)
##    GPIO.setup(7, GPIO.OUT)
##    GPIO.setup(11, GPIO.OUT)
##    GPIO.setup(12, GPIO.OUT)
##    
##    GPIO.output(7, False)
##    GPIO.output(11, True)
##    GPIO.output(12, False)
##    cmd3 = "raspistill -o " + cam_path + "low.jpg"
##    print cmd3
##    os.system(cmd3)
    
    GPIO.cleanup()
    
if __name__ == "__main__":
    main()
