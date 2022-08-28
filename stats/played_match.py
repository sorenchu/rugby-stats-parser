from .tackler import Tackler
from csv_file import CsvFile
import os

class PlayedMatch:

    PLAYER = 0
    QUALITY = 1
    ZONE = 2

    def __init__(self):
        self.tacklers = {}

    def filter_data(self, rows):
        data = []
        for row in rows:
            data.append(list(dict(filter(lambda elem: elem[1] == "1", row.items())).keys()))
        return data

    def analyze_tackles(self, path):
        csv = CsvFile(path)
        tackles = self.filter_data(csv.get_file_content())
        total_tackles = Tackler("total")
        for tackle in tackles:
            if tackle[self.PLAYER] not in self.tacklers.keys():
                self.tacklers[tackle[self.PLAYER]] = Tackler(tackle[self.PLAYER])
            else:
                self.tacklers[tackle[self.PLAYER]].add_tackle(tackle[self.QUALITY], tackle[self.ZONE])
                total_tackles.add_tackle(tackle[self.QUALITY], tackle[self.ZONE])
        self.tacklers["total"] = total_tackles

    def dump_tackles(self, output_path):
        if os.path.exists(output_path):
            os.remove(output_path)
        csv_writer = CsvFile(output_path, ",")
        for _, tackler in self.tacklers.items():
            csv_writer.write_csv_file(tackler.get_tackles())

