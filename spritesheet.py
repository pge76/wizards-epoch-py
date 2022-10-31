import pygame
import json
from spritedef import sprites
from settings import *


class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        sprite = sprites[name]
        x, y, w, h = sprite['x'] * TILE_SIZE, sprite['y'] * \
            TILE_SIZE, TILE_SIZE, TILE_SIZE
        image = self.get_sprite(x, y, w, h)
        return image
