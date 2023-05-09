import sys
import time

import pygame
from pygame.color import THECOLORS

from crosses import crosses
from zero import zero


class Game:
    def __init__(self):
        pygame.init()
        self.Line = [(0, 0), (0, 0)]
        self.score = (0, 0)
        self.cross = crosses()
        self.zero = zero()
        self.font = pygame.font.SysFont('couriernew', 40)
        self.new_ground()

    def new_ground(self):
        self.area = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.winner = False
        self.counter = 0
        self.area_pos = [[(20, 20), (20, 260), (20, 500)], [(260, 20), (260, 260), (260, 500)],[(500, 20), (500, 260), (500, 500)]]
        self.queue = False
        self.x = 1
        self.y = 1
        self.screen = pygame.display.set_mode((1280, 720))
        color = (255, 255, 255)
        line_color = (0, 0, 0)
        self.screen.fill(color)
        pygame.draw.line(self.screen, line_color, (0, 0), (0, 720), width=20)
        pygame.draw.line(self.screen, line_color, (0, 0), (720, 0), width=20)
        pygame.draw.line(self.screen, line_color, (0, 720), (720, 720), width=20)
        pygame.draw.line(self.screen, line_color, (720, 0), (720, 720), width=20)
        pygame.draw.line(self.screen, line_color, (240, 0), (240, 720), width=20)
        pygame.draw.line(self.screen, line_color, (480, 0), (480, 720), width=20)
        pygame.draw.line(self.screen, line_color, (0, 240), (720, 240), width=20)
        pygame.draw.line(self.screen, line_color, (0, 480), (720, 480), width=20)
        self.restart_text = self.font.render(str('Начать заново'), True, THECOLORS['black'])
        self.screen.blit(self.restart_text, (800, 200))
        self.restart_text_rect = self.restart_text.get_rect(topleft = (800,200))
        pygame.display.flip()
        self.run()
    def find(self, pos):
        if pos[0] < 240:
            self.x = 0
        elif pos[0] < 480:
            self.x = 1
        elif pos[0] < 720:
            self.x = 2
        else:
            self.x = -1
            self.y = -1
            return
        if pos[1] < 240:
            self.y = 0
        elif pos[1] < 480:
            self.y = 1
        elif pos[1] < 720:
            self.y = 2
        else:
            self.y = -1
            self.x = -1

    def check_win(self):
        number = self.area[self.x][self.y]
        if self.x == 0:
            if self.y == 0:
                if self.area[1][1] == number and self.area[2][2] == number:
                    self.Line = [(0, 0), (720, 720)]
                    return True
                if self.area[1][0] == number and self.area[2][0] == number:
                    self.Line = [(0, 110), (720, 110)]
                    return True
                if self.area[0][1] == number and self.area[0][2] == number:
                    self.Line = [(120, 0), (120, 720)]
                    return True
            if self.y == 1:
                if self.area[1][1] == number and self.area[2][1] == number:
                    self.Line = [(0, 360), (720, 360)]
                    return True
                if self.area[0][0] == number and self.area[0][2] == number:
                    self.Line = [(120, 0), (120, 720)]
                    return True
            if self.y == 2:
                if self.area[1][1] == number and self.area[2][0] == number:
                    self.Line = [(0, 720), (720, 0)]
                    return True
                if self.area[0][0] == number and self.area[0][1] == number:
                    self.Line = [(120, 0), (120, 720)]
                    return True
                if self.area[1][2] == number and self.area[2][2] == number:
                    self.Line = [(0, 600), (720, 600)]
                    return True
        if self.x == 1:
            if self.y == 0:
                if self.area[1][1] == number and self.area[1][2] == number:
                    self.Line = [(360, 0), (360, 720)]
                    return True
                if self.area[0][0] == number and self.area[2][0] == number:
                    self.Line = [(0, 110), (720, 110)]
                    return True
            if self.y == 1:
                if self.area[0][0] == number and self.area[2][2] == number:
                    self.Line = [(0, 0), (720, 720)]
                    return True
                if self.area[2][0] == number and self.area[0][2] == number:
                    self.Line = [(0, 720), (720, 0)]
                    return True
                if self.area[1][0] == number and self.area[1][2] == number:
                    self.Line = [(360, 0), (360, 720)]
                    return True
                if self.area[0][1] == number and self.area[2][1] == number:
                    self.Line = [(0, 360), (720, 360)]
                    return True
            if self.y == 2:
                if self.area[1][1] == number and self.area[1][0] == number:
                    self.Line = [(360, 0), (360, 720)]
                    return True
                if self.area[0][2] == number and self.area[2][2] == number:
                    self.Line = [(0, 600), (720, 600)]
                    return True
        if self.x == 2:
            if self.y == 0:
                if self.area[1][1] == number and self.area[0][2] == number:
                    self.Line = [(0, 720), (720, 0)]
                    return True
                if self.area[1][0] == number and self.area[0][0] == number:
                    self.Line = [(0, 110), (720, 110)]
                    return True
                if self.area[2][1] == number and self.area[2][2] == number:
                    self.Line = [(600, 0), (600, 720)]
                    return True
            if self.y == 1:
                if self.area[1][1] == number and self.area[0][1] == number:
                    self.Line = [(0, 360), (720, 360)]
                    return True
                if self.area[2][0] == number and self.area[2][2] == number:
                    self.Line = [(0, 600), (720, 600)]
                    return True
            if self.y == 2:
                if self.area[1][1] == number and self.area[0][0] == number:
                    self.Line = [(0, 0), (720, 720)]
                    return True
                if self.area[2][0] == number and self.area[2][1] == number:
                    self.Line = [(600, 0), (600, 720)]
                    return True
                if self.area[1][2] == number and self.area[0][2] == number:
                    self.Line = [(0, 600), (720, 600)]
                    return True
        return False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.find(event.pos)
                    if self.restart_text_rect.collidepoint(event.pos):
                        self.new_ground()
                    if self.counter == 9:
                        self.restart_menu()
                    try:
                        if self.y != -1 and self.x != -1:
                            if self.area[self.x][self.y] == -1:
                                if not self.queue:
                                    self.area[self.x][self.y] = 0
                                    self.cross.drow(self.screen, self.area_pos[self.x][self.y])
                                    pygame.display.flip()
                                    self.counter += 1
                                    if self.check_win():
                                        self.winner = True
                                        self.win()
                                    else:
                                        self.queue = True
                                        continue
                                if self.queue:
                                    self.area[self.x][self.y] = 1
                                    self.zero.drow(self.screen, self.area_pos[self.x][self.y])
                                    pygame.display.flip()
                                    self.counter += 1
                                    if self.check_win():
                                        self.winner = True
                                        self.win()
                                    else:
                                        self.queue = False
                    except IndexError:
                        print("Игрок промазал по полю")
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def win(self):
        text = self.font.render(str('Победитель:'), True, THECOLORS['black'])
        self.screen.blit(text, (800, 500))
        pygame.draw.line(self.screen, THECOLORS['black'], self.Line[0], self.Line[1], width=50)
        if not self.queue:
            self.cross.drow(self.screen, (1050, 500))
        else:
            self.zero.drow(self.screen, (1050, 500))
        pygame.display.flip()
        time.sleep(3)
        self.restart_menu()

    def restart_menu(self):
        while True:
            for event in pygame.event.get():
                restart_font = pygame.font.SysFont('couriernew', 60)
                self.screen.fill(THECOLORS['grey'])
                text = restart_font.render(str('Победитель:'), True, THECOLORS['black'])
                self.screen.blit(text, (300, 220))
                restart_text = restart_font.render(str('Нaчать заново? '), True, THECOLORS['black'])
                self.screen.blit(restart_text, (300, 320))
                restart_text_rect = restart_text.get_rect(topleft = (300, 320))
                mouse = pygame.mouse.get_pos()
                if self.counter == 9 and self.winner == False:
                    text = restart_font.render(str('Ничья'), True, THECOLORS['black'])
                    self.screen.blit(text, (800, 220))
                else:
                    if self.queue == False:
                        self.cross.drow(self.screen, (700, 120))
                    else:
                        self.zero.drow(self.screen, (700, 120))
                pygame.display.flip()
                if restart_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    self.new_ground()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()