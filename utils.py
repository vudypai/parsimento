"""Utility variables"""

# pitch classes of white keys
pitch_class = {
    "c": 0,
    "d": 2,
    "e": 4,
    "f": 5,
    "g": 7,
    "a": 9,
    "b": 11
}

accidental_terminology = {
    "isis": 2,
    "eses": -2,
    "is": 1,
    "es": -1
}

"""Utility functions"""

# SHARPS, -is suffix,
# FLATS, -es suffix
# pitch is ABSOLUTE. must denote accidentals EVEN WHEN KEY SIG PRESENT.

# construct_pitch_class: list -> list
def construct_pitch_class(basso):
    out = []
    for note in basso:
        change = 0
        # BROKEN you need a better fix for reading isis/eses
        for a in accidental_terminology.keys():
            if a in note:
                change += accidental_terminology[a]
        out.append((pitch_class[note[0]] + change) % 12)
    if len(out) == 12 and sum(out) == 66:
        print("That's a tone row, dawg.")  # lol Schoenberg
    return out

test_bass = ["d", "dis", "disis", "des", "deses"]
result = construct_pitch_class(test_bass)
print(result)

# generate_absolute_scale: str -> list
# given keynote, generate scale without accidentals
def generate_absolute_scale(keynote):
    notes = ["c", "d", "e", "f", "g", "a", "b"]
    return notes[notes.index(keynote[0]):] + notes[:notes.index(keynote[0])]

# label_degree: str, str -> int
# labels according to absolute scale
def label_degree(degree, key):
    scale = generate_absolute_scale(key)
    return scale.index(degree)





