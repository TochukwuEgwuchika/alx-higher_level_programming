#!/usr/bin/python3
"""
Script that adds all argument to a python list and saves the to a file
"""
argv = __import__("sys").argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, filename)
