import pygame
from blocks.grass import Grass
from blocks.stone import Stone
from blocks.darkStone import BlackStone
from blocks.semiDarkStone import SemiDarkStone
from miners.demtreuisdemarcusdejamesdathird import DemtreuisDemarcusDejamesDathird
from miners.jerome import Jerome
from miners.ash import Ash
from miners.head import Head
from miners.blockyguy import BlockyGuy
from buildings.cashmoney import CashMoneyBuilding
from carts.cartempty import CartEmpty
from buildings.pumpypump import PumpyPump
from buildings.elevator import Elevator
from miners.fatguy import FatGuy
from map import TILESIZE


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.ground = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.blackPpl = pygame.sprite.Group()
        self.bitches = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()
        self.carts = pygame.sprite.Group()
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
                if cell == 'C':
                    empty_cart = CartEmpty((x, y), TILESIZE)
                    self.carts.add(empty_cart)
                if cell == 'D':
                    dark_stone = SemiDarkStone((x, y), TILESIZE)
                    self.blocks.add(dark_stone)
                if cell == 'U':
                    pumpy = PumpyPump((x, y), TILESIZE * 3)
                    self.buildings.add(pumpy)
                if cell == 'E':
                    elevator = Elevator((x, y), TILESIZE * 5)
                    self.buildings.add(elevator)

    def run(self):
        self.ground.draw(self.display_surface)
        self.blocks.draw(self.display_surface)
        self.blackPpl.draw(self.display_surface)
        self.bitches.draw(self.display_surface)
        self.buildings.draw(self.display_surface)
        self.carts.draw(self.display_surface)
