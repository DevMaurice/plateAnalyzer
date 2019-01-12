# steramer here

from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import creds
import os
import json


class StdoutListener(StreamListener):
    def on_data(self, data):
        with open('tweets.txt', 'a+') as fs:
            fs.write(data)

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    listener = StdoutListener()
    auth = OAuthHandler(creds.CONSUMER_KEY, creds.CONSUMER_SECRET)
    auth.set_access_token(creds.ACCCESS_TOKEN, creds.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, listener)
    stream.filter(locations=[33.9, -0.94, 41.21, 3.98])
