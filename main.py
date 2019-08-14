import pygame
import random
from mob import Mob
from bullet import Bullet
from player import Player
from configs import *

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()

player = Player()
all_sprites.add(player)


for i in range(1):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(all_sprites,bullets)

    # Update
    all_sprites.update()

    #check for mob and bullet collision. If mob dies spawn a new one and add to sprite group
    #also now checking for out of bounds
    for mob in mobs:
        if(mob.isOutOfBounds()):
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

        hits = pygame.sprite.spritecollide(mob, bullets, True)
        if hits:
            mob.takeDamage()
            if(mob.isDead()):
                m = Mob()
                all_sprites.add(m)
                mobs.add(m)

 
    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        player.health-=10

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #update the display
    pygame.display.flip()

pygame.quit()