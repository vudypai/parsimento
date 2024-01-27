from main import determine_degrees

def format_note(note):
    return note.replace("#", "is").replace("b", "es").replace("n", "").lower()

def write_lilypond(degrees, basso):
    formatted_basso = [format_note(note) for note in basso]
    out = ""

    # Write notes
    out += r"bass = { \clef bass "
    for note in formatted_basso:
        out += f"{note} "
    out += "}"

    # Write degrees
    out += r"continuo = \figuremode {"
    for degree in degrees:
        out += f"<{degree}>4 "
    out += "}"

    out += r" \score { << \new Staff = bassStaff \bass \context Staff = bassStaff \continuo >> } "
    return out


if __name__ == "__main__":
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
    degrees = determine_degrees(tp)
    print(write_lilypond(degrees, tp))