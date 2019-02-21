# algo:
# get the row number
# open the file in rw
# Create a window
# add 3 buttons, positive, negative, exit
# loop:
#   add the text from the row
#   based on the button click, store a value of 0 or 1 in right column
from tkinter import *
import xlrd
import xlwt
import os


# change the no_of_tweets to the number of tweets present in the reading file
class LabelTweet:
    def __init__(self):
        self.no_of_tweets = 10
        self.result = 0
        # input your path directly in the file variable
        os.chdir("../data")
        # accepts only xls files
        self.file = "TO_Label_Modi_1_to_8.xlsx"
        self.data = xlrd.open_workbook(self.file)
        self.row_number = 0
        self.labelling_column = 2
        self.text_column = 1
        self.window = None
        # accepts only xls files
        self.output_file = "Label_Modi_1_to_8.xlsx"
        self.workbook = xlwt.Workbook()
        self.worksheet = self.workbook.add_sheet('Labelled Tweets')
        self.tweets = []

    def markPositive(self):
        print("Marked Positive")
        self.result = 1
        self.window.quit()
        self.window.destroy()

    def markNegative(self):
        print("Marked Negative")
        self.result = -1
        self.window.quit()
        self.window.destroy()

    def skip(self):
        print("Skipped")
        self.result = 0
        self.window.quit()
        self.window.destroy()

    def formatTweet(self, tweet):
        formatted_tweet = ""
        for letter in tweet:
            if ord(letter) in range(65536):
                formatted_tweet += letter
        return formatted_tweet

    def getTweets(self):
        sheet = self.data.sheet_by_index(0)
        self.tweets = []
        for i in range(0, self.no_of_tweets):
            try:
                tweet = sheet.cell_value(self.row_number, self.text_column)
            except:
                tweet = "None"
            finally:
                self.tweets.append(self.formatTweet(tweet))
                self.row_number += 1
        self.row_number = 0
        # for tweet in self.tweets:
        #     print(tweet)

    def labelTweet(self):
        for i in range(self.no_of_tweets):
            self.window = Tk()
            tweet = self.tweets[i]
            message = Message(self.window, text=tweet)
            message.pack()
            # positive button
            positive_button = Button(text='positive', command=self.markPositive)
            positive_button.pack(side=LEFT, padx='20', pady="20")
            # negative button
            negative_button = Button(text='negative', command=self.markNegative)
            negative_button.pack(side=LEFT, padx='20', pady="20")
            # exit button
            next_button = Button(text="Skip", command=self.skip)
            next_button.pack(side=LEFT, padx='20', pady="20")
            # run the dialog
            mainloop()
            self.worksheet.write(self.row_number, 0, self.row_number)
            self.worksheet.write(self.row_number, 1, tweet)
            self.worksheet.write(self.row_number, 2, self.result)
            print(self.row_number, " tweet written")
            self.row_number += 1
            self.window = None
        self.workbook.save(self.output_file)


if __name__ == "__main__":
    obj = LabelTweet()
    obj.getTweets()
    obj.labelTweet()
