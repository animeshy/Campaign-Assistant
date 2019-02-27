import xlrd

file = open("nm.txt", 'r')
list_of_tweets = []

for i in range(10400):
    try:
        list_of_tweets.append(file.readline())
    except:
        pass

file.close()

set_of_tweets = set(list_of_tweets)


# print(len(list_of_tweets))
# print(len(set_of_tweets))


# file = "rahul gandhi27122018.xls"
def getData(file):
    data = xlrd.open_workbook(file)
    tweets_list = []
    for I in range(20000):
        try:
            tweets_list.append(data.sheet_by_index(0).cell_value(I, 1))
            I += 1
        except:
            pass
    tweets_set = set(tweets_list)
    print(len(tweets_list))
    print(len(tweets_set))
    return tweets_set


chunk = []
bjp = getData("bjp.xls")
for i in bjp:
    chunk.append(i)
cong = getData("congress.xls")
for i in cong:
    chunk.append(i)
rg = getData("rahul gandhi.xls")
for i in rg:
    chunk.append(i)
for tweet in set_of_tweets:
    chunk.append(tweet)
print(len(chunk))
set_chunk = set(chunk)
print(len(set_chunk))
