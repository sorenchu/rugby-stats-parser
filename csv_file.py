import csv


class CsvFile:

    def __init__(self, path, delimiter=";"):
        self.path = path
        self.delimiter = delimiter

    def get_file_content(self):
        rows = []
        with open(self.path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=self.delimiter)
            for row in csv_reader:
                rows.append(row)
        return rows
        
    def write_csv_file(self, identifier, data):
        with open(self.path, "a", encoding="UTF8", newline="") as f:
            values_to_be_inserted = list(data.values())
            values_to_be_inserted.insert(0, identifier)
            writer = csv.writer(f)
            writer.writerow(values_to_be_inserted)
            
