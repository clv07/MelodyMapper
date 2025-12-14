import pydub
import io

def audio_to_wav(audio_file, file_extension):
    """
    Helper function to convert audio file into wav file for MIDI conversion.

    Args:
        audio_file (bytes): Audio file as memory object from user.
        file_extension (string): Types of audio file extension.
    Returns:
        wav_file (bytes): WAV audio file as memory objects.
    """
    try:

        file_extension = file_extension.lower()

        # List of accepted audio file type
        available_extension = ["mp3", "m4a", "wav"]

        # Check if the provided extension is valid
        if file_extension not in available_extension:
            raise ValueError(
                "Invalid file extension. Please provide a valid mp3, m4a, or wav file."
            )

        # Return the input file directly if it is a wav file
        if file_extension == "wav":
            return audio_file

        # Load audio from memory object
        audio_input = pydub.AudioSegment.from_file(
            io.BytesIO(audio_file), format=file_extension[1:]
        )

        # Convert mp3 and m4a file to wav file
        wav_output = io.BytesIO()
        audio_input.export(wav_output, format="wav")
        wav_file = wav_output.getvalue()

        return wav_file

    except Exception as e:
        print("An error occurred during conversion from audio file to wav file:", e)
        return None


if __name__ == "__main__":

    # Sample audio file
    audio_file = b"guitar.wav"

    # Audio file to MIDI Conversion
    if audio_to_wav(audio_file) is None:
        print("Please provide audio file with extension of mp3, m4a or wav.")
