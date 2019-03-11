import csv
import json
import os
import re

# objective for the module is to:
# 1.read the tweets stored in json files
# 2.extract time, tweet text, tweet id, favourite count(likes) at that instant
# 3.find unique tweets
# 4.store it in an excel file.

path_to_tweets = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Full Text Tweets\\query narendra modi"
path_to_save = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Unique Full Text Tweets\\query narendra modi.csv"


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
        no_of_tweets = len(self.list_of_files)
        for i in range(0,2000):
            with open(self.list_of_files[i]) as f:
                file = json.load(f)
                print(i)
            tweet = {'id': file['id']}
            try:
                tweet['created_time'] = file['retweeted_status']['created_at']
                tweet['text'] = file['retweeted_status']['full_text']
            except:
                tweet['created_time'] = file['created_at']
                tweet['text'] = file['full_text']
            tweets.append(tweet)
        return tweets

    def write_to_file(self, tweets, output_file_path) -> None:
        """
        Function to store all the tweets to a csv file.
        :param tweets: contains the list of tweets, where tweet is a dictionary
        :return: None
        """
        with open(output_file_path, mode='w',newline='') as csv_file:
            tweet = ['id','created_time','text']
            writer = csv.DictWriter(csv_file, fieldnames=tweet)

            writer.writeheader()
            for tweet in tweets:
                try:
                    writer.writerow(tweet)
                except:
                    pass

    @staticmethod
    def get_unique_tweets(list_of_tweets) -> list:
        """
        Function to remove the redundant tweets in the list
        :param list_of_tweets: takes in list of tweets
        :return: returns the unique list of tweets
        """
        no_of_tweets = len(list_of_tweets)
        unique_list_of_full_text = []
        # for tweet in tweets:
        #     unique_list_of_full_text.append(tweet['text'])
        # unique_list_of_full_text = set(unique_list_of_full_text)
        # unique_list_of_full_text = list(unique_list_of_full_text)
        # print("unique length : ",len(unique_list_of_full_text))
        unique_list_of_tweets = []
        for iterator in range(0, no_of_tweets):
            if list_of_tweets[iterator]['text'] in unique_list_of_full_text:
                # tweets.pop(iterator)
                # iterator -= 1
                # no_of_tweets -= 1
                continue
            else:
                unique_list_of_full_text.append(list_of_tweets[iterator]['text'])
                unique_list_of_tweets.append(list_of_tweets[iterator])
        for text in unique_list_of_full_text:
            print(text)
        return unique_list_of_tweets


# objectStageData = StageData()
# objectStageData.get_tweet_file_names(path_to_tweets)
# tweets = objectStageData.read_tweets()
# unique_tweets = objectStageData.get_unique_tweets(tweets)
# l = len(unique_tweets)
# print(len(unique_tweets))
# for i in range(0, l):
    # print(tweets[i])
# objectStageData.write_to_file(tweets,path_to_save)
full_text = []
with open("D:\\Users\\yashk\\Campaign-Assistant\\Data\\Unique Full Text Tweets\\query rahul gandhi.csv",'r') as file:
    reader = csv.reader(file)
    for tweet in reader:
        full_text.append(tuple([tweet[1],tweet[2]]))
    full_text = set(full_text)
    print(len(full_text))
    full_text = list(full_text)
    number = len(full_text)
    print(full_text[0])
    for i in range(0,number):
        full_text[i] = list(full_text[i])
        full_text[i].append(full_text[i][1])
        full_text[i][1] = full_text[i][0]
        full_text[i][0] = str(1000000+i)
    print(full_text[0])
with open("D:\\Users\\yashk\\Campaign-Assistant\\Data\\Unique Full Text Tweets\\query rahul gandhi.csv",'w',newline='') as file:
    tweet = {}
    writer = csv.DictWriter(file, fieldnames=['id','created_time','text'])
    for text in full_text:
        tweet['id'] = text[0]
        tweet['created_time'] = text[1]
        tweet['text'] = text[2]
        writer.writerow(tweet)
    print(tweet)