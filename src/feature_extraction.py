import librosa
import numpy as np

# Load the song (same as before)
file_path = '/Users/omeratia/Desktop/AI music project/datasets/Drake - Don’t Run.mp3'
y, sr = librosa.load(file_path)

# --- Feature 1: Tempo (Beats per Minute) ---
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
# Explanation:
# - `librosa.beat.beat_track()` detects the tempo by analyzing the beat pattern.
# - This gives us the speed of the song — slow ballad (60 bpm) or fast dance (120 bpm).

# --- Feature 2: Spectral Centroid ---
spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
avg_centroid = np.mean(spectral_centroid)
# Explanation:
# - This is like the "center of mass" of the frequencies.
# - Low centroid = bass-heavy song.
# - High centroid = bright, treble-focused song.

# --- Feature 3: Spectral Bandwidth ---
spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
avg_bandwidth = np.mean(spectral_bandwidth)
# Explanation:
# - This measures how "wide" the frequency content is.
# - Narrow bandwidth = simple sound (single instrument).
# - Wide bandwidth = rich, complex mix (lots of overlapping instruments).

# --- Feature 4: Zero Crossing Rate ---
zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
avg_zero_crossing = np.mean(zero_crossing_rate)
# Explanation:
# - Counts how often the waveform crosses the zero line.
# - High ZCR = sharp, percussive sounds (like hi-hats).
# - Low ZCR = smooth, continuous sounds (like strings).

# --- Feature 5: MFCCs (Mel-Frequency Cepstral Coefficients) ---
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
avg_mfccs = np.mean(mfccs, axis=1)
# Explanation:
# - MFCCs are a **compressed fingerprint** of the sound spectrum.
# - They are used a lot in speech and music classification because they capture timbre.
# - We compute 13 coefficients and average each one over time.

# --- Feature 6: Chroma Features ---
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
avg_chroma = np.mean(chroma, axis=1)
# Explanation:
# - This captures which musical **notes** (C, D, E, etc.) are present over time.
# - Good for capturing melody and harmonic content.

# Combine into a single feature vector (for AI model later)
feature_vector = {
    "tempo": tempo,
    "spectral_centroid": avg_centroid,
    "spectral_bandwidth": avg_bandwidth,
    "zero_crossing_rate": avg_zero_crossing,
    "mfccs": avg_mfccs.tolist(),
    "chroma": avg_chroma.tolist()
}

# Print to understand
import pprint
pprint.pprint(feature_vector)