#!/usr/bin/env python
# include RPi libraries in to Python code
import RPi.GPIO as GPIO
import time
#import cam
#import upc

# instantiate GPIO as an object
##GPIO.setmode(GPIO.BOARD)

# define GPIO pins with variables a_pin and b_pin
a_pin = 35
b_pin = 37

# create discharge function for reading capacitor data
def discharge():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.001)

# create time function for capturing analog count value
def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    count = 0
    GPIO.output(a_pin, True)
    while not GPIO.input(b_pin):
        count = count + 1
    return count

# create analog read function for reading charging and discharging data
def analog_read():
    discharge()
#    print charge_time()
    return charge_time()
    
if __name__ == "__main__":
#add a while loop here to test this alone
#    while True :
        analog_read()
