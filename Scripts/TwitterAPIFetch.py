from TwitterAPI import TwitterAPI

api = TwitterAPI(consumer_key="ZkueGAecI0y6rrbwbPrN3KcRg",
                 consumer_secret="VN5O8rcKYmCF6SSFNZtU3QkxH1l47vrU4I3uaWc6Cdnub2XhIB",
                 access_token_key="1046326010713714688-JNIZx8CXJbErXnRaEiblSF1mctEKP8",
                 access_token_secret="BGgxzDGQpoHhEWFN13HpPqrpPO24GPmuFtb16an7OYoCk")

tweets = api.request('search/tweets', {'q': 'modi', 'count':100, 'tweet_mode': 'extended', 'lang': 'en'})

for item in tweets:
        print(item)


