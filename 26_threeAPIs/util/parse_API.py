import urllib.request
import json

def image_XKCD():
    data={}

    with open("data_xkcd.json", "r") as read_file:
        data = json.load(read_file)
    return data["img"]

def imageDog():
    data={}

    with open("data_dog.json", "r") as read_file:
        data = json.load(read_file)
    return data["message"]
