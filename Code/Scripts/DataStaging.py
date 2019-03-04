import csv
import json
import os

# objective for the module is to:
# 1.read the tweets stored in json files
# 2.extract time, tweet text, tweet id, favourite count(likes) at that instant
# 3.find unique tweets
# 4.store it in an excel file.

path_to_tweets = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Full Text Tweets\\query narendra modi"


class StageData:

    def __init__(self):
        self.list_of_files = []

    def get_tweet_file_names(self, path_to_files) -> None:
        """
        To get all the file names of the json files in a directory
        and store it in list_of_files
        :return:None
        """
        self.list_of_files = os.listdir(path_to_files)
        no_of_files = len(self.list_of_files)
        for iterator in range(0, no_of_files):
            self.list_of_files[iterator] = path_to_files + "\\" + self.list_of_files[iterator]

    def read_tweets(self) -> list:
        """
        Takes a JSON file_path as input
        :return: a list of tweets, where each tweet has tweet_id, time, text, likes
        """
        tweets = []
        for input_file_path in self.list_of_files:
            with open(input_file_path) as f:
                file = json.load(f)
            tweet = {'id': file['id']}
            # if it is not a retweet then we can directly get the details
            if tweet['retweeted']:
                tweet['created_time'] = file['created_at']
                tweet['text'] = file['full_text']
                tweet['likes'] = file['favorite_count']
            # else we need to dig down to hte original tweet to get the details.
            else:
                tweet['created_time'] = file['retweeted_status']['created_at']
                tweet['text'] = file['retweeted_status']['full_text']
                tweet['likes'] = file['retweeted_status']['favorite_count']
            tweets.append(tweet)
            tweet = None
        return tweets

    def write_to_file(self, tweets, output_file_path) -> None:
        """
        Function to store all the tweets to a csv file.
        :param tweets: contains the list of tweets, where tweet is a dictionary
        :return: None
        """
        pass

    def get_unique_tweets(self, tweets) -> list:
        """
        Function to remove the redundant tweets in the list
        :param tweets: takes in list of tweets
        :return: returns the unique list of tweets
        """
        no_of_tweets = len(tweets)
        list_of_full_text = []
        for tweet in tweets:
            list_of_full_text.append(tweet['text'])
        for iterator in range(0, no_of_tweets):
            if tweets[iterator]['text'] in list_of_full_text:
                tweets.pop(iterator)
                iterator -= 1
                no_of_tweets -= 1
            else:
                list_of_full_text.append(tweets[iterator]['text'])


objectStageData = StageData()
