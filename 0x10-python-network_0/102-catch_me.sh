#!/bin/bash
# script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -sL -X PUT -H "Origin: School" --data "user_id=98" $1
