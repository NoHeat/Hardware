# include RPi libraries in to Python code
import RPi.GPIO as GPIO
import time
import cam
import upc
import sensval

# provide a loop to display analog data count value on the screen
while True:
    if not(sensval.analog_read() == 0):
        upc.main()
        cam.main()
        GPIO.cleanup()
    time.sleep(0.05)
    
