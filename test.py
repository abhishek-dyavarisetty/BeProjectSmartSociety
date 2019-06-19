import cv2

def get_image():
    cam = cv2.VideoCapture(0)
    img,frame = cam.read()
    del(cam)
    return frame
