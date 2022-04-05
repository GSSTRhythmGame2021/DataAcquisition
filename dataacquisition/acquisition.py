"""analyzes given spotify song"""
import os

import pandas as pd
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials


def authentication(cid: str, secret: str):
    """Sets up the client authentication"""
    client_credentials_manager = SpotifyClientCredentials(
        client_id=cid, client_secret=secret
    )
    spot_auth = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return spot_auth


def analysis_func(track: str, spot_auth) -> pd.DataFrame:
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
    with open("Varied - SBG (Skelly57) [Normal].osu", "a", encoding="utf-8") as beatmap:
        beatmap.write(
            "osu file format v14\n"
            "\n"
            "[General]\n"
            "AudioFilename: audio.mp3\n"
            "AudioLeadIn: 0\n"
            "PreviewTime: -1\n"
            "Countdown: 0\n"
            "SampleSet: Normal\n"
            "StackLeniency: 0.7\n"
            "Mode: 0\n"
            "LetterboxInBreaks: 0\n"
            "WidescreenStoryboard: 0\n"
            "\n"
            "[Editor]\n"
            "DistanceSpacing: 0.8\n"
            "BeatDivisor: 1\n"
            "GridSize: 32\n"
            "TimelineZoom: 1\n"
            "\n"
            "[Metadata]\n"
            "Title:Spotify Beatmap Generation\n"
            "TitleUnicode:Spotify Beatmap Generation\n"
            "Artist:Varied\n"
            "ArtistUnicode:Varied\n"
            "Creator:Skelly57\n"  # default creator, can change to group name later
            "Version:Normal\n"
            "Source:\n"
            "Tags:\n"
            "BeatmapID:0\n"
            "BeatmapSetID:-1\n"
            "\n"
            "[Difficulty}\n"
            "HPDrainRate:5\n"
            "CircleSize:5\n"
            "OverallDifficulty:5\n"
            "ApproachRate:5\n"
            "SliderMultiplier:1.4\n"
            "SLiderTickRate:1\n"
            "\n"
            "[Events]\n"
            "//Background and Video events\n"
            "//Break Periods\n"
            "//Storyboard Layer 0 (Background)\n"
            "//Storyboard Layer 1 (Fail)\n"
            "//Storyboard Layer 2 (Pass)\n"
            "//Storyboard Layer 3 (Foreground)\n"
            "//Storyboard Layer 4 (Overlay)\n"
            "//Storyboard Sound Samples\n"
            "\n"
            "[TimingPoints]\n"
            "0,500,4,1,0,100,1,0\n"
            "\n"
            "\n"
            "[HitObjects]\n"
        )
        for index, _ in segments.iterrows():
            pitchavg = pitchaverage(seg_pitch[index])
            print(
                pitchcat(pitchavg),
                ",192,",
                seg_start[index] * 1000,
                ",5,4,0:0:0:0:\n",
                sep="",
            )
            beatmap.write(
                str(pitchcat(pitchavg))
                + ",192,"
                + str(seg_start[index] * 1000)
                + ",5,4,0:0:0:0:\n"
            )


def pitchaverage(seg_pitch) -> float:
    """averages all pitches in a section"""
    ret: float = 0.0
    for _, value in enumerate(seg_pitch):
        ret += value
    ret /= len(seg_pitch) - 1
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

    spot_auth = authentication(cid, secret)

    track = "spotify:track:6yIjtVtnOBeC8SwdVHzAuF"
    segments = analysis_func(track, spot_auth)
    beatmaker(segments)


if __name__ == "__main__":
    main()
