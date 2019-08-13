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
        print(self.rect.x)
        print(self.rect.y)

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        if keystate[pygame.K_SPACE]:
            print('moving up')
            self.isJumping = 1
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        self.playerJump()

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
            print(self.velocity)
        
            #Checking is ground has been reached
            if(self.rect.y >= 490):
                self.isJumping = 0
                self.velocity = 8
                print('jump set to 0')
     
    def shoot(self,all_sprites,bullets):
        bullet = Bullet(self.rect.x, self.rect.y)
        all_sprites.add(bullet)
        bullets.add(bullet)