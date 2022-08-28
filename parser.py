#!/usr/bin/python3
from stats.played_match import PlayedMatch

def main():
    played_match = PlayedMatch()
    played_match.analyze_tackles("mock_tackle.csv")
    played_match.dump_tackles("tackles_output.csv")
    played_match.analyze_penalties("mock_penalties.csv")
    played_match.dump_penalties("penalties_output.csv")


if __name__ == "__main__":
    main()
