from .tackler import Tackler
from csv_file import CsvFile

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
        tacklers = {}
        for tackle in tackles:
            if tackle[self.PLAYER] not in tacklers.keys():
                tacklers[tackle[self.PLAYER]] = Tackler()
            else:
                tacklers[tackle[self.PLAYER]].add_tackle(tackle[self.QUALITY], tackle[self.ZONE])
        for player, tackles in tacklers.items():
            print(player)
            print(tackles)

