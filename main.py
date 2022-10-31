import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        pygame.display.set_caption(TITLE)
        
    def run(self):
       while True:
           for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            dt = self.clock.tick(FRAMERATE) / 1000
            self.level.run(dt)
            pygame.display.update()
    
if __name__ == '__main__':
    game = Game()
    game.run()
        
                                              