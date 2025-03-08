import librosa
import matplotlib.pyplot as plt
import numpy as np

# Load the song
file_path = '../datasets/Drake - Don’t Run.mp3'
y, sr = librosa.load(file_path)

# How many samples per second?
print(f"Sample rate: {sr} Hz")  # 22050 Hz

# Let's zoom in at **10 seconds into the song**
start_second = 10
start_sample = int(start_second * sr)  # 10 seconds worth of samples

# We still want to see 20 milliseconds worth of data (short zoom)
zoom_samples = int(0.02 * sr)  # 0.02 seconds = 20ms

# Slice the waveform
y_zoom = y[start_sample:start_sample + zoom_samples]

# Create time axis (in milliseconds relative to the zoom window)
time = np.linspace(start_second * 1000, (start_second + 0.02) * 1000, zoom_samples)

# Plot the zoomed-in waveform section
plt.figure(figsize=(12, 6))
plt.plot(time, y_zoom, marker='o', linestyle='-', markersize=4)

plt.title(f"Zoomed-In Waveform - {start_second}s to {start_second+0.02}s")
plt.xlabel("Time (milliseconds)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()