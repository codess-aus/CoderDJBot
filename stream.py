from twython import TwythonStreamer
from auth import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET,
)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            print("@{}: {}".format(username, tweet))

stream = MyStreamer(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET,
)
stream.statuses.filter(track='#100daysofcode')