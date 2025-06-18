import pygame
from projectiles_rewrite.proj_rewrite import Bullet, Asteroid, blt, ast, bltList, astList

from random import randint
import time

from typing import Optional


pygame.init()

running = True

start = time.time()

screen = pygame.display.set_mode([800, 600])
background = pygame.image.load('assets/background1.png')

clock = pygame.time.Clock()

ship : pygame.Rect = pygame.Rect(600, 20, 50, 50)
shipimg = pygame.image.load('assets/spaceship.png')

playerx = ship.x
playery = ship.y

def player():
    screen.blit(shipimg, (playerx, playery))

# hearts and their locations
h1 = pygame.image.load('assets/heart.png')
h2 = h1
h3 = h1
lives: int = 3
hearts: list = [1, 1, 1]


while running:
    clock.tick(60)

    screen.fill((120, 200, 255))
    screen.blit(background, (0, 0))

    if len(hearts) >= 1:
        screen.blit(h1, (50, 550))
    if len(hearts) >= 2: 
        screen.blit(h2, (100, 550))
    if len(hearts) >= 3:
        screen.blit(h3, (150, 550))
    
    player()


    ship.x = pygame.mouse.get_pos()[0] - 25
    ship.y = pygame.mouse.get_pos()[1] - 25
    playerx = ship.x
    playery = ship.y

    

    for item in blt[:]:
        # if bullet is off the screen, remove it
        if item.y < 0 or item.x < 0 or item.x > 800 or item.y > 600:
            blt.remove(item)

        bull: pygame.Rect = item.getBullet()
        bltList.append(bull)

       
        pygame.draw.rect(screen, (0, 0, 0), bull)

        for asteroid in ast[:]:
            if bull.colliderect(asteroid.getAst()):
                ast.remove(asteroid)

        item.move()


    # TODO: add checks for collisions

    for item in ast[:]:
        # if asteroid is off the screen, remove it
        if item.y > 600 or item.x < 0 or item.x > 800:
            ast.remove(item)
        stroid: pygame.Rect = item.getAst()
        astList.append(stroid)

        pygame.draw.rect(screen, (255, 255, 255), stroid)
        
        if stroid.colliderect(ship):
            item.shipCollision()
            lives -= 1
            hearts.pop()
        
        # for bullet in blt:
        #     if stroid.colliderect(bullet):
        #         ast.remove(stroid)
        if stroid not in astList:
            ast.remove(stroid)


        item.move()

    if lives == 0:
        running = False



    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                blt.append(Bullet(ship.x, ship.y - 25, 10, 10, [0,-1]))


        if event.type == pygame.QUIT:
            running = False


    ticks: list[int] = list()
    ticks.append(pygame.time.get_ticks())
    for tick in ticks:
        if tick % 11 == 0:
            ast.append(Asteroid(randint(0, 800), 1, 5, 7, [0, 1]))

    pygame.display.flip()


end = time.time()
print(f"score: {end - start}")
pygame.quit()