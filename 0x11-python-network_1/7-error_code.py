#!/usr/bin/python3
"""
Script takes in a URL, sends a request to the url and displays the body
of the response
"""
import requests
import sys


if __name__ == "__main__":
    """execute script only when run directly"""
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as error:
        status_code = error.response.status_code
        print(f"Error code: {status_code}")
