class RGBNeuron:
    def __init__(self):
        self.probability = 0

    def calc_prob(self, rgb_list, list_index):
        self.probability = rgb_list[list_index] / 255

    def output(self):
        return self.probability
