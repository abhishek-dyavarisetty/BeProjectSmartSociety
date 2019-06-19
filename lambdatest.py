import urllib
from urllib.request import urlopen

response = urlopen('https://tough-pug-86.localtunnel.me/faces')
data = response.read().decode("utf-8")
print(data)
if(data == "Not Found"):
    print("sucess")
else:
    print("bad")