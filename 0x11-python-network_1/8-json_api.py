#!/usr/bin/python3
"""
Script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Script takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
    """
    url = 'http://0.0.0.0:5000/search_user'
    req = requests.get(url)
    if len(argv) == 2:
        req = requests.post(url, data={'q': argv[1]})
    else:
        req = requests.post(url, data={'q': ""})
    try:
        if req.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(req.json().get('id'), req.json().get('name')))
    except:
        print("Not a valid JSON")
