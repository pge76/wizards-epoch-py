import pygame
from camera import CameraGroup
from settings import *
from player import Player
from spritesheet import Spritesheet
from tilemap import Tilemap


class Level:
    def __init__(self) -> None:
        # reference to display
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.setup()

    def setup(self):
        self.player: Player = Player((0, 0), self.all_sprites)
        spritesheet = Spritesheet('assets/tileset/background.png')
        self.background: Tilemap = Tilemap('map.csv', spritesheet)

    def run(self, dt):
        self.display_surface.fill('black')
        self.background.draw(self.display_surface)
        self.all_sprites.update(dt)
        self.all_sprites.custom_draw()
