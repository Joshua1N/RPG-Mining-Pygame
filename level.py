import pygame
from blocks.grass import Grass
from blocks.stone import Stone
from map import TILESIZE


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.ground = pygame.sprite.Group()
        self.rocks = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if cell == '1':
                    grass = Grass((x, y), TILESIZE)
                    self.ground.add(grass)
                if cell == '2':
                    stone = Stone((x, y), TILESIZE)
                    self.rocks.add(stone)

    def run(self):
        self.ground.draw(self.display_surface)
        self.rocks.draw(self.display_surface)
