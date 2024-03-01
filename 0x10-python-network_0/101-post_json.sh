#!/bin/bash
# script sends a json POST request and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" --data @$2 $1
