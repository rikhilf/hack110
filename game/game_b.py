import pygame
from game.projectiles import Bullet, Asteroid
from random import randint
import time
from typing import Union

pygame.init()

screen = pygame.display.set_mode([800, 600])
background = pygame.image.load('game/assets/background1.png')

clock = pygame.time.Clock()

start = time.time()

running = True

ship : pygame.Rect = pygame.Rect(600, 20, 50, 50)

shipimg = pygame.image.load('game/assets/spaceship.png')
playerx = ship.x
playery = ship.y

def player():
    screen.blit(shipimg, (playerx, playery))

# hearts and their locations
h1 = pygame.image.load('game/assets/heart.png')
h2 = h1
h3 = h1
lives: int = 3
bullet: list[pygame.Rect] = list()
hearts: list = [1, 1, 1]

blt: list[Bullet] = list()  # Bullet(randint(0, 600), randint(0, 600), 10, 10)
# rect: pygame.Rect = blt.getRect()
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
    
    

    
    for item in blt:
        rect: pygame.Rect = item.getRect()
        rect2: pygame.Rect = item.getRect()
        rect_goodbad: bool = False
        rect2_goodbad: bool = False
        if item.vector[1] == -1:
            pygame.draw.rect(screen, (0, 0, 0), rect)
            rect_goodbad = False
        else:
            pygame.draw.rect(screen, (255, 255, 255), rect2)
            rect2_goodbad = True
        

        fire_hit: bool = (rect2.colliderect(rect)) and (not (rect2_goodbad == rect_goodbad))
        ship_hit: bool = (rect.colliderect(ship)) and (not (rect2_goodbad == rect_goodbad))

        

        # if fire_hit:
        #      blt.remove(item)
        if ship_hit:
            blt.remove(item)
            lives -= 1
            hearts.pop()
            # if lives == 2:
            #     h3 = ""
            # elif lives == 1: 
            #     h2 = ""
            # elif lives == 0:
            #     h1 = ""
            
        if lives == 0: 
            running = False


        item.move()




    ticks: list[int] = list()
    ticks.append(pygame.time.get_ticks())
    for event in pygame.event.get():
        fired: bool = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                blt.append(Bullet(ship.x, ship.y - 25, 10, 10, 1, [0, -1]))
                # for i in range(0, len(blt)):
                #     bullet.append(pygame.Rect(blt[i].x, blt[i].y, 50, 50))
                
                fired = True
        

        if event.type == pygame.QUIT:
            running = False
    for tick in ticks:
            if tick % 11 == 0:
                blt.append(Bullet(randint(0, 800), 1, 5, 7, 0, [0, 1]))

    pygame.display.flip()
        

end = time.time()
print(f"score: {end - start}")

pygame.quit()