#!/usr/bin/python3
from stats.played_match import PlayedMatch
from csv_file import CsvFile

def main():
    file_input = CsvFile("example.csv")
    played_match = PlayedMatch()
    played_match.analyze_penalties(file_input)
    played_match.analyze_tackles(file_input)
    played_match.dump_penalties("patata.csv")
    played_match.dump_tackles("tomas.csv")


if __name__ == "__main__":
    main()
