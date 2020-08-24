#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    variables = {'email': sys.argv[2]}
    req = urllib.request.Request(url, variables)
    with urllib.request.urlopen(url, variables) as response:
        print(response.read())
