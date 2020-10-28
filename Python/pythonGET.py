#!/bin/env python

import requests
import hashlib
import base64
import time
import hmac

# Account Info
AccessId = '<INSERT-ACCESS-ID>'
AccessKey = '<INSERT-ACCESS-KEY>'
Company = '<INSERT-COMPANY-NAME>'

# Request Info
httpVerb = 'GET'
resourcePath = '/device/devices'
queryParams = ''
data = ''

# Construct URL
url = 'https://' + Company + '.logicmonitor.com/santaba/rest' + resourcePath + queryParams

# Get current time in milliseconds
epoch = str(int(time.time() * 1000))

# Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

# Construct signature
hmac = hmac.new(AccessKey.encode(), msg=requestVars.encode(), digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(hmac.encode())

# Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type': 'application/json', 'Authorization': auth}

# Make request
response = requests.get(url, data=data, headers=headers)

# Print status and body of response
print('Response Status:', response.status_code)
print('Response Body:', response.content)
