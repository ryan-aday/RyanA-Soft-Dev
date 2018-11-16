import urllib.request
import json

def image():
    data={}
    with open("dataset.json", "r") as read_file:
        data = json.load(read_file)
    return data["img"]


#Can add a bunch of other things after refering to data
