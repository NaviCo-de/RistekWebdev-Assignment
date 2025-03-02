#Utils app utama
import os
import json

JSON_FILE = os.path.join(os.path.dirname(__file__), '../data.json')

def read_json():
    with open(JSON_FILE, 'r') as file:
        return json.load(file)

def write_json(data):
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=4)