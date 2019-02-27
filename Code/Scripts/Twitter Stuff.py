
import tweepy

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "ZkueGAecI0y6rrbwbPrN3KcRg"
consumer_secret = "VN5O8rcKYmCF6SSFNZtU3QkxH1l47vrU4I3uaWc6Cdnub2XhIB"
access_key = "1046326010713714688-JNIZx8CXJbErXnRaEiblSF1mctEKP8"
access_secret = "BGgxzDGQpoHhEWFN13HpPqrpPO24GPmuFtb16an7OYoCk"

# Function to extract tweets
def get_tweets(username):

        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)

        # Calling api
        api = tweepy.API(auth)

        # 200 tweets to be extracted
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)

        # Empty Array
        tmp=[]

        # create array of tweet information: username,
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
        for j in tweets_for_csv:

            # Appending tweets to the empty array tmp
            tmp.append(j)

        # Printing the tweets
        for element in tmp:
            print(element)


# Driver code
if __name__ == '__main__':

    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("@narendramodi")
