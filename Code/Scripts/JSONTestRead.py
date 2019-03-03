import json
from pprint import pprint
import os

path_to_tweets = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Full Text Tweets\\query narendra modi"
files = os.listdir(path_to_tweets)
print(files[0])
files[0] = path_to_tweets+"\\"+files[0]
with open(files[0]) as f:
    file = json.load(f)
pprint(file['retweeted_status']['favorite_count'])