"""analyzes given spotify song"""
import os
import spotipy
from dotenv import load_dotenv
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

def authentication(cid: str,secret: str) -> any:
    """Sets up the client authentication"""
    client_credentials_manager = SpotifyClientCredentials(client_id=cid,
            client_secret=secret)
    spot_auth = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return spot_auth

def analysis_func(track: str,spot_auth) -> any:
    """analyses the trck useing the spotify api"""
    analysis = spot_auth.audio_analysis(track)
    # features = spot_auth.audio_features(track)
    # features_df = pd.DataFrame(data=features, columns=features[0].keys())
    #beats_df = pd.DataFrame(data=analysis["beats"])
    segments_df = pd.DataFrame(data=analysis["segments"])
    # bars_df = pd.DataFrame(data=analysis["bars"])
    # tatums_df = pd.DataFrame(data=analysis["tatums"])
    return segments_df

def beatmaker(segments):
    """appends the osu file with data"""
    seg_start = segments["start"]
    seg_pitch = segments["pitches"]
    with open("ManiaTest.osu", 'a', encoding="utf-8") as beatmap:
        for index, _ in segments.iterrows():
            pitchavg = pitchaverage(seg_pitch[index])
            print(pitchcat(pitchavg),",192,",seg_start[index]*1000,",5,4,0:0:0:0:\n", sep='')
            beatmap.write("256,192,"+ str(seg_start[index]*1000) +",5,4,0:0:0:0:\n")

def pitchaverage(seg_pitch):
    """averages all piches in a section"""
    temp = 0
    for index in range( len(seg_pitch)):
        temp += seg_pitch[index]
    temp /= len(seg_pitch)-1
    print(temp)
    return temp

def pitchcat(pitchavg):
    """catagorizes pitches into four groups"""
    if(pitchavg < 0.3):
        temp = 128
    elif(pitchavg < 0.4):
        temp = 256
    elif(pitchavg < 0.5):
        temp = 384
    else:
        temp = 512
    return temp

def main():
    """declared variables and calls other funvtions"""
    load_dotenv()
    cid: str = os.environ.get("CLIENT_ID")
    secret: str = os.environ.get("CLIENT_SECRET")

    spot_auth = authentication(cid,secret)

    track = "spotify:track:6yIjtVtnOBeC8SwdVHzAuF"
    segments = analysis_func(track,spot_auth)
    beatmaker(segments)

if __name__ == "__main__":
    main()
