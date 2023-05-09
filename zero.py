import pygame


class zero:
    def __init__(self):
        self.zero = pygame.image.load('image/zero.png')
    def drow(self,screen, pos):
        screen.blit(self.zero, pos)