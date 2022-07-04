from __future__ import annotations
import pygame
from typing import Optional

blt: list[Bullet] = list()  # Bullet(randint(0, 600), randint(0, 600), 10, 10)
ast: list[Asteroid] = list()
astList: list[pygame.Rect] = list()
bltList: list[pygame.Rect] = list()

class Bullet:
    x: int
    y: int
    radius: int
    speed: float
    vector: list[float]
    #goodbad: int

    def __init__(self, x_pos: int, y_pos: int, radius: int, speed: float, vector: list[float] = [0,1]):
        self.x = x_pos
        self.y = y_pos
        self.radius = radius
        self.speed = speed
        self.vector = vector

    def move(self): 
        self.x += (self.vector[0] * self.speed)
        self.y += (self.vector[1] * self.speed)

    def getBullet(self) -> pygame.Rect:
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 10, 10)



class Asteroid:
    x: int
    y: int
    radius: int
    speed: float
    vector: list[float]
    #goodbad: int

    def __init__(self, x_pos: int, y_pos: int, radius: int, speed: float, vector: list[float] = [0,1]):
        self.x = x_pos
        self.y = y_pos
        self.radius = radius
        self.speed = speed
        self.vector = vector

    def move(self): 
        self.x += (self.vector[0] * self.speed)
        self.y += (self.vector[1] * self.speed)

    def getAst(self) -> pygame.Rect:
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 20, 20)

    def generator(self):
        stroid: pygame.Rect = self.getAst()

    def shipCollision(self):
        ast.remove(self)