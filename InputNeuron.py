class InputNeuron:
    def __init__(self):
        self.rgb_list = [0, 0, 0]

    def set_values(self, hex_code):
        self.rgb_list[0] = int(hex_code[0:2], 16)
        self.rgb_list[1] = int(hex_code[2:4], 16)
        self.rgb_list[2] = int(hex_code[4:6], 16)

    def output(self):
        return self.rgb_list