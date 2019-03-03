
import csv
import json

# objective for the module is to:
# 1.read the tweets stored in json files
# 2.extract time, tweet text, tweet id, favourite count(likes) at that instant
# 3.find unique tweets
# 4.store it in an excel file.

path_to_tweets = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Full Text Tweets\\query narendra modi"


class StageData:

    def __init__(self):
        self.list_of_files = []


    def get_details(self,json_file_path) -> dict:
        """
        Takes a JSON file_path as input
        :return: a dictionary having tweet_id, time, text, likes
        """
        with open(json_file_path) as f:
            file = json.load(f)
        tweet = {}
        tweet['id'] = file['id']
        tweet['created_time'] = file['retweeted_status']['created_at']
        tweet['text'] = file['retweeted_status']['full_text']
        tweet['likes'] = file['retweeted_status']['favorite_count']