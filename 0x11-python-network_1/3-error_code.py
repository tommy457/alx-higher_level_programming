#!/usr/bin/python3
"""
Script that fetches an url and prints the body and handel error codes.
"""
from urllib import request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
