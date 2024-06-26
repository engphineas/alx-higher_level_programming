#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the
response.
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """takes in a URL, sends a request to the URL and displays the
    value of the X-Request-Id variable found in the header of the
    response"""
    with urllib.request.urlopen(argv[1]) as response:
        id_html = response.info().get('X-Request-Id')
        print(id_html)
