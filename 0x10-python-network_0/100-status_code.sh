#!/bin/bash
# displays the status code of response
curl -s -o /dev/null -w "%{http_code}" 1$

