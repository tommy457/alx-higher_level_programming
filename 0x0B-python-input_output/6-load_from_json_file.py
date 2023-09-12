#!/usr/bin/python3
"""Module for load_from_json_file method"""

import json


def load_from_json_file(filename):
    """Method that creates an Object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
