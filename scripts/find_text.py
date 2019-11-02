#!/usr/bin/env python3.6
# command example: find_text "phrase" place1 place2

import os
import sys



def check_place(param):
    if os.path.isdir(param):
        os.chdir(param)
        path = os.getcwd()
        for tree in os.walk(path):
            for arr in tree[:0:-1]:
                for element in arr:
                    check_place(element)
    elif os.path.isfile(param) and param.endswith(".txt"):
        find_phase(param)

def find_phase(file):
    with open(file, "r") as file:
        print(f"\n*** File: {file.name} ***")
        for num, line in enumerate(file, 1):
            if line.find(phrase) != -1:
                print(f"line {num}: {line}")

try:
    phrase, *places_to_look = sys.argv[1:]
    if not places_to_look:
        print("Indicate where to search for a phrase")
    else:
        for place in places_to_look:
            check_place(place)
except ValueError:
    print("Write phrase which You would find")


