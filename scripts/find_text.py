#!/usr/bin/env python3.6

'''
command example: find_text "phrase" place1 place2

program search only in .txt files
'''

import os
import sys

def find_phrase(file):
    with open(file, "r") as file:
        print(f"\n*** File: {file.name} ***")
        for num, line in enumerate(file, 1):
            if line.find(phrase) != -1:
                print(f"line {num}: {line}")

def change_dir(dir):
    os.chdir(dir)
    path = os.getcwd()
    return path

def get_next_element(path):
    for tree in os.walk(path):
        for branch in tree[:0:-1]:
            for el in branch:
                check_place(el)

def check_place(param):
    if os.path.isdir(param):
        path = change_dir(param)
        get_next_element(path)
    elif os.path.isfile(param) and param.endswith(".txt"):
        find_phrase(param)

def get_param():
    try:
        phrase, *places_to_look = sys.argv[1:]
        if not places_to_look:
            print("Indicate where to search for a phrase")
        else:
            return phrase, places_to_look
    except ValueError:
        print("Write phrase which You would find")

def run():
    global phrase
    phrase, places_to_look = get_param()
    for place in places_to_look:
        check_place(place)

if __name__ == '__main__':
    run()
