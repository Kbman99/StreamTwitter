import tweepy
from tokens import keys


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, handler):
        self.handler = handler

    def on_data(self, data):
        print("New tweet received...")
        self.handler.process_tweet(data)
        return True

    def on_error(self, status):
        if status == "420":
            return False


def setup_streamer(handler):
    my_stream_listener = MyStreamListener(handler)
    auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
    auth.set_access_token(keys["access_token"], keys["access_token_secret"])

    my_stream = tweepy.Stream(auth=auth, listener=my_stream_listener)
    print("Setup complete.")
    print("---------------------------")
    my_stream.filter(track=['@PlayMeThisSong'], async=True)
