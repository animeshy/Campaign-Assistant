import twitter


api = twitter.Api(consumer_key="ZkueGAecI0y6rrbwbPrN3KcRg",
                 consumer_secret="VN5O8rcKYmCF6SSFNZtU3QkxH1l47vrU4I3uaWc6Cdnub2XhIB",
                 access_token_key="1046326010713714688-JNIZx8CXJbErXnRaEiblSF1mctEKP8",
                 access_token_secret="BGgxzDGQpoHhEWFN13HpPqrpPO24GPmuFtb16an7OYoCk")

result = api.GetSearch(term="modi",
                       raw_query=None,
                       geocode=None,
                       since_id=None,
                       max_id=None,
                       until=None,
                       since=None,
                       count=15,
                       lang=None,
                       locale=None,
                       result_type='mixed',
                       include_entities=None,
                       return_json=False)

print(result)
