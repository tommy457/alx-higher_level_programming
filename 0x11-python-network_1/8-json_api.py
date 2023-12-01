#!/usr/bin/python3
"""
Script that sends a request to the URL with the letter as a parameter
and displays the body of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": ""}

    if len(argv) > 1:
        data["q"] = argv[1]

    req = requests.post(url, data=data)
    res_dict = req.json()

    if (res_dict == {}):
        print("No result")

    elif (req.headers.get('content-type')) != 'application/json':
        print("Not a valid JSON")

    else:
        print("[{}] {}".format(res_dict.get("id"), res_dict.get("name")))
