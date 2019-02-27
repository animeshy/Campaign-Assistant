import xlrd


# file = "rahul gandhi27122018.xls"
file = "narendra modi.xls"
data = xlrd.open_workbook(file)
i = 0
tweets_list = []
for i in range(14530):
    tweets_list.append(data.sheet_by_index(0).cell_value(i,1))
    i += 1
tweets_set = set(tweets_list)
print(len(tweets_list))
print(len(tweets_set))
