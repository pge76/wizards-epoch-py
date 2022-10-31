import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
        # general setup
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill("green")
        self.rect = self.image.get_rect(center = pos)
        
        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
    def input(self):
        print("input")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
    def move(self, dt):
        print("move", self.direction, dt)
        # normalize the direction vector
        if(self.direction.magnitude() > 0):
            self.direction = self.direction.normalize()
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos
        
    def update(self, dt):
        self.input()
        self.move(dt)