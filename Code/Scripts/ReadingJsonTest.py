import json

with open('../data/extendedTweetCompletionData.json', 'r') as infile:
    data = json.load(infile)
    print(data.split("\n")[0]['created_at'])
