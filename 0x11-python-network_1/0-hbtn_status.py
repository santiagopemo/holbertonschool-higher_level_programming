#!/usr/bin/python3
"""hbtn status module"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html.__str__()))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))