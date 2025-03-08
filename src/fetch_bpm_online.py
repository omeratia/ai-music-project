import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# ✅ Load Spotify credentials from environment variables
SPOTIPY_CLIENT_ID = 'b4bfbf4d1a774411900453c87bbb547d'
SPOTIPY_CLIENT_SECRET = '47362b141ea64c52ac733ae6e9b040c3'
SPOTIPY_REDIRECT_URI = "http://localhost:5002/callback"

import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# ✅ Load Spotify credentials


# ✅ Authenticate using Client Credentials (NOT OAuth)
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                        client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_audio_analysis(track_id):
    """Fetch full audio analysis data from Spotify."""
    print(f"🎵 Fetching Audio Analysis for Track ID: {track_id}")

    try:
        # ✅ Step 1: Get a Fresh Access Token (to avoid expired tokens)
        token_info = auth_manager.get_access_token(as_dict=True)
        access_token = token_info['access_token']

        # ✅ Step 2: Request `/audio-features/` to Get `analysis_url`
        headers = {"Authorization": f"Bearer {access_token}"}
        url = f"https://api.spotify.com/v1/audio-features/{track_id}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"❌ Failed to fetch audio features: {response.status_code}")
            print(f"⚠️ API Response: {response.json()}")
            return None

        audio_features = response.json()
        analysis_url = audio_features.get("analysis_url")
        
        if not analysis_url:
            print("❌ No analysis_url found in response.")
            return None

        print(f"🔍 Analysis URL: {analysis_url}")

        # ✅ Step 3: Fetch Full Analysis Data from `analysis_url`
        analysis_response = requests.get(analysis_url, headers=headers)

        if analysis_response.status_code == 200:
            analysis_data = analysis_response.json()
            print("✅ Successfully fetched detailed audio analysis!")

            # Save analysis to JSON file
            with open(f"analysis_{track_id}.json", "w") as f:
                json.dump(analysis_data, f, indent=4)

            print(f"📂 Analysis data saved to analysis_{track_id}.json")
            return analysis_data
        else:
            print(f"❌ Failed to fetch analysis: {analysis_response.status_code}")
            return None

    except Exception as e:
        print(f"⚠️ Error: {e}")
        return None

# 🎵 Example: Fetch analysis for a song (Replace with your track ID)
track_id = "7LRMbd3LEoV5wZJvXT1Lwb"  # Change this to your track ID
analysis_data = get_audio_analysis(track_id)

if analysis_data:
    print("🔍 Top-Level Keys in Analysis Data:", list(analysis_data.keys()))