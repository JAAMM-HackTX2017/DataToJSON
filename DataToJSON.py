import json


import httplib
import json

accessKey = '6067bebac38e41f8a603221788faa59f'

url = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/keyPhrases'

url2 = 'westcentralus.api.cognitive.microsoft.com'
path2 = '/text/analytics/v2.0/sentiment'


def intensity(message):
    return len(message)


def getquad(x, y):
    roundedTo = quadrantSize / 2.0
    return round(x / roundedTo) * roundedTo, round(y / roundedTo) * roundedTo


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


jsonF = open("../../JAAMM-Twitter_Retrieve/posts.json")
datastore = json.load(jsonF)

regionSize = int(datastore["region-size"])
quadrantSize = int(datastore["quadrant-size"])
size = int(datastore["size"])

maxVal = 0

heatData = {}

messages = []
for i in range(0, size):
    data = datastore[str(i)]
    rawx = data[0]
    rawy = data[1]
    loc = getquad(rawx, rawy)
    x = loc[0]
    y = loc[1]
    messages.append(data[2])
sentiments = GetSentiments(messages)
print(sentiments)
"""value = intensity(data[2])
    if value > maxVal:
        maxVal = value
    if (x, y) not in heatData:
        heatData[(x, y)] = 0
    heatData[(x, y)] += value
outputData = []
for key in heatData:
    outputData.append({"x": key[0], "y": key[1], "value": heatData[key]})
rawout = {"max": maxVal, "data": outputData}
outputfile = open("data.json", "w")
json.dump(rawout, outputfile)"""
