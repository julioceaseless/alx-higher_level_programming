#!/usr/bin/python3
"""
Script takes in a URL and an email address, sends a POST request to the
passed URL with the email as a paramater, and diplays the body of the
response
"""
import requests
import sys

if __name__ == "__main__":
    """ execute script only when run directly"""
    url = sys.argv[1]
    email_addr = sys.argv[2]

    data = {"email": email_addr}
    response = requests.post(url, data=data)
    print(response.text)
