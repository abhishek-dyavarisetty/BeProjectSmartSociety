import numpy
import urllib
from subprocess import call, Popen, PIPE
import json
import shutil
#import CaptureImage
#import cv2


def describe_face_image():
    cmd = Popen(["bash", "detect-faces.sh", 'capture.jpg'], stdout=PIPE)
    
    data = ""
    for line in cmd.stdout:
#while cmd.stdout != None:
        data += line.decode("utf-8")
        data += cmd.stdout.readline().decode("utf-8")
    print(data)
#data = data.decode("utf-8")
#print(data)
    data = data.replace("'", '"')
    print(data)
    
    data = json.loads(data)
    print(data)
    if len(data["FaceDetails"]) == 0:
        return []
    else:
        gender = data["FaceDetails"][0]["Gender"]["Value"] # Male or Female
        emotion = data["FaceDetails"][0]["Emotions"][0]["Type"] # CALM, etc.
        return [gender, emotion]

def identify_face_image():
    cmd = Popen(["bash", "match-faces.sh", 'capture.jpg'], stdout=PIPE)
    
#output = ""
#for line in cmd.stdout:
#    output += line
    data = ""
    for line in cmd.stdout:
#while cmd.stdout != None:
        data += line.decode("utf-8")
        data += cmd.stdout.readline().decode("utf-8")
    print(data)
#data = data.decode("utf-8")
#print(data)
    data = data.replace("'", '"')
    print(data)

# Typical Return Value
#{
#    "SearchedFaceBoundingBox": {
#        "Width": 0.2554086446762085, 
#        "Top": 0.1308760643005371, 
#        "Left": 0.3861177861690521, 
#        "Height": 0.4540598392486572
#    }, 
#    "SearchedFaceConfidence": 99.9906005859375, 
#    "FaceMatches": [
#        {
#            "Face": {
#                "BoundingBox": {
#                    "Width": 0.4717549979686737, 
#                    "Top": 0.16526399552822113, 
#                    "Left": 0.234375, 
#                    "Height": 0.4717549979686737
#                }, 
#                "FaceId": "b1e93a17-05c7-5b54-b41a-552b5c50c146", 
#                "ExternalImageId": "lukas.png", 
#                "Confidence": 99.99960327148438, 
#                "ImageId": "b440ba40-6664-5448-86c6-52a905843b42"
#            }, 
#            "Similarity": 86.0721206665039
#        }
#    ]
#}

#    try:
    data = json.loads(data)
    print(data)
#    except ValueError as e:
#        return None
    
    if len(data["FaceMatches"]) == 0:
        return None
    
    elif data["FaceMatches"][0]["Similarity"]>=80:
        return data["FaceMatches"][0]["Face"]["ExternalImageId"].split(".")[0]
    
    else:
        return None
    
def face_camera():
    Popen(["bash", "image.sh"], stdout=PIPE)
#    CaptureImage.CaptureImage()
#    file = 'capture.jpg'
    person = identify_face_image()
#    data = describe_face_image()
    if person:
#        return [person, data[0], data[1]]
        return [person]
    
    else:
        return None