#!/usr/bin/python3
from stats.played_match import PlayedMatch
from csv_file import CsvFile
import sys, getopt, os

def print_error_and_exit():
    print("usage: parser.py -i <file.csv>")
    sys.exit(2)

def main(argv):
    input_file = ""
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print_error_and_exit()
    if opts == []:
        print_error_and_exit()
    for opt, arg in opts:
        if opt == "-h":
            print_error_and_exit()
        if opt in ("-i", "--ifile"):
            input_file = arg

    file_input = CsvFile(input_file)
    played_match = PlayedMatch()
    tackles = played_match.analyze_element(file_input, "tackle")
    played_match.dump_elements("tackles.csv", tackles)
    penalties = played_match.analyze_element(file_input, "penalty")
    played_match.dump_elements("penalties.csv", penalties)

if __name__ == "__main__":
    main(sys.argv[1:])
