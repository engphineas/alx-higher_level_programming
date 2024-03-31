#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL and displays the
body of the response using requests.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Script takes in a URL, sends a request to the URL and displays the
    body of the response using requests.
    """
    url = argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
