#!/usr/bin/python3
import requests
"""
Script that fetches a URL.
"""

url = "https://alx-intranet.hbtn.io/status"
req = requests.get(url).text

print("Body response:\n\t- type: {}\n\t- content: {}".format(type(req), req))
