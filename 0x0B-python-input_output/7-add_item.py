#!/usr/bin/python3
"""Modul for adding arguments to a Python list, and then save it"""

import sys
import os.path
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    items = load_from_json_file("add_item.json")

items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
