import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # general setup
        self.image: pygame.Surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill("green")

        self.rect: pygame.Rect = self.image.get_rect(center=pos)

        # movement attributes
        self.direction: pygame.math.Vector2 = pygame.math.Vector2()
        self.pos: pygame.math.Vector2 = pygame.math.Vector2(self.rect.center)
        self.speed: int = 200

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
        if (self.direction.magnitude() > 0):
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)
