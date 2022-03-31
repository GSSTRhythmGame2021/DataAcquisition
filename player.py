"""analyzes given spotify song"""
import os

import json
import spotipy
import webbrowser
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

def authentication(cid: str, secret: str):
    """Sets up the client authentication"""
    client_credentials_manager = SpotifyClientCredentials(
        client_id=cid, client_secret=secret
    )
    spot_auth = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return spot_auth


def main():
    """declares variables and calls other funvtions"""
    load_dotenv()
    cid: str | None
    cid = os.environ.get("CLIENT_ID")
    secret: str | None
    secret = os.environ.get("CLIENT_SECRET")
    username: str | None
    username = os.environ.get("CLIENT_USERNAME")
    track: str | None
    track = os.environ.get("TRACK_ID")
    uri: str | None
    uri = os.environ.get("CLIENT_REDIRECT")

    if cid is None or secret is None or username is None or track is None or uri is None:
        print("Configure your environment variables")
        return

    spot_auth = authentication(cid, secret)
    oauth = spotipy.SpotifyOAuth(cid,secret,uri)
    token_dict = oauth.get_access_token()
    token = token_dict['access_token']


