class Tackler:

    def __init__(self):
        self.stats = {
           "QP0": 0,
           "QP1": 0,
           "QP2": 0,
           "QP3": 0,
           "ZP0": 0,
           "ZP1": 0,
           "ZP2": 0,
           "ZP3": 0,
        }

    def add_tackle(self, quality: str, zone: str):
        self.stats[quality] += 1
        self.stats[zone] += 1

    def __str__(self):
        content = ""
        for key, value in self.stats.items():
            if content == "":
                content = f"{key}: {value}\n"
            else:
                content = f"{content}{key}: {value}\n"
        return content
