
#request sentiment api
#POST https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment HTTP/1.1
#Host: westcentralus.api.cognitive.microsoft.com
#Content-Type: application/json
#Ocp-Apim-Subscription-Key: 1dab9d779d2a4d67aa1144b1fd298926

#{
#  "documents": [
#    {
#      "language": "string",
#      "id": "string",
#      "text": "string"
#   }
#  ]
#}

# -*- coding: utf-8 -*-

import httplib, urllib
import json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the accessKey string value with your valid access key.
accessKey = '6067bebac38e41f8a603221788faa59f'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your access keys.
# For example, if you obtained your access keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial access keys are generated in the westcentralus region, so if you are using
# a free trial access key, you should not need to change this region.
url = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'

def GetSentiment (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection(url)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse()
    return response.read()

documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': 'i need help' },
    { 'id': '2', 'language': 'en', 'text': 'Mason is cool' }
]}


print 'Please wait a moment for the results to appear.\n'
result = GetSentiment(documents)
#print (json.dumps(json.loads(result), indent=4))
print(result)
