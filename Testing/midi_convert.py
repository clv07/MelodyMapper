'''
https://mido.readthedocs.io/en/stable/index.html
mido message
.type
.note
.bytes()
Message('note_on', channel=2, note=60, velocity=64, time=0)

mid -> MidiFile
mid.tracks -> MidiTrack in a list

midifile -> miditrack -> msg

'''

# from mido import MidiFile
# from mido import Message
# from mido.tokenizer import Tokenizer

# mid = MidiFile('Am_I_Blue_AB.mid', clip=True)

# tracks = {}
# bin_msg = []


# for i, track in enumerate(mid.tracks):
#     for msg in track:
#         print(msg)
#         ha = msg.hex()
#         print(ha)
#         print(Message.from_hex(ha))
#         break


# # for msg in bin_msg:
# #     print(Message.from_bytes(msg))


from mido import MidiFile, Message

mid = MidiFile('Am_I_Blue_AB.mid', clip=True)

for i, track in enumerate(mid.tracks):
    for msg in track:
        # Get the bytes representation of the message
        msg_bytes = msg.bytes()

        # Print the bytes and decode them back to a Message object
        print("Bytes:", msg_bytes)
        decoded_msg = Message.from_bytes(msg_bytes)
        print("Decoded Message:", decoded_msg)
        print()

# Uncomment the following block if you want to work with the list of bytearrays
# bin_msgs = []
# for i, track in enumerate(mid.tracks):
#     for msg in track:
#         bin_msgs.append(msg.bytes())
#
# for msg_bytes in bin_msgs:
#     decoded_msg = Message.from_bytes(msg_bytes)
#     print("Decoded Message:", decoded_msg)
#     print()
