import random
import pygame
from configs import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        print(pygame.mouse.get_pos())
        print(x,y)
        x2,y2 = pygame.mouse.get_pos()
        self.rect.x = x + 30
        self.rect.y = y + 30
        self.speedx = 10
        #self.speedy = 30
    
    def update(self):

        self.rect.x += self.speedx
        #self.rect.y -= self.speedy
        if self.rect.x > WIDTH:
            #print("killed")
            self.kill()