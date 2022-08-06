#!/usr/bin/python3
from csv_file import CsvFile
from pprint import pprint


def filter_data(rows):
    data = []
    for row in rows:
        data.append(list(dict(filter(lambda elem: elem[1] == "1", row.items())).keys()))
    return data

def main():
    csv = CsvFile("mock_tackle.csv")
    # csv = CsvFile("mock_touch.csv")
    tackles = filter_data(csv.get_file_content())
    # print(tackles)
    tacklers = {}
    for tackle in tackles:
        if tackle[0] not in tacklers.keys():
            tacklers[tackle[0]] = {
                "QP0": 0,
                "QP1": 0,
                "QP2": 0,
                "QP3": 0,
                "ZP0": 0,
                "ZP1": 0,
                "ZP2": 0,
                "ZP3": 0,
            }
        else:
            tacklers[tackle[0]][tackle[1]] += 1
            tacklers[tackle[0]][tackle[2]] += 1
    pprint(tacklers)


if __name__ == "__main__":
    main()
