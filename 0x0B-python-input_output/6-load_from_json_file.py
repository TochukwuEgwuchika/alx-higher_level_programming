#!/usr/bin/python3
"""
Contains load_from_json_file function
"""
import json

def load_from_json_file(filename):
    """Loads object from json file"""
    with open(filename,"r+"):
        return json.load(filename)
