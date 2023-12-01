#!/usr/bin/python3
import requests
from sys import argv
"""
Script that fetches a URL and prints value of the X-Request-Id.
"""
if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url).headers

    print(req["X-Request-Id"])
