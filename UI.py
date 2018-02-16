import pygame
import sys

from Controller import Controller

net = Controller()
learnrate = 0.05
print("Answer '#' to exit")

for i in range(100000000000000000):
    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    hex_code = net.ui_random_code()
    rgb_list = int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16)

    screen.fill(rgb_list)
    pygame.display.update()
    print(hex_code)
    result = net.predict(hex_code)


    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render(result[0], True, (0, 0, 0), rgb_list)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery

    screen.fill(rgb_list)
    screen.blit(text, textrect)

    pygame.display.update()


    answer = input('is that ' + result[0] + '?: Y/n')
    if answer in ['n', 'N', 'No', 'no']:
        if not result[1]:
            result[2].border -= learnrate
        else:
            result[2].border += learnrate
        print("test")
    elif answer == '#':
        for n in net.secondaryNs:
            for j in n:
                print(j.border)

        sys.exit()