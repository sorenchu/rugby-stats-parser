from .tackler import Tackler
from .penalty import Penalty
from csv_file import CsvFile
import os

class PlayedMatch:

    PLAYER = 0
    QUALITY = 1
    ZONE = 2
    PENALTY_TYPE = 1
    TACKLE = "Placaje"
    PENALTY = "Golpe de castigo"

    def __init__(self):
        self.tacklers = {}
        self.penaltiers = {}

    def filter_data(self, rows):
        data = []
        for row in rows:
            data.append(list(dict(filter(lambda elem: elem[1] == "1", row.items())).keys()))
        return data

    def analyze_tackles(self, csv_file):
        csv_file.extract_fragment_by_name(self.TACKLE)
        rows = csv_file.get_file_content_by_fragment_name(self.TACKLE)
        tackles = self.filter_data(rows)
        total_tackles = Tackler()
        for tackle in tackles:
            if tackle[self.PLAYER] not in self.tacklers.keys():
                self.tacklers[tackle[self.PLAYER]] = Tackler()
            self.tacklers[tackle[self.PLAYER]].add_tackle(tackle[self.QUALITY], tackle[self.ZONE])
            total_tackles.add_tackle(tackle[self.QUALITY], tackle[self.ZONE])
        self.tacklers["total"] = total_tackles

    def dump_tackles(self, output_path):
        if os.path.exists(output_path):
            os.remove(output_path)
        csv_writer = CsvFile(output_path, ",")
        for key, tackler in self.tacklers.items():
            csv_writer.write_csv_file(key, tackler.get_tackles())

    def analyze_penalties(self, csv_file):
        csv_file.extract_fragment_by_name("Golpe de castigo")
        rows = csv_file.get_file_content_by_fragment_name("Golpe de castigo")
        penalties = self.filter_data(rows)
        total_penalties = Penalty()
        for penalty in penalties:
            if penalty[self.PLAYER] not in self.penaltiers.keys():
                self.penaltiers[penalty[self.PLAYER]] = Penalty()
            self.penaltiers[penalty[self.PLAYER]].add_penalty(penalty[self.PENALTY_TYPE], penalty[self.ZONE])
            total_penalties.add_penalty(penalty[self.PENALTY_TYPE], penalty[self.ZONE])
        self.penaltiers["total"] = total_penalties

    def dump_penalties(self, output_path):
        if os.path.exists(output_path):
            os.remove(output_path)
        csv_writer = CsvFile(output_path, ",")
        for key, penaltier in self.penaltiers.items():
            csv_writer.write_csv_file(key, penaltier.get_penalties())

