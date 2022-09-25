#!/usr/bin/python3
from stats.played_match import PlayedMatch
from csv_file import CsvFile

def main():
    file_input = CsvFile("example.csv")
    played_match = PlayedMatch()
    tackles = played_match.analyze_element(file_input, "tackle")
    played_match.dump_elements("tackles.csv", tackles)
    penalties = played_match.analyze_element(file_input, "penalty")
    played_match.dump_elements("penalties.csv", penalties)

if __name__ == "__main__":
    main()
