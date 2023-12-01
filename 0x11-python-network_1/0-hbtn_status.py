#!/usr/bin/python3
"""
Script that fetches an url and prints the body.
"""
import urllib.request

if __name__ == "__main__":

    url = "https://intranet.alxswe.com/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        body = "Body response:\n\t- type: {}"\
            "\n\t- content: {}\n\t- utf8 content: {}"
        print(body.format(type(html), html, html.decode('utf-8')))
