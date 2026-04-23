import json
import os

FILE_PATH = "data/storage.json"

def load_data():
    if not os.path.exists(FILE_PATH):
        return []
    
    try:
        with open(FILE_PATH, "r") as file:
            content = file.read().strip()

            if content == "":
                return []
            return json.loads(content)
        
    except:
        return[]
    
def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)