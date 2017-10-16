from tokens import keys
import streamer
from tweets import TwitterHandler

if __name__ == "__main__":
    print("Setting up twitter streamer...")
    handler = TwitterHandler()
    streamer.setup_streamer(handler)
