#!/usr/bin/python3
"""To JSON String Module"""
import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
