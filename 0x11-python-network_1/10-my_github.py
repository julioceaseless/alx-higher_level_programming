#!/usr/bin/python3
"""
script takes Github credentials(username and password) and uses the
GitHub Api to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sysy


if __name__ == "__main__":
    """execute code only when run directly"""
    username = sys.argv[1]
    password = sys.argv[2]
    headers = {"Authorization": 'token'}
    res = requests.get("https://api.github.com/user",
                       auth=HTTPBasicAuth(username, password))
    id_json = res.json().get("id")
    print(id_json)
