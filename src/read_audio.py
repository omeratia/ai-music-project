import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the audio file
file_path = '../datasets/Drake - Don’t Run.mp3'
y, sr = librosa.load(file_path)

# Print some basic song info
print(f"Sample Rate: {sr} Hz")  # How many samples per second (22050 is default)
print(f"Duration: {len(y)/sr:.2f} seconds")  # Total length in seconds

# Create a single figure for both plots
plt.figure(figsize=(14, 8))

# ==========================
# Plot 1: Waveform
# ==========================
plt.subplot(1, 2, 1)  # 1 row, 2 columns, this is plot 1
librosa.display.waveshow(y, sr=sr)
plt.title('Waveform - Drake - Don’t Run')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')

# ==========================
# Plot 2: Spectrogram
# ==========================
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

plt.subplot(1, 2, 2)  # 1 row, 2 columns, this is plot 2
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram - Drake - Don’t Run')

# Show both plots together
plt.tight_layout()
plt.show()