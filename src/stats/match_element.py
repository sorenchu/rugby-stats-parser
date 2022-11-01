class MatchElement:

    def __init__(self, combination_list):
        self.elements = {}
        for combination in combination_list:
            self.elements[combination] = 0

    def add_element(self, key):
        self.elements[key] += 1


    def get_elements(self):
        return self.elements

