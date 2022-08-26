#!/usr/bin/python3
from csv_file import CsvFile
from tackler import Tackler
from pprint import pprint

PLAYER = 0
QUALITY = 1
ZONE = 2


def filter_data(rows):
    data = []
    for row in rows:
        data.append(list(dict(filter(lambda elem: elem[1] == "1", row.items())).keys()))
    return data

def main():
    csv = CsvFile("mock_tackle.csv")
    # csv = CsvFile("mock_touch.csv")
    tackles = filter_data(csv.get_file_content())
    tacklers = {}
    for tackle in tackles:
        if tackle[PLAYER] not in tacklers.keys():
            tacklers[tackle[PLAYER]] = Tackler()
        else:
            tacklers[tackle[PLAYER]].add_tackle(tackle[QUALITY], tackle[ZONE])
    for player, tackles in tacklers.items():
        print(player)
        pprint(tackles)


if __name__ == "__main__":
    main()
