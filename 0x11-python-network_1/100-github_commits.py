#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)
    for i, c in enumerate(r.json()):
        if i == 10:
            break
        print("{}: {}".format(c.get("sha"),
                              c.get("commit").get("author").get("name")))
