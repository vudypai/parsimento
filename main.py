import math

pitch_class = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11
}

sharp_keys = ["C", "G", "D", "A", "E", "B", "F#" "C#"]
flat_keys = ["F", "Bb", "Eb", "Ab", "Db", "Gb"]

chrom_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
chrom_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]


def generate_major_scale(root_note):
    major_scale_pattern = [2, 2, 1, 2, 2, 2, 1]
    if "n" in root_note:
        root_note = root_note[0]
    if root_note in sharp_keys:
        chromatic_notes = chrom_sharp
    else:
        chromatic_notes = chrom_flat
    root_note_index = chromatic_notes.index(root_note)
    major_scale_notes = [root_note]

    for step in major_scale_pattern:
        root_note_index = (root_note_index + step) % 12
        major_scale_notes.append(chromatic_notes[root_note_index])
    return major_scale_notes


def pc_cons(basso):
    out = []
    for note in basso:
        change = 0
        for i in note:
            if i == "#":
                change += 1
            if i == "b":
                change -= 1
        out.append((pitch_class[note[0]] + change) % 12)
    if len(out) == 12 and sum(out) == 66:
        print("That's a tone row, dawg.")
    return out


def inv_cons(pitches):
    out = []
    for i in range(len(pitches) - 1):
        out.append(int(math.remainder(pitches[i+1] - pitches[i], 12)))
    out.append(9999)
    return out


def generate_absolute_scale(keynote):
    notes = ["C", "D", "E", "F", "G", "A", "B"]
    return notes[notes.index(keynote[0]):] + notes[:notes.index(keynote[0])]


def create_mut_dict(basso):
    mut_dict = {0: basso[0], len(basso) - 2: basso[0]}
    intervals = inv_cons(pc_cons(basso))
    # initial labelling of semitone movements
    for i in range(len(basso)):
        if "#" in basso[i] or "b" in basso[i] or "n" in basso[i]:
            if intervals[i] == 1:  # moves semitone up
                mut_dict[i] = basso[i + 1]  # keynote is destination note of semitone movement
            elif intervals[i] == -1:  # moves semitone down
                temp_scale = generate_major_scale(basso[i])  # keynote is minor 6th down from semitone
                mut_dict[i] = temp_scale[2]

    return mut_dict


def label_degree(d, scale):  # scale is absolute
    return scale.index(d[0]) + 1


def function_1(basso, mut_dict):
    scale = mut_dict[0]
    degrees = [0] * len(basso)
    for i in range(len(basso)):
        if i in mut_dict:
            scale = generate_absolute_scale(mut_dict[i])
        degrees[i] = (label_degree(basso[i], scale))
    return degrees


def determine_degrees(basso):
    mut_dict = create_mut_dict(basso)
    for _ in range(3):
        degrees = function_1(basso, mut_dict)
        for i in range(len(degrees)):
            if degrees[i] == 6 and i not in mut_dict:
                if degrees[i+1] == 5:
                    mut_dict[i] = generate_major_scale(basso[i][0])[2]  # keynote at index is m6 down
                if degrees[i+1] == 7:
                    mut_dict[i] = generate_major_scale(basso[i][0])[4]  # keynote at index is P4 down

    return degrees

# Tests
tp = ["C", "F", "E", "D",
      "C", "E", "F", "G",
      "C", "B", "C", "C",
      "F#", "G", "C", "D",
      "G", "G", "E", "F#",
      "B", "B", "G", "A",
      "D", "Fn", "E", "D",
      "C", "A", "D", "E",
      "A", "A", "F#", "G",
      "C", "D", "G", "Bb",
      "A", "Fn", "G", "A",
      "D", "Bn", "C", "E",
      "F", "G", "C"
      ]
tp2 = ["G", "B", "C", "B", "A", "G", "D", "D", "G", "B", "C", "A", "B", "G", "A", "F", "G", "C#", "D", "A", "F", "D", "C#", "D", "G", "G", "A", "A", "D", "F", "G", "E", "F", "D", "E", "C#", "D", "Fn", "E", "D", "C", "A", "D", "E", "A", "A", "Fn", "G", "C", "F#", "G", "F", "G", "B", "C", "B", "A", "G", "D", "D", "G", "B", "D", "G", "E", "C", "D", "E", "B", "C", "C#", "D"]

result = determine_degrees(tp2)
print(result)
