#!/bin/bash
# script takes in a URL and displays all HTTP methods the server will accept
curl -sI $1 | grep -oP "Allow: (.*)$" | cut -c8-
