#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the
response header
"""
import requests
import sys


if __name__ == "__main__":
    """run script only when called directly"""
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
