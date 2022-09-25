from .tackler import Tackler
from .penalty import Penalty
from csv_file import CsvFile
import os
import yaml
from itertools import product

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
        self.load_config()

    def load_config(self):
        with open("./config/entities.yml", "r") as f:
            try:
                self.config = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                print(exc)
                return

    def get_combinations(self, config_name):
        combination_list = []
        for combs in product(*self.config[config_name]["keys"].values()):
            combination_list.append("-".join(combs))
        return combination_list

    def analyze_tackles(self, csv_file):
        csv_file.extract_fragment_by_name(self.TACKLE)
        rows = csv_file.get_file_content_by_fragment_name(self.TACKLE)
        for tackle in rows:
            if tackle[self.PLAYER] not in self.tacklers.keys():
                self.tacklers[tackle[self.PLAYER]] = Tackler(self.get_combinations("tackle"))
            self.tacklers[tackle[self.PLAYER]].add_tackle(tackle[self.QUALITY], tackle[self.ZONE])

    def dump_tackles(self, output_path):
        if os.path.exists(output_path):
            os.remove(output_path)
        csv_writer = CsvFile(output_path, ",")
        for key, tackler in self.tacklers.items():
            csv_writer.write_csv_file(key, tackler.get_tackles())

    def analyze_penalties(self, csv_file):
        csv_file.extract_fragment_by_name(self.PENALTY)
        rows = csv_file.get_file_content_by_fragment_name(self.PENALTY)
        for penalty in rows:
            if penalty[self.PLAYER] not in self.penaltiers.keys():
                self.penaltiers[penalty[self.PLAYER]] = Penalty(self.get_combinations("penalty"))
            self.penaltiers[penalty[self.PLAYER]].add_penalty(penalty[self.PENALTY_TYPE], penalty[self.ZONE])

    def dump_penalties(self, output_path):
        if os.path.exists(output_path):
            os.remove(output_path)
        csv_writer = CsvFile(output_path, ",")
        for key, penaltier in self.penaltiers.items():
            csv_writer.write_csv_file(key, penaltier.get_penalties())

