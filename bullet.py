import random
import pygame
from configs import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x + 30
        self.rect.y = y + 30
        self.speedy = 10

    def update(self):
        self.rect.x += self.speedy
        #print(self.rect.x)
        #print(self.rect.y)
        # kill if it moves off the top of the screen
        if self.rect.x > WIDTH:
            #print("killed")
            self.kill()