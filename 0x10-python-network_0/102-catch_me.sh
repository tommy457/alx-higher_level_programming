#!/bin/bash
# Respond with a message containing You got me!, in the body of the response.
curl -sLX PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
