import numpy
import urllib
from subprocess import call, Popen, PIPE
import json
import shutil
import cv2

cmd = Popen(["bash", "match-faces.sh", 'capture.jpg'], stdout=PIPE)
    
#output = ""
#for line in cmd.stdout:
#    output += line
print (cmd.stdout)
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
#        return "error generated"
    
if len(data["FaceMatches"]) == 0:
    print("Not Found")
    
elif data["FaceMatches"][0]["Similarity"]>=80:
    print(data["FaceMatches"][0]["Face"]["ExternalImageId"].split(".")[0])
    
else:
    print("some thing is wrong")
