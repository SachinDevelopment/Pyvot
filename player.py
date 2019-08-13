import random
import pygame
from configs import *
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 100))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.velocity = 8
        self.isJumping = 0
        self.mass = 3
        self.health = 100

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        if keystate[pygame.K_SPACE]:
            self.isJumping = 1
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        self.playerJump()
        self.draw_health()

    def playerJump(self):   
        #calc force
        #print('jump method initiated')
        if self.isJumping:
            if self.velocity > 0:
                force = (.5 * self.mass * self.velocity**2)
            else:
                force = -(.5 * self.mass * self.velocity**2)
                #change pos
            self.rect.y-=force
        
            #change velocity
            self.velocity-=1
        
            #Checking is ground has been reached
            if(self.rect.y >= 490):
                self.isJumping = 0
                self.velocity = 8

    def draw_health(self):
        if self.health > 66:
            col = (0,255,0)
        elif self.health > 33:
            col = (255,255,0)
        else:
            col = (255,0,0)
        width = int(self.rect.width * self.health / 100)
        print(self.health)
        self.health_bar = pygame.Rect(0, 0, width, 7)
        if self.health <= 100:
            pygame.draw.rect(self.image, col, self.health_bar)


    def shoot(self,all_sprites,bullets):
        bullet = Bullet(self.rect.x, self.rect.y)
        all_sprites.add(bullet)
        bullets.add(bullet)