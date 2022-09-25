class Tackler:

    def __init__(self, combination_list):
        self.tackles = {}
        for combination in combination_list:
            self.tackles[combination] = 0

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
