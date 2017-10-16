import json
import discordwebhook as wh
# Class for storing tweet information


class TwitterHandler:
    def __init__(self):
        self.tweets = []
        self.played_songs = []
        self.newest_tweet = None
        self.current_song = None

    def parse_string(self, string_to_parse):
        parsed_string = string_to_parse.split(" ", 2)
        return parsed_string[1]

    def parse_tweet(self, tweet):
        return {
            "created_at": tweet["created_at"],
            "user": tweet["user"]["screen_name"],
            "text": tweet["text"]
        }

    def process_tweet(self, data):
        tweet_context = json.loads(data)
        self.tweets.append(tweet_context)
        song = self.parse_string(tweet_context["text"])
        print("Tweet text: {}".format(song))
        if self.song_already_played(song):
            print("This song has recently been requested, please wait before requesting again")
        else:
            self.played_songs.append(song)
            self.current_song = song
            self.newest_tweet = self.parse_tweet(tweet_context)
            print("Requester: {}".format(self.newest_tweet["user"]))
            print("------------------------------------")
            wh.send_msg('!play {} {}'.format(song, self.newest_tweet["user"]))

    def song_already_played(self, song):
        try:
            if song not in self.played_songs:
                self.played_songs.append(song)
                return False
            elif self.played_songs[::-1].index(song) >= 9:
                return True
        except ValueError:
            return True
