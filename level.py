#imports
import pygame
from blocks.grass import Grass
from blocks.stone import Stone
from blocks.darkStone import BlackStone
from blocks.semiDarkStone import SemiDarkStone
from buildings.cashmoney import CashMoneyBuilding
from buildings.pumpypump import PumpyPump
from ores.coal import Coal
from ores.iron import Iron
from ores.gold import Gold
from ores.diamond import Diamond
from ores.bitcoin import Bitcoin
from map import TILESIZE

#initializes the level
class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
#placing still objects on the tile map
    def setup_level(self, layout):
        self.ground = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.blackPpl = pygame.sprite.Group()
        self.bitches = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()
        self.ores = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if cell == '1':
                    grass = Grass((x, y), TILESIZE)
                    self.ground.add(grass)
                if cell == '2':
                    stone = Stone((x, y), TILESIZE)
                    self.blocks.add(stone)
                if cell == '3':
                    jewishppl = BlackStone((x, y), TILESIZE)
                    self.blackPpl.add(jewishppl)
                if cell == 'B':
                    cash_building = CashMoneyBuilding((x, y), TILESIZE * 4)
                    self.buildings.add(cash_building)
                if cell == 'Z':
                    dark_stone = SemiDarkStone((x, y), TILESIZE)
                    self.blocks.add(dark_stone)
                if cell == 'U':
                    pumpy = PumpyPump((x, y), TILESIZE * 3)
                    self.buildings.add(pumpy)
                if cell == '5':
                    coal = Coal((x, y), TILESIZE * 2)
                    self.ores.add(coal)
                if cell == '6':
                    iron = Iron((x, y), TILESIZE * 2)
                    self.ores.add(iron)
                if cell == '7':
                    gold = Gold((x, y), TILESIZE * 2)
                    self.ores.add(gold)
                if cell == '8':
                    diamond = Diamond((x, y), TILESIZE * 2)
                    self.ores.add(diamond)
                if cell == '9':
                    bitcoin = Bitcoin((x, y), TILESIZE * 2)
                    self.ores.add(bitcoin)

    def run(self):
        self.ground.draw(self.display_surface)
        self.blocks.draw(self.display_surface)
        self.blackPpl.draw(self.display_surface)
        self.bitches.draw(self.display_surface)
        self.buildings.draw(self.display_surface)
        self.ores.draw(self.display_surface)
