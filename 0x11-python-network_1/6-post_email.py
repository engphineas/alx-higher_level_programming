#!/usr/bin/python3
"""
Script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8) using requests.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Script takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the response
    (decoded in utf-8) using requests.
    """
    url = argv[1]
    req = requests.post(url, data={'email': argv[2]})
    print(req.text)
