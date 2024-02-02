import math

"""Utility variables"""

# lists of chromatic scales
chrom_sharp = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b"]
chrom_flat = ["c", "des", "d", "ees", "e", "f", "ges", "g", "aes", "a", "bes", "b"]

# circle of fifths
sharp_keys = ["c", "g", "d", "a", "e", "b", "fis", "cis", "gis"]
flat_keys = ["f", "bes", "ees", "aes", "des", "ges"]

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

# corresponding pitch transformations for accidentals
accidental_terminology = {
    "isis": 2,
    "eses": -2,
    "is": 1,
    "es": -1
}

"""Utility functions"""

# construct_pitch_class: list -> list
def construct_pitch_class(basso):
    out = []
    for note in basso:
        change = accidental_terminology.get(note[1:], 0)
        out.append((pitch_class[note[0]] + change) % 12)
    if len(out) == 12 and sum(out) == 66:
        print("That's a tone row, dawg.")  # lol Schoenberg
    return out

# construct_interval_class: list -> list
# takes output of construct_pitch_class and returns intervals between notes
def construct_interval_class(pitches):
    out = []
    for i in range(len(pitches) - 1):
        out.append(int(math.remainder(pitches[i+1] - pitches[i], 12)))
    out.append(400)  # dummy number to make list the same length as pitch classes
    return out


# generate_absolute_scale: str -> list
# given keynote, generate scale without accidentals
def generate_absolute_scale(keynote):
    notes = ["c", "d", "e", "f", "g", "a", "b"]
    return notes[notes.index(keynote[0]):] + notes[:notes.index(keynote[0])]

# generate_major_scale: str -> list
# given keynote, generate major scale
def generate_major_scale(keynote):
    major_scale_pattern = [2, 2, 1, 2, 2, 2, 1]
    if keynote in sharp_keys:
        chromatic_notes = chrom_sharp
    else:
        chromatic_notes = chrom_flat
    root_note_index = chromatic_notes.index(keynote)
    major_scale_notes = [keynote]

    for step in major_scale_pattern:
        root_note_index = (root_note_index + step) % 12
        major_scale_notes.append(chromatic_notes[root_note_index])
    return major_scale_notes

# label_degree: str, str -> int
# labels according to absolute scale
def label_degree(degree, key):
    scale = generate_absolute_scale(key)
    return scale.index(degree[0]) + 1


"""TESTS"""


