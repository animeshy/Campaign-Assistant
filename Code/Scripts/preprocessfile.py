import re
import csv


def preprocessTweets(tweet):
    # Convert www.* or https?://* to nothing
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet)

    # Convert @username to __HANDLE
    tweet = re.sub('@[^\s]+', '', tweet)

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

    return tweet.lower()

input_file = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Unique Full Text Tweets\\query rahul gandhi.csv"
output_file = "D:\\Users\\yashk\\Campaign-Assistant\\Data\\Unique Full Text Tweets\\preprocessed rahul gandhi.csv"
with open(input_file, mode='r', newline="") as in_f:
    file_reader = csv.reader(in_f)
    rows = []
    for row in file_reader:
        rows.append(row)
    with open(output_file, mode='w+', newline='') as out_f:
        file_writer = csv.writer(out_f)
        for row in rows:
            file_writer.writerow([row[0],row[1],preprocessTweets(row[2])])