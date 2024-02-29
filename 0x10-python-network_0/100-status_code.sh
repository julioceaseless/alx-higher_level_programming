#!/bin/bash
# script sends a request to URL passed as arguent and displays the status code of response
curl -s -o /dev/null -w "%{http_code}" 1$

