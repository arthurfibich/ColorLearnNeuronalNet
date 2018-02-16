class SplittingNeuron:
    def __init__(self):
        self.main_color = 0
        self.accent_color = 0

    def calc_main_and_accent(self, rgb_list):
        for i in range(len(rgb_list)):
            if rgb_list[i] == max(rgb_list):
                self.main_color = i
        shortened_list = []
        for i in range(len(rgb_list)):
            if not i == self.main_color:
                shortened_list.append(i)
        if rgb_list[shortened_list[0]] > rgb_list[shortened_list[1]]:
            self.accent_color = shortened_list[0]

        else:
            self.accent_color = shortened_list[1]

    def output(self):
        return self.main_color, self.accent_color
