#Classifer Imports
import sys
import time
import re
import nltk
from sklearn.externals import joblib
import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Label

# You can create your kv code in the Python file
Builder.load_file("kivytut2.kv")

# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(Screen):
    # Testing input
    # def animesh(self, testingstring):
    #     self.display.text = "success"

    # Processing Tweets
    def preprocessTweets(self, tweet):

        # Convert www.* or https?://* to URL
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)

        # Convert @username to __HANDLE
        tweet = re.sub('@[^\s]+', '__HANDLE', tweet)

        # Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

        # trim
        tweet = tweet.strip('\'"')

        # Repeating words like happyyyyyyyy
        rpt_regex = re.compile(r"(.)\1{1,}", re.IGNORECASE)
        tweet = rpt_regex.sub(r"\1\1", tweet)

        # Emoticons
        emoticons = \
            [
                ('__positive__', [':-)', ':)', '(:', '(-:', \
                                  ':-D', ':D', 'X-D', 'XD', 'xD', \
                                  '<3', ':\*', ';-)', ';)', ';-D', ';D', '(;', '(-;', ]), \
                ('__negative__', [':-(', ':(', '(:', '(-:', ':,(', \
                                  ':\'(', ':"(', ':((', ]), \
                ]

        def replace_parenth(arr):
            return [text.replace(')', '[)}\]]').replace('(', '[({\[]') for text in arr]

        def regex_join(arr):
            return '(' + '|'.join(arr) + ')'

        emoticons_regex = [(repl, re.compile(regex_join(replace_parenth(regx)))) \
                           for (repl, regx) in emoticons]

        for (repl, regx) in emoticons_regex:
            tweet = re.sub(regx, ' ' + repl + ' ', tweet)

        # Convert to lower case
        tweet = tweet.lower()

        return tweet

    # Stemming of Tweets
    def stem(self, tweet):
        stemmer = nltk.stem.PorterStemmer()
        tweet_stem = ''
        words = [word if (word[0:2] == '__') else word.lower() \
                 for word in tweet.split() \
                 if len(word) >= 3]
        words = [stemmer.stem(w) for w in words]
        tweet_stem = ' '.join(words)
        return tweet_stem

    def predict(self, tweet):
        classifier = joblib.load('svmClassifierTest.pkl')
        tweet_processed = self.stem(self.preprocessTweets(tweet))
        X = [tweet_processed]
        sentiment = classifier.predict(X)
        self.display2.text = str(sentiment)


class ScreenTwo(Screen):
    def testcloud(self):
        pass


# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen1 = ScreenOne(name="screen_one")
gridlayout = GridLayout()
screen1.add_widget(gridlayout)
screen_manager.add_widget(screen1)

screen2 = ScreenTwo(name="screen_two")
gridlayout2 = GridLayout()
screen2.add_widget(gridlayout2)
screen_manager.add_widget(screen2)


class KivyTut2App(App):

    def build(self):
        return screen_manager

sample_app = KivyTut2App()
sample_app.run()
