import colorsys


class Trainer:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0

        self.h = 0
        self.s = 0
        self.v = 0

        self.red = 0
        self.green = 120
        self.blue = 240

        self.yellow = 60
        self.cyan = 180
        self.magenta = 300

        self.orange = 30

        self.redd = 0
        self.greend = 0
        self.blued = 0

        self.yellowd = 0
        self.cyand = 0
        self.magentad = 0

        self.oranged = 0

        self.min_dif = 360
        self.answer = ""

    def result(self, hex_code):
        self.r = int(hex_code[0:2], 16)
        self.g = int(hex_code[2:4], 16)
        self.b = int(hex_code[4:6], 16)
        self.h, self.s, self.v = colorsys.rgb_to_hsv(self.r/255, self.g/255, self.b/255)
        self.h *= 360
        self.s *= 100
        self.v *= 100
        self.redd = abs(self.red - self.h)
        self.greend = abs(self.green - self.h)
        self.blued = abs(self.blue - self.h)
        self.yellowd = abs(self.yellow - self.h)
        self.cyand = abs(self.cyan - self.h)
        self.magentad = abs(self.magenta - self.h)
        self.oranged = abs(self.orange - self.h)
        color_diffs = [self.blued, self.redd, self.greend, self.yellowd, self.magentad, self.cyand, self.oranged]
        name_list = ["blue", "red", "green", "yellow", "magenta", "cyan", "orange"]
        white_chance = 100 - self.s
        black_chance = 100 - self.v
        maximum = min(color_diffs)
        for i in range(len(color_diffs)):
            if color_diffs[i] == maximum:
                return name_list[i], maximum, white_chance, black_chance

    def check_result(self, hex_code, answer):
        answer_list = self.result(hex_code)
        # print(answer_list[0])
        if answer_list[0] == answer or (answer == "white" and answer_list[2] <= 80) or (answer == "black" and answer_list[3] <= 80) or answer == "gray":
            return True, answer_list[0]
        return False, answer_list[0]

if __name__ == "__main__":
    t = Trainer()
    print(t.result("ffffff"))