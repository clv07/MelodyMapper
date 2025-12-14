import wave

def print_wav_info(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        print("WAV File Information:")
        print("Channels:", wav_file.getnchannels())
        print("Sample Width:", wav_file.getsampwidth())
        print("Frame Rate:", wav_file.getframerate())
        print("Number of Frames:", wav_file.getnframes())
        print("Compression Type:", wav_file.getcomptype())
        print("Compression Name:", wav_file.getcompname())

if __name__ == "__main__":
    wav_file_path = "sample1.wav"
    print_wav_info(wav_file_path)
