#!/bin/bash

# Fetch the METAR data and save it to a JSON file
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json

# Parse the data with jq to extract the receiptTime values and limit to the first 6
jq -r '.[].receiptTime' aviation.json | head -n 6

