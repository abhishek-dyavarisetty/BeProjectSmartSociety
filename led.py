import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT )
print ("LED on")
GPIO.output(24,GPIO.HIGH)
time.sleep(3)
GPIO.output(24,GPIO.LOW)
