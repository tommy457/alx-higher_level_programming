#!/usr/bin/python3
"""
cript that takes your GitHub credentials
and uses the GitHub API to display your id.
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = f"https://api.github.com/users/{argv[1]}"
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": f"Bearer {argv[2]}",
               "X-GitHub-Api-Version": "2022-11-28"
               }
    req = requests.get(url=url, headers=headers)
    print(req.json().get("id"))
