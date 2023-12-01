#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
first argument will be the repository name.
The second argument will be the owner name.
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    req = requests.get(url=url, headers=headers)
    commits = req.json()[:10]

    for idx in range(10):
        sha = commits[idx].get("sha")
        author_name = ((commits[idx].get("commit")).get("author")).get("name")
        print("{}: {}".format(sha, author_name))
