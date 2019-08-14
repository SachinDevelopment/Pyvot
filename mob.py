import random
import pygame
from configs import *

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 80))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange((WIDTH / 2 + 100),(WIDTH / 2 + 600))
        self.rect.bottom = HEIGHT - 20
        self.speedy = 5
        self.speedx = 5
        self.health = 100

    def update(self):
        self.rect.x-=random.randrange(2,4)
        self.draw()

    
    def isOutOfBounds(self):
        if self.rect.x <= WIDTH / 8:
            self.kill()
            print("killing mob")
            return True
        else:
            return False

    def isDead(self):
        if(self.health <= 0):
            print("killing mob")
            self.kill()
            return True
        else:
            return False

    def takeDamage(self):
        print(self.health)
        self.health-=10
       
    def draw_health(self):
        width = int(self.rect.width * self.health / 100)
        width_full = int(self.rect.width)
        self.health_bar = pygame.Rect(0, 0, width, 7)
        self.health_bar_full = pygame.Rect(0, 0, width_full, 7)
        pygame.draw.rect(self.image, (255,0,0), self.health_bar_full)
        pygame.draw.rect(self.image, (0,255,0), self.health_bar)
        
    def draw(self):
        self.draw_health()
    