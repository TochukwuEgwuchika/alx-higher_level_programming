#!/usr/bin/python3
"""
Contains save_to_json_file function
"""

import json

def save_to_json_file(my_obj, filename):
    """ saves an object to json file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
