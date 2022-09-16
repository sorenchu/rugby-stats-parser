import csv, io


class CsvFile:

    def __init__(self, path, delimiter=";"):
        self.path = path
        self.delimiter = delimiter
        self.fragments = {}

    def get_file_content_by_fragment_name(self, fragment_name):
        rows = []
        fragment_content = csv.DictReader(io.StringIO(self.fragments[fragment_name]), delimiter=self.delimiter)
        for row in fragment_content:
            rows.append(row)
        return rows
        
    def write_csv_file(self, identifier, data):
        with open(self.path, "a", encoding="UTF8", newline="") as f:
            values_to_be_inserted = list(data.values())
            values_to_be_inserted.insert(0, identifier)
            writer = csv.writer(f)
            writer.writerow(values_to_be_inserted)

    def extract_fragment_by_name(self, fragment_name):
        fragment = ""
        with open(self.path) as f:
            getting_row = False
            content_file = f.read()
            init = content_file.find(f"CATEGORY: {fragment_name},,,") + len(f"CATEGORY: {fragment_name},,,\n")
            end = content_file.find("\n,,,\n", init)
            self.fragments[fragment_name] = content_file[init:end+1].replace(",,,", "")

