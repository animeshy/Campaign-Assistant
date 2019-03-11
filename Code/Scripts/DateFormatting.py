# module to format the tweet time Thu Feb 28 14:51:59 +0000 2019
# converting that day to 28, month to 2, hour 14 and min 51
import csv

def format_date_string(date_str):
    """
    :param date_str: expects the format Thu Feb 28 14:51:59 +0000 2019
    :return: a dictionary containing day,month,hour,min
    """
    # month_val represents the month value
    month_val = {
        'Jan':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
    }
    time = date_str.split(" ")[3]
    time = time.split(":")
    date = date_str.split(" ")
    # date[1] is month and date[2] is day of the month
    # print(date)
    date = [date[1],date[2]]
    day = int(date[1])
    month = month_val[date[0]]
    hour = int(time[0])
    minutes = int(time[1])
    time = {}
    time['day'] = day
    time['month'] = month
    time['hour'] = hour
    time['min'] = minutes
    return time


if __name__ == '__main__':
    # time = format_date_string('Thu Feb 28 14:51:59 +0000 2019')
    # print(time)
    # read file
    # format date
    # write file
    input_file = 'D:\\Users\\yashk\\Campaign-Assistant\\Data\\Unique Full Text Tweets\\preprocessed rahul gandhi.csv'
    output_file = 'D:\\Users\\yashk\\Campaign-Assistant\\Data\\Unique Full Text Tweets\\formated preprocessed rahul gandhi.csv'
    tweets = []
    with open(input_file,mode='r') as in_file:
        file_reader = csv.reader(in_file)
        for tweet in file_reader:
            formatted_tweet = {}
            formatted_tweet['id'] = tweet[0]
            formatted_tweet['time'] = tweet[1]
            formatted_tweet['text'] = tweet[2]
            try:
                time = format_date_string(tweet[1])
                formatted_tweet['day'] = time['day']
                formatted_tweet['month'] = time['month']
                formatted_tweet['hour'] = time['hour']
                formatted_tweet['min'] = time['min']
                tweets.append(formatted_tweet)
            except:
                continue
    with open(output_file,mode='w',newline='') as out_file:
        file_writer = csv.DictWriter(out_file,tweets[0].keys())
        file_writer.writeheader()
        file_writer.writerows(tweets)
