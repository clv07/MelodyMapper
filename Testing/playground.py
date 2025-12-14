import aubio
import numpy as np
import mido
from mido import MidiFile, MidiTrack, Message


def audio_to_midi(audio_file, output_midi_file):
    # Initialize aubio pitch detection
    samplerate = 44100
    win_s = 4096
    hop_s = 512
    pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)
    pitch_o.set_unit("midi")

    # Open the audio file
    s = aubio.source(audio_file, samplerate, hop_s)

    # Create a new MIDI file and track
    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)

    # Process the audio and extract MIDI notes
    total_frames = 0
    while True:
        samples, read = s()
        pitch = pitch_o(samples)[0]
        if pitch > 0:  # Only add notes with a positive pitch value
            midi_note = int(round(pitch))
            track.append(Message("note_on", note=midi_note, velocity=64, time=0))
            track.append(Message("note_off", note=midi_note, velocity=64, time=128))
        total_frames += read
        if read < hop_s:
            break

    # Save the MIDI file
    midi_file.save(output_midi_file)

    return output_midi_file


# Example usage
output_midi_file = audio_to_midi("sample1.wav", "output_file.mid")
print(f"MIDI file saved as {output_midi_file}")
