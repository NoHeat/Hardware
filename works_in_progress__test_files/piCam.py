
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
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

def main():
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(12, True)
    GPIO.output(18, True)
    capture(1)
    GPIO.output(18, False)
    
##    GPIO.output(7, True)
##    GPIO.output(11, False)
##    GPIO.output(12, True)
##    capture(2)
##
##    GPIO.output(7, False)
##    GPIO.output(11, True)
##    GPIO.output(12, False)
##    capture(3)
##    
    GPIO.cleanup()
def capture(cam):
    cmd = "raspistill -o /home/pi/Desktop/capture_%d.jpg" % cam
    os.system(cmd)


    
if __name__ == "__main__":
    main()

    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(12, True)

