#!/bin/bash
# curl command to display the size of the body of the response

curl -so /dev/null $1$ -w '%{size_download}\n'
