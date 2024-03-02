#!/usr/bin/python3
"""
This script feches https://intranet.hbtn.io/status using urllib module
"""
import urllib.request


if __name__ == "__main__":
    """ only run when called directly"""

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
