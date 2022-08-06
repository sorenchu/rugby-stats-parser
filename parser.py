#!/usr/bin/python3
from csv_file import CsvFile
from pprint import pprint

def main():
    # csv = CsvFile("mock_touch.csv")
    csv = CsvFile("example.csv")
    pprint(csv.get_file_content())
    


if __name__ == "__main__":
    main()
