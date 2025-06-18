import pygame
from projectiles import Bullet
from random import randint

pygame.init()

screen = pygame.display.set_mode([800, 600])
background = pygame.image.load('game/assets/background1.png')

clock = pygame.time.Clock()

running = True

ship : pygame.Rect = pygame.Rect(600, 20, 50, 50)

shipimg = pygame.imag.load('game/assets/spaceship.img')
playerx = 370
playery = 480

def player():
    screen.blit(ship.img, (playerx, playery))

# rect2: pygame.Rect = pygame.Rect(600, 600, 50, 50)


while running:
    clock.tick(60)

    screen.fill((120, 200, 255))
    screen.blit(background, (0, 0))

    player()

    ship.x = pygame.mouse.get_pos()[0] - 25
    ship.y = pygame.mouse.get_pos()[1] - 25
    playerx = ship.x
    playery = ship.y

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                bullet = Bullet(400, 200, 10, 10)
                bullet.move()

        if event.type == pygame.QUIT:
            running = False


pygame.quit()