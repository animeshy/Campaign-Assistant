import urllib.request

# open a connection to a URL using urllib
webUrl = urllib.request.urlopen('https://t.co/hFm6dU7nWD')

# get the result code and print it
print("result code: " + str(webUrl.getcode()))

# read the data using the URL and print it
data = webUrl.read()
print(str(data))

# beautiful suite
str2 = data.replace(b"\n", b"")
print(str2)

