#!/usr/bin/python3
from csv_file import CsvFile
from pprint import pprint


def filter_data(rows):
    data = []
    for row in rows:
        data.append(dict(filter(lambda elem: elem[1] == "1", row.items())).keys())
    return data

def main():
    # csv = CsvFile("mock_tackle.csv")
    csv = CsvFile("mock_touch.csv")
    tackles = []
    print(filter_data(csv.get_file_content()))


if __name__ == "__main__":
    main()
