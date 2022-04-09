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
blt: list[Bullet] = list()  # Bullet(randint(0, 600), randint(0, 600), 10, 10)
# rect: pygame.Rect = blt.getRect()
while running:
    clock.tick(60)

    screen.fill((120, 200, 255))
    # screen.blit(background, (0, 0))
    # pygame.draw.rect(screen, (150, 10, 245), rect)
    # pygame.draw.rect(screen, (150, 10, 245), rect2)

   
    # pygame.display.flip()
    for item in blt:
        rect: pygame.Rect = item.getRect()
        pygame.draw.rect(screen, (255,255,255), rect)
        
        hit: bool = rect.colliderect(rect)
        if hit:
            blt.remove(item)
        item.move()
        # if hit:
        #     bullet.remove(blt)

    for event in pygame.event.get():
        fired: bool = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                
                blt.append(Bullet(randint(0, 600), randint(0, 600), 10, 10))
                for i in range(0, len(blt)):
                    bullet.append(pygame.Rect(blt[i].x, blt[i].y, 50, 50))
                
                fired = True
        
                
            

        if event.type == pygame.QUIT:
            running = False
    # blt.move()
    pygame.display.flip()
        


pygame.quit()