import json

import http.client
import json

accessKey = '6067bebac38e41f8a603221788faa59f'

url = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'

messageSentimacy = {}


def intensity(message):
    return messageSentimacy[message]


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
    conn = http.client.HTTPSConnection(url)
    body = json.dumps(documents)
    conn.request("POST", path, body, headers)
    response = conn.getresponse()
    return response.read()


jsonF = open("../../JAAMM-Twitter_Retrieval/posts.json")
datastore = json.load(jsonF)

regionSize = int(datastore["region-size"])
quadrantSize = int(datastore["quadrant-size"])
size = int(datastore["size"])

maxVal = 0

heatData = {}

messages = []
for i in range(0, size):
    messages.append(datastore[str(i)][0])
sentiments = json.loads(GetSentiments(messages))["documents"]
for sentiment in sentiments:
    score = sentiment["score"]
    if score > 0.5:
        score = 0
    elif score > 0.25:
        score = 1
    elif score > 0.125:
        score = 3
    elif score > 0.0625:
        score = 5
    elif score > 0.03125:
        score = 7
    else:
        score = 10
    message = datastore[sentiment["id"]][0]
    messageSentimacy[message] = score
for i in range(0, size):
    data = datastore[str(i)]
    rawx = data[1][0]
    rawy = data[1][1]
    loc = getquad(rawx, rawy)
    x = loc[0]
    y = loc[1]
    value = intensity(data[0])
    if value > maxVal:
        maxVal = value
    if (x, y) not in heatData:
        heatData[(x, y)] = 0
    heatData[(x, y)] += value
outputData = []
for key in heatData:
    outputData.append({"lat": key[0], "lng": -key[1], "value": heatData[key]})
rawout = {"max": maxVal, "data": outputData}
outputfile = open("data.json", "w")
json.dump(rawout, outputfile)
