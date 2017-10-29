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
path = '/text/analytics/v2.0/keyPhrases'

url2 = 'westcentralus.api.cognitive.microsoft.com'
path2 = '/text/analytics/v2.0/sentiment'

def GetKeyPhrases (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (url)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

def GetSentiment (documents):
    "Gets the sentiments for a set of documents and returns the information."
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection(url2)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse()
    return response.read()

documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': 'My house flooded'},
    { 'id': '2', 'language': 'en', 'text': 'I need help'},
    { 'id': '3', 'language': 'en', 'text': 'my family needs help in the downtown Houston area'}
]}

print 'Please wait a moment for the results to appear.\n'

#getphrases gives originally a string, json.loads(x) makes value into a dictionary to be able to iterate through
result = json.loads(GetKeyPhrases(documents))
print "going through 'documents'..."
print json.loads(GetSentiment(documents))

for dictionary in result['documents']:
    for word in dictionary['keyPhrases']:
        print word
        wordDict = {'documents': [
            {'id': '1', 'language': 'en', 'text': word}
        ]}
        res = GetSentiment(wordDict)
        print res

print('finished printing')

print("printing result")
print(result)
#print (json.dumps(json.loads(result), indent=4))
