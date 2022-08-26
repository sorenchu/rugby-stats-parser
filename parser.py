#!/usr/bin/python3
from stats.played_match import PlayedMatch

def main():
    played_match = PlayedMatch()
    played_match.analyze_tackles("mock_tackle.csv")

if __name__ == "__main__":
    main()
