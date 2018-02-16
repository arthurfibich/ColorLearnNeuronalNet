import colorsys
import random
from datetime import datetime

import math

from InputNeuron import InputNeuron
from RGBNeuron import RGBNeuron
from SplittingNeuron import SplittingNeuron
from SecondaryNeuron import SecondaryNeuron
from Trainer import Trainer

class Controller:

    def __init__(self):

        self.inputN = InputNeuron()
        self.redN = RGBNeuron()
        self.greenN = RGBNeuron()
        self.blueN = RGBNeuron()
        self.spN = SplittingNeuron()
        self.secondaryNs = [[SecondaryNeuron(0, 0), SecondaryNeuron(0, 1), SecondaryNeuron(0, 2)], [SecondaryNeuron(1, 0), SecondaryNeuron(1, 1), SecondaryNeuron(1, 2)], [SecondaryNeuron(2, 0), SecondaryNeuron(2, 1), SecondaryNeuron(2, 2)]]

    def get_color_name(self, main_color, accent_color, is_accent):
        main_colors = ["red", "green", "blue"]
        accent_colors = ["yellow", "cyan", "magenta"]

        if not is_accent:
            return main_colors[main_color]
        else:
            if (main_color * accent_color) == 2:
                return accent_colors[1]
            elif (main_color * accent_color) == 0:
                if (main_color + accent_color) == 1:
                    return accent_colors[0]
                else:
                    return accent_colors[2]

    def predict(self, code):
        r = 0
        g = 1
        b = 2
        self.inputN.set_values(code)
        print(self.inputN.output())
        self.redN.calc_prob(self.inputN.output(), r)
        self.greenN.calc_prob(self.inputN.output(), g)
        self.blueN.calc_prob(self.inputN.output(), b)
        print(self.redN.output())
        print(self.greenN.output())
        print(self.blueN.output())
        self.spN.calc_main_and_accent(self.inputN.output())
        print(self.spN.output())
        secN = self.secondaryNs[self.spN.output()[0]][self.spN.output()[1]]
        secN.calc_accent_color(self.inputN.output())
        print(secN.output())
        print(secN.border)
        print(self.get_color_name(self.spN.output()[0], self.spN.output()[1], secN.output()[1]))
        return self.get_color_name(self.spN.output()[0], self.spN.output()[1], secN.output()[1]), secN.output()[1], secN

    def random_code(self):
        return ''.join(random.choice('0123456789abcdef') for n in range(6))

    def ui_random_code(self):

        h = random.randint(0, 360)
        r, g, b = colorsys.hsv_to_rgb(h/360, 1, 1)
        return '%02x%02x%02x' % (int(255*r), int(255*g), int(255*b))


if __name__ == "":
    starting_time = datetime.now()
    trainer = Trainer()
    net = Controller()
    runs = 1000000
    learnrate = 0.1
    trues = 0
    for i in range(runs):
        code = net.random_code()
        try:
            prediction = net.predict(code)
        except:
            print("OOPS!!!")
        result = trainer.check_result(code, prediction[0])
        print(prediction)
        print(result)
        if math.log(i + 1, 10) % 1 == 0 and i > 10:
            learnrate /= 100
        if (result[0] or result[1] == 'orange') and i > (runs - 100):
            trues += 1
        else:
            if not prediction[1]:
                prediction[2].border -= learnrate
            else:
                prediction[2].border += learnrate

    quote = trues / 100
    print(quote)
    ending_time = datetime.now()
    print(learnrate)
    for n in net.secondaryNs:
        for j in n:
            print(j.border)
    print(ending_time - starting_time)
    print(-math.log(1-quote, 2))


if __name__ == "__main__":
    net = Controller()
    print(net.ui_random_code())
