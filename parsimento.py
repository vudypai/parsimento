from reg import *
from parse2ly import *
from main import *
from ROTO import *

print("Welcome to Parsimento! This program does its best to provide good harmony to a bass line.\n"
      "Please specify a path to the .ly file of the bass you would like to figure.")

orig_file = input()
ly = open(orig_file, "r")
basso = get_notes(ly.read())
figuring = determine_degrees(basso)
output = open(orig_file + "figured.ly", "w")
output.write(write_lilypond(figuring, basso))

print("Wrote harmony for " + orig_file + " to " + orig_file + "figured.ly!")
