import os
import spotipy
from dotenv import load_dotenv
from pathlib import Path
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path)

# Get Spotify credentials
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# Authenticate using Spotify Client Credentials (Same method that worked before)
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                        client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def fetch_audio_features(track_id):
    """Fetch audio features for a given track ID using the Spotify API."""
    try:
        features = sp.audio_features([track_id])[0]

        if not features:
            print("❌ No features found or track ID is invalid.")
            return

        print(f"🎵 Audio Features for Track ID {track_id}:")
        print(f"   Tempo (BPM): {features['tempo']}")
        print(f"   Key: {features['key']}")
        print(f"   Mode: {features['mode']}")
        print(f"   Danceability: {features['danceability']}")
        print(f"   Energy: {features['energy']}")
        print(f"   Valence: {features['valence']}")

    except spotipy.exceptions.SpotifyException as e:
        print(f"🚨 Spotify API Error: {e}")

# Example usage
track_id = "6eHvBAY5OxPvOZTUDuhzM7"
fetch_audio_features(track_id)