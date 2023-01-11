#!/bin/bash

# Take the URL as an argument
URL=${1}

# Generate a random temperature between 10 and 40
temperature=$(awk -v min=10 -v max=40 'BEGIN{srand(); print int(min+rand()*(max-min+1))}')

# Generate a random humidity between 50 and 90
humidity=$(awk -v min=50 -v max=90 'BEGIN{srand(); print int(min+rand()*(max-min+1))}')

# construct the JSON payload
payload="{\"temperature\": $temperature, \"humidity\": $humidity}"

echo ${payload}
echo ${URL}

# # send the POST request
curl -H "Content-Type: application/json" -X POST -d "${payload}" ${URL}
