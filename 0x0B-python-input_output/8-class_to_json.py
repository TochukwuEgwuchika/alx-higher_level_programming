#!/usr/bin/python3
"""
Function to convert object to dictionary
"""

def class_to_json(obj):
    """Return the dictionary description of an object"""
    return obj.__dict__
