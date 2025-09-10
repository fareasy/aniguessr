import json
import os

def get_top2000():
    file_path=os.path.join(os.path.dirname(__file__),"..","data","top2000.json")
    with open(file_path) as json_file:
        return json.load(json_file)