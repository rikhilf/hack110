import pygame

class Bullet:
        x: int
        y: int
        radius: int
        speed: float
        vector: list[float]
        goodbad: int

        def __init__(self, x_pos: int, y_pos: int, radius: int, speed: float, goodbad: int, vector: list[float] = [0,1]):
                self.x = x_pos
                self.y = y_pos
                self.radius = radius
                self.speed = speed
                self.vector = vector
                self.goodbad = goodbad
                


        def move(self):
                self.x += (self.vector[0] * self.speed)
                self.y += (self.vector[1] * self.speed)

        
        def getRect(self) -> pygame.Rect:
                return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 3, self.radius * 3)

class Asteroid:
        x: int
        y: int
        radius: int
        speed: float
        vector: list[float]

        def __init__(self, x_pos: int, y_pos: int, radius: int, speed: float, vector: list[float] = [0,1]):
                self.x = x_pos
                self.y = y_pos
                self.radius = radius
                self.speed = speed
                self.vector = vector
                


        def move(self):
                self.x += (self.vector[0] * self.speed)
                self.y += (self.vector[1] * self.speed)

        
        def getRect(self) -> pygame.Rect:
                return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 3, self.radius * 3)
