import os
import librosa
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Path to dataset folder
DATASET_PATH = '/Users/omeratia/Desktop/AI music project/datasets/'

def extract_features(file_path):
    y, sr = librosa.load(file_path)

    # Extract features
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    spectral_bandwidth = np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr))
    zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y))

    # Flatten MFCCs and Chroma features
    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=1).flatten()
    chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr), axis=1).flatten()

    # Ensure all features have the same shape before concatenation
    feature_vector = np.concatenate([
        np.array([spectral_centroid, spectral_bandwidth, zero_crossing_rate]),  # All scalars
        mfccs,  # Already flattened
        chroma  # Already flattened
    ])

    return feature_vector

# Load dataset & extract features
song_features = []
song_names = []

for file in os.listdir(DATASET_PATH):
    if file.endswith(".mp3") or file.endswith(".wav"):
        file_path = os.path.join(DATASET_PATH, file)
        print(f"Extracting features for: {file}")
        features = extract_features(file_path)
        song_features.append(features)
        song_names.append(file)

# Convert to numpy array
dataset = np.array(song_features)

# Normalize features
scaler = StandardScaler()
dataset_scaled = scaler.fit_transform(dataset)

# KNN Model using Cosine Similarity
knn = NearestNeighbors(n_neighbors=3, metric='cosine')  # Using Cosine Similarity
knn.fit(dataset_scaled)

# Find most similar songs
print("\n🔍 Finding most similar songs:")
for idx, song in enumerate(song_names):
    distances, indices = knn.kneighbors([dataset_scaled[idx]], n_neighbors=3)  # 3 closest songs
    print(f"\n🎶 Song: {song}")
    for i, neighbor_idx in enumerate(indices[0][1:]):  # Skipping itself
        print(f"   🔗 Similar to: {song_names[neighbor_idx]} (Distance: {distances[0][i+1]:.4f})")
