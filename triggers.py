#!/usr/bin/env python

#Import for GPIO usage
import RPi.GPIO as GPIO
#Import for system and command line usage
import cam
import upc

def main():
    upc.main()
    cam.main()
    GPIO.cleanup()

if __name__ == "__main__":
    main()
