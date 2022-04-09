import pygame
from game.projectiles import Bullet
from random import randint

pygame.init()

screen = pygame.display.set_mode([800, 600])

# background = pygame.image.load('assets/background1.png')

clock = pygame.time.Clock()

running = True

# rect: pygame.Rect = pygame.Rect(600, 20, 50, 50)

# rect2: pygame.Rect = pygame.Rect(600, 600, 50, 50)

bullet: list[pygame.Rect] = list()
blt = Bullet(600, 20, 10, 10)
rect: pygame.Rect = blt.getRect()
while running:
    clock.tick(60)

    screen.fill((120, 200, 255))
    # screen.blit(background, (0, 0))
    # pygame.draw.rect(screen, (150, 10, 245), rect)
    # pygame.draw.rect(screen, (150, 10, 245), rect2)

   
    # pygame.display.flip()
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                
                
                for item in bullet:
                    pygame.draw.rect(screen, (255,255,255), rect)
                
                bullet.append(pygame.Rect(600, 20, 50, 50))
                
            

        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
        


pygame.quit()