from .tackler import Tackler
from .penalty import Penalty
from .match_element import MatchElement
from csv_file import CsvFile
import os
import yaml
from itertools import product

class PlayedMatch:

    PLAYER = 0

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

    def get_name(self, config_name):
        return self.config[config_name]["name"]

    def get_combinations(self, config_name):
        combination_list = []
        for combs in product(*self.config[config_name]["keys"].values()):
            combination_list.append("-".join(combs))
        return combination_list


    def analyze_element(self, csv_file, element_name):
        elements = {}
        config_name = self.get_name(element_name)
        csv_file.extract_fragment_by_name(config_name)
        rows = csv_file.get_file_content_by_fragment_name(config_name)
        for row in rows:
            if row[self.PLAYER] not in elements.keys():
                elements[row[self.PLAYER]] = MatchElement(
                    self.get_combinations(element_name)
                )
            elements[row[self.PLAYER]].add_element("-".join(row[1:]))
        return elements

    def dump_elements(self, output_path, elements):
        if os.path.exists(output_path):
            os.remove(output_path)
        csv_writer = CsvFile(output_path, ",")
        for key, element in elements.items():
            csv_writer.write_csv_file(key, element.get_elements())

