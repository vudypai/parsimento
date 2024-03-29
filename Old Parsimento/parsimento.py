from reg import *
from parse2ly import *
from main import *
from ROTO import *

print("Welcome to Parsimento! This program does its best to provide good harmony to a bass line.\n"
      "Please specify a path to the .ly file of the bass you would like to figure.")

orig_file = input(">")
ly = open(orig_file, "r")
basso = get_notes(ly.read())
degrees = determine_degrees(basso)
figuring = octave_rule(degrees)
output = open(orig_file[:-3] + "-figured.ly", "w")
output.write(write_lilypond(figuring, basso))

print("Wrote harmony for " + orig_file + " to " + orig_file[:-3] + "-figured.ly!")
