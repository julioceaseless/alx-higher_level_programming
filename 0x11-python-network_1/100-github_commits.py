#!/usr/bin/python3
""" retrieve commits from github"""
import requests
import sys


if __name__ == "__main__":
    """execute script only when run directly"""
    repos = sys.argv[1]
    owner = sys.argv[2]
    count = 0

    # api repo for commits
    url = f"https://api.github.com/repos/{owner}/{repos}/commits"

    # my access token
    token = "github_pat_11ABNNLMY0Owfczxfjvkne_EsiJKasx8UpWiVWsy\
    WZkdJmdkQnbO2ZmhwTGwYZ0uAzFCT4F4DBK8c4rRo3"

    # required headers
    headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"}

    # retrieve commits
    res = requests.get(url)

    # create json from commits data
    object_list = res.json()

    # filter sha and committer's name
    for obj in object_list[:10]:
        print("{}: {}".format(obj["sha"], obj["commit"]["author"]["name"]))
