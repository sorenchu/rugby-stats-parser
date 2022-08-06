import csv


class CsvFile:

    def __init__(self, path, delimiter=";"):
        self.path = path
        self.delimiter = delimiter

    def get_file_content(self):
        rows = []
        with open(self.path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            for row in csv_reader:
                rows.append(row)
        return rows
        