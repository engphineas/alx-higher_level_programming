#!/usr/bin/python3
"""Script fetches https://intranet.hbtn.io/status using requests"""
import requests


if __name__ == "__main__":
    """fetch https://intranet.hbtn.io/status using requests"""
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
