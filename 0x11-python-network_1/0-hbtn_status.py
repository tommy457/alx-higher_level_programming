#!/usr/bin/python3
"""
Script that fetches an url and prints the body.
"""
import urllib.request


with urllib.request.urlopen("https://intranet.alxswe.com/status") as response:
    html = response.read()
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode('utf-8')}")
