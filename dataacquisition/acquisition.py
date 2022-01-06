import os
import spotipy
from dotenv import load_dotenv
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

def authentication(cid: str,secret: str) -> any:
    client_credentials_manager = SpotifyClientCredentials(client_id=cid,
            client_secret=secret)
    spot_auth = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return spot_auth

def analysis_func(track: str,spot_auth) -> any:
    Analysis = spot_auth.audio_analysis(track)
    beats_df = pd.DataFrame(data=Analysis["beats"])
    return beats_df

def beatmaker(beats):
    beat_start = beats["start"]
    with open("osutesting.osu", 'a', encoding="utf-8") as beatmap:
        for index, _ in beats.iterrows():
            print("256,192,",beat_start[index]*1000,",5,4,0:0:0:0:\n", sep='')
            beatmap.write("256,192,"+ str(beat_start[index]*1000) +",5,4,0:0:0:0:\n")

def main():
    load_dotenv()
    cid: str = os.environ.get("CLIENT_ID")
    secret: str = os.environ.get("CLIENT_SECRET")

    spot_auth = authentication(cid,secret)

    track = "spotify:track:6yIjtVtnOBeC8SwdVHzAuF"
    beats = analysis_func(track,spot_auth)
    beatmaker(beats)

if __name__ == "__main__":
    main()
