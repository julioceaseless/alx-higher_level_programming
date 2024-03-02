#!/usr/bin/python3
"""
script uses requests module to fetch https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    """execute script only when called directly"""
    res = requests.get("https://alx-intranet.hbtn.io/status")
    body = res.text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
