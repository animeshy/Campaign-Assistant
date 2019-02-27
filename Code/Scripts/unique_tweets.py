# read excel
# store tweets in a list
# convert to tuple
# save the list.

import xlrd
import xlwt

file_name = '9-Jan-15-Jan.xls'
workbook = xlrd.open_workbook(file_name)
sheet = workbook.sheet_by_index(0)
no_of_rows = sheet.nrows
tweets =[]

# reading the tweets from excel
for i in range(no_of_rows):
    tweets.append(sheet.cell_value(i,1))
print(tweets[0])
# finding the unique tweets
unique_tweets = set(tweets)
unique_tweets = list(unique_tweets)

# writing the tweets to excel
file_name = 'unique_'+file_name
workbook_ = xlwt.Workbook()
sheet_ = workbook_.add_sheet('test')
no_of_rows = len(unique_tweets)
for i in range(no_of_rows):
    sheet_.write(i,0,i)
    print(i, unique_tweets[i])
    sheet_.write(i,1,unique_tweets[i])
workbook_.save(file_name)
