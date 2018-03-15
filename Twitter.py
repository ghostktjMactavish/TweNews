from twitterscraper import query_tweets
def tweet(news):
    queried_data=query_tweets(news,20)
    data=list()
    for twe in queried_data:
        data.append(twe.text)
    return data#returns list of tweets all of which are strings
