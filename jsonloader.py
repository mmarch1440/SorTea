import os
import json

def loadFromJson(path):
    with open(path, "r") as jsonfile:
        return json.load(jsonfile)