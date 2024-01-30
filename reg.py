import re

s = """
{ 
  \key g \major
  \clef bass 
  g d' b g 
  a g c' d' 
  g e d c \break
  b, g, a, g,
  c b, a, g, 
  c fis g e \break
  c d e b,
  c 2 d 2 g, 1}
"""


def get_notes(s):
    matches = re.findall(r"\b(?<!\\key )([a-g])(is|es)*(?:'|,)*(?:\s|$)", s)
    notes = [
    letter.upper() + alter.replace("es", "b").replace("is", "#")
    for (letter, alter) in matches]
    return notes

