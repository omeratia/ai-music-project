import librosa
import numpy as np

def detect_bpm(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file, sr=None)

    # Onset envelope (detects beat-related energy changes)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)

    # Compute the BPM
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr, onset_envelope=onset_env)

    return tempo

# Example usage:
file_path = "/Users/omeratia/Desktop/AI music project/datasets/spotidownloader.com - Free Me - Odeal.mp3"
bpm = detect_bpm(file_path)
print(f"🎵 Estimated BPM: {bpm}")