#!/usr/bin/python3
"""
script sends request to the url provided in the command line
and displays the body of the response(decoded in UTF-8)
"""
import urllib.request
import urllib.parse
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.URLError as exception:
        print(f"Error code: {exception.code}")
