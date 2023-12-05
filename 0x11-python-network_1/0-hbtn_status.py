#!/usr/bin/python3
"""
Script that fetches an url and prints the body.
"""
import urllib.request


with urllib.request.urlopen("https://intranet.alxswe.com/status") as response:
    res = response.read()
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
    print(f"\t- utf8 content: {res.decode('utf-8')}")
