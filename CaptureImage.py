import test
import cv2
import numpy

def CaptureImage():
    filename = 'capture.jpg'
    print(filename)
    camera_capture = False
    while camera_capture==False:
        camera_capture = test.get_image()
        img = cv2.imread('capture.jpg',0)
    cv2.imwrite(filename,frame)
#        cv2.imshow('image',CaptureImage)
#        return img
    
CaptureImage()