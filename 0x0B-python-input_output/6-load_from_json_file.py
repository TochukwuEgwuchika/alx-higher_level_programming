#!/usr/bin/python3
"""
Contains load_from_json_file function
"""
import json

def load_from_json_file(filename):
    """Loads object from json file"""
    with open(filename,"r") as f:
        return json.load(f)
