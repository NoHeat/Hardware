import RPi.GPIO as GPIO
import os

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(True):
    print GPIO.input(11)
