#!/usr/bin/python3
"""
Has the write_file function
"""

def write_file(filename="", text=""):
    """takes in a text and writes the text to a file(UTF8)"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
