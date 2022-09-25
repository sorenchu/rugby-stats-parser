class Penalty:

    def __init__(self, combination_list):
        self.penalties = {}
        for combination in combination_list:
            self.penalties[combination] = 0

    def add_penalty(self, penalty_type: str, zone: str):
        self.penalties[f"{penalty_type}-{zone}"] += 1

    def get_penalties(self):
        return self.penalties
