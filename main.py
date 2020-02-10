#!/usr/bin/python

# import depending packages
import json
import requests

# Ofcourse, no application is complete without Hello, world!
print ('Hello, world!')

# The page which provides our remote IP information
requestUrl = 'http://ipinfo.io'

# Fire the request
r = requests.get(requestUrl)

# Get the JSON date and parse it
data = json.loads(r.text)

# Print the Remote IP fetched from the page
print ('Your IP address is: ') + data['ip']

# End
print ('You succesfully ran this script!')
