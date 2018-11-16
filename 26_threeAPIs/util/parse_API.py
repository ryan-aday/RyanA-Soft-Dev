import urllib.request
import json

def image_XKCD():
    data={}

    with open("data_xkcd.json", "r") as read_file:
        data = json.load(read_file)
    return data["img"]

def imageWeather():
    data={}

    with open("data_weather.json", "r") as read_file:
        data = json.load(read_file)
    return data['query']['results']['channel']['link']


def imageDog():
    data={}

    with open("data_dog.json", "r") as read_file:
        data = json.load(read_file)
    print(data["status"])
    return data["message"]
