#!/usr/bin/python3
"""
Script that takes in a url, sends a request and show the value of the
X-Request-Id variable found in the header of the reponse h
"""
import urllib.request
import sys


if __name__ == "__main__":
    """ run only when called directly"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
