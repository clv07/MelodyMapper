import mido


def print_midi_info(file_path):
    midi_file = mido.MidiFile(file_path)

    print("MIDI File Information:")
    print("Type:", midi_file.type)
    print("Ticks per Beat:", midi_file.ticks_per_beat)

    for i, track in enumerate(midi_file.tracks):
        print(f"\nTrack {i + 1}:")
        for msg in track:
            print(msg)


if __name__ == "__main__":
    midi_file_path = "sample1.mid"
    print_midi_info(midi_file_path)