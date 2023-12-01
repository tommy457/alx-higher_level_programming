#!/usr/bin/python3
"""
Script that sends a POST request a URL with the email as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    email = argv[2]
    data = {"email": email}

    req = requests.post(url, data=data)
    print(req.text)
