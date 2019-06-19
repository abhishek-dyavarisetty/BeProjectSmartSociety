from flask import Flask, send_from_directory
import os
import faceTest as c
import base64
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
@app.route('/faces')
def face_camera():
    data = c.face_camera()
    if data:
        #led
        return data[0]
#        if data != "":
#            if data is None:
#                data[0]=""
#                return ",".join(data)
#        else:
#            return "Not Found"
    else:
        return "Not Found"
    
@app.route('/led')
def abc():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24,GPIO.OUT )
    print ("LED on")
    GPIO.output(24,GPIO.HIGH)
    time.sleep(10)
    GPIO.output(24,GPIO.LOW)
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)