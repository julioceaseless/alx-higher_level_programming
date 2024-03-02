#!/usr/bin/python3
"""
Script takes in a letter and sends a POST request to
http://0.0.0.:5000/search_user with the letter as a  parameter
"""
import requests
import sys


if __name__ == "__main__":
    """execute script only when run directly"""
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        print("No result")
        exit(1)

    letter = sys.argv[1]
    my_obj = {"q": letter}
    res = requests.post(url, data=my_obj)
    try:
        res_json = res.json()
    except requests.exceptions.JSONDecodeError as JSONError:
        print("Not a valid JSON")
    else:
        if len(res_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(res_json["id"], res_json["name"]))
