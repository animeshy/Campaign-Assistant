#Classifer Imports
import sys
sys.setrecursionlimit(5000)
import time
import re
import nltk
from sklearn.externals import joblib
import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# for people who do not have this kivy-gargen env
# from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from kivy.uix.button import Label
from kivy.uix.widget import Widget
import matplotlib.pyplot as plt

# You can create your kv code in the Python file
Builder.load_file("campaigngui.kv")

# Create a class for all screens in which you can include
# helpful methods specific to that screen

#Plot global cordinates
plt.plot([1, 23, 2, 4])
plt.ylabel('Popularity(%)')
plt.xlabel('Timeline(days)')

class WelcomeScreen(Screen):
    def welcome(self):
        pass

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
    def basicgraph(self):
        # boxlayout2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # boxlayout2.add_widget(FigureCanvasTkAgg(plt.gcf()))
        pass


class ScreenThree(Screen):
    def summary(self):
        pass

class ScreenFour(Screen):
    def help(self):
        pass

class ScreenFive(Screen):
    def support(self):
        pass

class ScreenSix(Screen):
    def sortingTwoLists(self,listkey,listvalue):
        keylen = len(listkey)
        valuelen = len(listvalue)
        for i in range(0,keylen-1):
            for j in range(0,valuelen-i-1):
                if listkey[j] > listkey[j+1]:
                    listkey[j],listkey[j+1] = listkey[j+1],listkey[j]
                    listvalue[j],listvalue[j+1] = listvalue[j+1],listvalue[j]
        return listkey,listvalue

    def freq(self):
        data = """"""
        data = ScreenOne().preprocessTweets(data)
        words = data.split(" ")
        unique_words = set(words)
        no_of_words = len(unique_words)
        word_freq = []*len(unique_words)
        for i in range(0,no_of_words):
            word_freq[i] = words.count(unique_words[i])
        print(word_freq)

    def showFrequency(self):
        pass


# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
welcome1 = WelcomeScreen(name="welcome_screen")
boxlayout = BoxLayout()
welcome1.add_widget(boxlayout)

screen1 = ScreenOne(name="screen_one")
boxlayout = BoxLayout()
screen1.add_widget(boxlayout)

screen2 = ScreenTwo(name="screen_two")
boxlayout2 = BoxLayout()
screen2.add_widget(boxlayout2)

screen3 = ScreenThree(name="screen_three")
boxlayout3 = BoxLayout()
screen3.add_widget(boxlayout3)

screen4 = ScreenFour(name="screen_four")
boxlayout4 = BoxLayout()
screen4.add_widget(boxlayout4)

screen5 = ScreenFive(name="screen_five")
boxlayout5 = BoxLayout()
screen5.add_widget(boxlayout5)

frequencyScreen = ScreenSix(name="frequency_screen")
boxlayout6 = BoxLayout()
frequencyScreen.add_widget(boxlayout6)


screen_manager.add_widget(welcome1)
screen_manager.add_widget(screen1)
screen_manager.add_widget(screen2)
screen_manager.add_widget(screen3)
screen_manager.add_widget(screen4)
screen_manager.add_widget(screen5)
screen_manager.add_widget(frequencyScreen)

class CampaignGUIApp(App):
    def build(self):
        return screen_manager

sample_app = CampaignGUIApp()
sample_app.run()