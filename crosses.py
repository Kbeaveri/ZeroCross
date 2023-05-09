import pygame.image


class crosses:
    def __init__(self):
        self.cross = pygame.image.load('image/Cross.png')
    def drow(self,screen,pos):
        screen.blit(self.cross, pos)