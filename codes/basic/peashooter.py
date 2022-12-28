import pygame


class PeaShooter:

    def __init__(self):
        self.image = pygame.image.load('res/image/peashooter.png')
        self.pos = 200, 100

    def draw(self, surf):
        surf.blit(self.image, self.pos)
