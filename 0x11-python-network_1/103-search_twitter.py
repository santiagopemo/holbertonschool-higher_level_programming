#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge
"""
import requests
import sys
import base64


if __name__ == "__main__":
    # Authentication Token
    c_key = sys.argv[1]
    c_secret = sys.argv[2]
    bearer_token_credentials = "{}:{}".format(c_key, c_secret)
    bearer_token_credentials = bearer_token_credentials.encode("ascii")
    bearer_64 = base64.b64encode(bearer_token_credentials).decode("utf-8")
    url = 'https://api.twitter.com/oauth2/token?grant_type=client_credentials'
    headers = {
        'Authorization': 'Basic {}'.format(bearer_64),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
    r_auth = requests.post(url, headers=headers)
    bearer_token = r_auth.json().get("access_token")
    # Search
    headers = {'Authorization': 'Bearer {}'.format(bearer_token)}
    search_url = 'https://api.twitter.com/1.1/search/tweets.json'
    q = sys.argv[3]
    q_type = 'mixed'
    search_params = {'q': q, 'type': q_type}
    r_search = requests.get(search_url, headers=headers, params=search_params)
    results = r_search.json().get("statuses")
    for i, tweet in enumerate(results):
        if i == 5:
            break
        print("[{}] {} by {}".format(tweet.get("id"), tweet.get("text"),
                                     tweet.get("user").get("name")))
