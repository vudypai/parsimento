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

