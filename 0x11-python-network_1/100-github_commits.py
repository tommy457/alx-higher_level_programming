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
    req = requests.get(url)
    commits = req.json()[:10]

    for commit in commits:
        sha = commits.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author_name))
