#!/usr/bin/python3
"""script fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    """fetches https://intranet.hbtn.io/status"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html_page = response.read()
        html_str = html_page.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(html_page)))
    print("\t- content: {}".format(html_page))
    print("\t- utf8 content: {}".format(html_str))
