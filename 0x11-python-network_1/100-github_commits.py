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
    params = {'per_page': 10}
    r = requests.get(url, params=params)
    for c in r.json():
        print("{}: {}".format(c.get("sha"),
                              c.get("commit").get("author").get("name")))
