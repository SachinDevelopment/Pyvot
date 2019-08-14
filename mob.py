import random
import pygame
from configs import *

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange((WIDTH / 2 + 100),(WIDTH / 2 + 800))
        self.rect.bottom = HEIGHT - 20
        self.speedy = 5
        self.speedx = 5
        self.health = 100

    def update(self):
        self.rect.x-=random.randrange(1,2)
        #self.rect.y = random.randrange(500, 700)
        # self.rect.x += self.speedx
        # self.rect.y += self.speedy
        # self.rect.x = random.randrange(700,800)
        # self.rect.y = random.randrange(500, 700)
        # self.speedy = random.randrange(1, 8)


        self.draw()
        
    def draw_health(self):
        width = int(self.rect.width * self.health / 100)
        width_full = int(self.rect.width)
        self.health_bar = pygame.Rect(0, 0, width, 7)
        self.health_bar_full = pygame.Rect(0, 0, width_full, 7)
        pygame.draw.rect(self.image, (255,0,0), self.health_bar_full)
        pygame.draw.rect(self.image, (0,255,0), self.health_bar)
        
    def draw(self):
        self.draw_health()
    
        
        # self.rect.x += self.speedx
        # self.rect.y += self.speedy
        # if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
        #     self.rect.x = random.randrange(WIDTH - self.rect.width)
        #     self.rect.y = random.randrange(-100, -40)
        #     self.speedy = random.randrange(1, 8)