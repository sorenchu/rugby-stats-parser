class Tackler:

    def __init__(self, player):
        self.tackles = {
            "player": player,
            "QP0-ZP0": 0,
            "QP0-ZP1": 0,
            "QP0-ZP2": 0,
            "QP0-ZP3": 0,
            "QP1-ZP0": 0,
            "QP1-ZP1": 0,
            "QP1-ZP2": 0,
            "QP1-ZP3": 0,
            "QP2-ZP0": 0,
            "QP2-ZP1": 0,
            "QP2-ZP2": 0,
            "QP2-ZP3": 0,
            "QP3-ZP0": 0,
            "QP3-ZP1": 0,
            "QP3-ZP2": 0,
            "QP3-ZP3": 0,
        }

    def add_tackle(self, quality: str, zone: str):
        self.tackles[f"{quality}-{zone}"] += 1

    def get_tackles(self):
        return self.tackles

    def __str__(self):
        content = ""
        for key, value in self.tackles.items():
            if content == "":
                content = f"{key}: {value}\n"
            else:
                content = f"{content}{key}: {value}\n"
        return content
