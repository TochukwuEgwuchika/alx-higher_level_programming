#!/bin/usr/python3
"""
Contains from_json_string function
"""
import json

def from_json_string(my_str):
    """Converts a string to object"""
    return json.loads(my_str)
