#!/usr/bin/python3
"""
Script that sends a POST request to the passed URLand displays the body of the response.
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    e_data = urllib.parse.urlencode({"email": email}).encode('ascii')

    with urllib.request.urlopen(url, e_data) as response:
        html = response.read()
        print(html.decode('utf-8'))
