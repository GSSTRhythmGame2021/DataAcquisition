"""analyzes given spotify song"""
import os
import spotipy
from dotenv import load_dotenv
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

def authentication(cid: str,secret: str):
    """Sets up the client authentication"""
    client_credentials_manager = SpotifyClientCredentials(
            client_id=cid,
            client_secret=secret
            )
    spot_auth = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return spot_auth

def analysis_func(track: str,spot_auth) -> pd.DataFrame:
    """analyses the trck useing the spotify api"""
    analysis = spot_auth.audio_analysis(track)
    # features = spot_auth.audio_features(track)
    # features_df = pd.DataFrame(data=features, columns=features[0].keys())
    # beats_df = pd.DataFrame(data=analysis["beats"])
    segments_df = pd.DataFrame(data=analysis["segments"])
    # bars_df = pd.DataFrame(data=analysis["bars"])
    # tatums_df = pd.DataFrame(data=analysis["tatums"])
    return segments_df

def beatmaker(segments) -> None:
    """appends the osu file with data"""
    seg_start = segments["start"]
    seg_pitch = segments["pitches"]
    with open("ManiaTest.osu", 'a', encoding="utf-8") as beatmap:
        for index, _ in segments.iterrows():
            pitchavg = pitchaverage(seg_pitch[index])
            print(pitchcat(pitchavg),",192,",
                    seg_start[index]*1000,",5,4,0:0:0:0:\n", sep='')
            beatmap.write(str(pitchcat(pitchavg))+",192,"
                    + str(seg_start[index]*1000) +",5,4,0:0:0:0:\n")

def pitchaverage(seg_pitch) -> float:
    """averages all piches in a section"""
    ret: float = 0.0
    for _, value in enumerate(seg_pitch):
        ret += value
    ret /= len(seg_pitch)-1
    return ret

def pitchcat(pitchavg) -> int:
    """catagorizes pitches into four groups"""
    # values are set to four button osu mania defults
    far_left: int = 128
    cent_left: int = 256
    cent_right: int = 384
    far_right: int = 512
    ret: int
    # pitch ranges are guesstimations and can be optimised for better distribution
    if pitchavg < 0.3:
        ret = far_left
    elif pitchavg < 0.4:
        ret = cent_left
    elif pitchavg < 0.5:
        ret = cent_right
    else:
        ret = far_right
    return ret

def main():
    """declared variables and calls other funvtions"""
    load_dotenv()
    cid: str | None = os.environ.get("CLIENT_ID")
    secret: str | None = os.environ.get("CLIENT_SECRET")

    if cid is None or secret is None:
        print("Configure your environment variables")
        return

    spot_auth = authentication(cid,secret)

    track = "spotify:track:6yIjtVtnOBeC8SwdVHzAuF"
    segments = analysis_func(track,spot_auth)
    beatmaker(segments)

if __name__ == "__main__":
    main()
