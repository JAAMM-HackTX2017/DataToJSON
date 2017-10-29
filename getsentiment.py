# -*- coding: utf-8 -*-

import httplib, urllib
import json

accessKey = '6067bebac38e41f8a603221788faa59f'

url = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/keyPhrases'

url2 = 'westcentralus.api.cognitive.microsoft.com'
path2 = '/text/analytics/v2.0/sentiment'


# def GetKeyPhrases(documents):
#    headers = {'Ocp-Apim-Subscription-Key': accessKey}
#    conn = httplib.HTTPSConnection (url)
#    body = json.dumps (documents)
#    conn.request ("POST", path, body, headers)
#    response = conn.getresponse ()
#    return response.read ()


def GetSentiments(messages):
    documents = {'documents': []}
    i = 0
    for message in messages:
        documents['documents'].append({'id': i, 'language': 'en', 'text': message})
        i += 1
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection(url2)
    body = json.dumps(documents)
    conn.request("POST", path, body, headers)
    response = conn.getresponse()
    return response.read()


documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': 'My house flooded'},
    { 'id': '2', 'language': 'en', 'text': 'I need help'},
    { 'id': '3', 'language': 'en', 'text': 'my family needs help in the downtown Houston area'}
]}


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