import os
import time
import json

def get_dateTime():
    return time.strftime("%Y-%m-%d %H:%M:%S")
def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)
def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
# clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
