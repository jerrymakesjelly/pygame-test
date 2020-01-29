import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self, group)
        self.image = pygame.image.load('sprites/images/intro_ball.gif')
        self.rect = self.image.get_rect()
