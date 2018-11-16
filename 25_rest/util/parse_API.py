import urllib.request
import json

def kind():
    data={}
    with open("dataset.json", "r") as read_file:
        data = json.load(read_file)
    return data["kind"]

def items():
    data={}
    with open("dataset.json", "r") as read_file:
        data = json.load(read_file)
    return data["items"]

#Can add a bunch of other things after refering to data
