class SecondaryNeuron:
    def __init__(self, main_color, accent_color):
        self.accent_color = accent_color
        self.main_color = main_color
        self.accent_color_value = 0
        self.main_color_value = 0
        self.quotient = 0
        self.border = 0.7
        self.is_accent = False

    def calc_accent_color(self, rgb_list):
        self.accent_color_value = rgb_list[self.accent_color]
        self.main_color_value = rgb_list[self.main_color]
        self.quotient = self.accent_color_value / self.main_color_value
        self.is_accent = self.quotient > self.border

    def output(self):
        return self.quotient, self.is_accent
