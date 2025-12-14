# import librosa
# import soundfile as sf

# # Get example audio file
# filename = librosa.ex("trumpet")

# data, samplerate = sf.read(filename, dtype="float32")
# data = data.T
# data_22k = librosa.resample(data, samplerate, 22050)

import librosa
import soundfile as sf

# Get example audio file
filename = librosa.example('trumpet')

data, samplerate = sf.read(filename, dtype='float32')
data = data.T

# Specify the target sampling rate (e.g., 22050)
target_samplerate = 22050

# Resample the data to the target sampling rate
data_22k = librosa.resample(data, orig_sr=samplerate, target_sr=target_samplerate)
