# Mining Min rs | Joshua, Diego, Patrick, Liza, Keegan | Version: 4.2.69 | Project Ended: 3/8/2022
#totally origanal idea


# IMPORTS
import pygame, sys
from map import *
from level import Level
from miners.ash import *
from miners.blockyguy import *
from miners.jerome import *
from miners.demtreuisdemarcusdejamesdathird import *
from miners.head import *
from buildings.elevator import Elevator
from carts.cartcoal import Cart

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
vec = pygame.math.Vector2

# GAME CLASS / START VARIABLES / CALLING ON SPRITE CLASSES
class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.level = Level(map, screen)
        self.loaded = False
        self.coins = 20000
        self.minespeed = 100
        self.upgrades = 10
        self.unlocked = 1
        self.shaft_upgrade = 250
        self.cart_level = 1

        self.load()

# RUN CERTAIN FUNCTIONS DEPENDING ON GAME STATE
    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
                self.test()

            elif self.state == 'help':
                # How to play page here
                pass
            else:
                self.running = False
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    ############### HELPER FUNCTIONS ###############

    def draw_text(self, words, screen, pos, size, color, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        pos[0] = pos[0] - text_size[0] / 2
        pos[1] = pos[1] - text_size[1] / 2
        screen.blit(text, pos)

    def load(self):
        # START SCREEN
        self.title = pygame.image.load(
            'C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/Title.png').convert_alpha()
        self.title = pygame.transform.scale(self.title, (800, 150)).convert_alpha()
        self.start_button = pygame.image.load(
            'C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/Play-Button.png').convert_alpha()
        self.start_button_rect = self.start_button.get_rect(center=(680, 400))
        self.start_button = pygame.transform.scale(self.start_button, (400, 75)).convert_alpha()
        self.exit_button = pygame.image.load(
            'C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/Exit.png').convert_alpha()
        self.exit_button = pygame.transform.scale(self.exit_button, (400, 75)).convert_alpha()
        self.exit_button_rect = self.exit_button.get_rect(center=(680, 600))
        self.howtoplay_button = pygame.image.load(
            'C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/HowToPlay.png').convert_alpha()
        self.howtoplay_button = pygame.transform.scale(self.howtoplay_button, (500, 100)).convert_alpha()
        self.howtoplay_button_rect = self.howtoplay_button.get_rect(center=(650, 800))
        self.corner_logo = pygame.image.load(
            'C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/Title.png')
        self.corner_logo = pygame.transform.scale(self.corner_logo, (300, 100))
        self.background = pygame.image.load('C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/Sky.png')
        self.background = pygame.transform.scale(self.background, (WIDTH, 270))
        self.shaft = pygame.image.load('C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/mineshaft.png')
        self.new_shaft = pygame.transform.scale(self.shaft, (WIDTH, 270))


        # Miners
        self.ash = Ash('ash', 440, 325, 5)
        self.blocky_guy = BlockyGuy('blockyguy', 440, 485, 5)
        self.jerome = Jerome('jerome', 440, 810, 5)
        self.demtreuis_demarcus_dejames_dathird = DemtreuisDemarcusDejamesDathird('DemtreuisDemarcusDejamesDathird',
                                                                                  440, 645, 3)
        self.head = Head('head', 440, 970, 5)
        self.elevator = Elevator('elevator', 245, 400, 5)
        self.cart = Cart('cart', 420, 190, 7)

        # BUTTONS / TEXT
        self.buy_button = pygame.image.load(
            'C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/Upgrade.png')
        self.buy_button = pygame.transform.scale(self.buy_button, (100, 50))
        self.buy_button_rect = self.buy_button.get_rect(center=(250, 250))
        self.shaft_button = pygame.image.load('C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/newshaft.png')
        self.shaft_button = pygame.transform.scale(self.shaft_button, (100, 50))
        self.shaft_button_rect = self.shaft_button.get_rect(center=(350, 350))


    ############### INTRO FUNCTIONS ###############

    # EVENTS FROM START SCREEN
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'playing'
                elif self.howtoplay_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'help'
                elif self.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

    def start_update(self):
        pass

    def start_draw(self):
        # FILLING SCREEN / DRAWING BUTTONS
        screen.fill('light blue')
        screen.blit(self.title, (500, 10))
        screen.blit(self.start_button, (720, 400))
        screen.blit(self.exit_button, (720, 600))
        pygame.display.update()

    ############### PLAYING FUNCTIONS ###############

    def test(self):
        # MOVING CART
        if self.cart.rect.x >= 1666:
            self.coins = (self.ores[0]) + (self.ores[1] * 2) + (self.ores[2] * 3) + (self.ores[3] * 4) + (
                        self.ores[4] * 5)

    def playing_events(self):
        # EVENTS HAPPENING WHILE PLAYING GAME
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Events while Playing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'start'
                if event.key == pygame.K_u:
                    if self.coins >= self.upgrades:
                        self.coins -= self.upgrades
                        self.upgrades += 20
                        self.ash.speed += .5
                        self.ash.loaded_speed += 1
                        self.blocky_guy.speed += .5
                        self.blocky_guy.loaded_speed += 1
                        self.demtreuis_demarcus_dejames_dathird.loaded_speed += 1
                        self.demtreuis_demarcus_dejames_dathird.speed += .5
                        self.jerome.loaded_speed += 1
                        self.jerome.speed += .5
                        self.head.loaded_speed += 1
                        self.head.speed += .5

                if event.key == pygame.K_SPACE:
                    if self.coins >= self.shaft_upgrade and self.unlocked == 1:
                        self.coins -= self.shaft_upgrade
                        self.shaft_upgrade += 250
                        self.unlocked += 1
                    elif self.coins >= self.shaft_upgrade and self.unlocked == 2:
                        self.shaft_upgrade += 500
                        self.coins -= self.shaft_upgrade
                        self.unlocked += 1
                    elif self.coins >= self.shaft_upgrade and self.unlocked == 3:
                        self.coins -= self.shaft_upgrade
                        self.shaft_upgrade += 3000
                        self.unlocked += 1
                    elif self.coins >= self.shaft_upgrade and self.unlocked == 4:
                        self.coins -= self.shaft_upgrade
                        self.shaft_upgrade += 6000
                        self.unlocked += 1
                    elif self.coins >= self.shaft_upgrade and self.unlocked == 5:
                        self.coins -= 10000

        self.ores = [self.ash.coal, self.blocky_guy.iron, self.demtreuis_demarcus_dejames_dathird.gold, self.jerome.diamonds, self.head.bitcoins]

    def playing_update(self):
        # MAKES MINERS WALK / UNLOCK NEW MINERS
        self.ash.walking()
        if self.unlocked == 2:
            self.ash.walking()
            self.blocky_guy.walking()
        elif self.unlocked == 3:
            self.ash.walking()
            self.blocky_guy.walking()
            self.demtreuis_demarcus_dejames_dathird.walking()
        elif self.unlocked == 4:
            self.ash.walking()
            self.blocky_guy.walking()
            self.demtreuis_demarcus_dejames_dathird.walking()
            self.jerome.walking()
        elif self.unlocked == 5:
            self.ash.walking()
            self.blocky_guy.walking()
            self.jerome.walking()
            self.demtreuis_demarcus_dejames_dathird.walking()
            self.head.walking()
        self.elevator.walking()
        self.cart.walking()

    def playing_draw(self):
        # FILL BACKGROUND / PLACE IMAGES & DRAW SPRITE CLASSES / TEXT
        screen.fill('light gray')
        screen.blit(self.background, (0, 0))

        self.level.run()
        self.ash.drawing()
        self.blocky_guy.drawing()
        self.jerome.drawing()
        self.demtreuis_demarcus_dejames_dathird.drawing()
        self.head.drawing()
        self.elevator.drawing()
        self.cart.drawing()
        self.draw_text(f"Coins: {self.coins}", screen, [WIDTH / 2, 50], 100, 10, "black")
        self.draw_text(f"{self.upgrades}", screen, [10, 110], 16, 16, "black")
        self.draw_text(f"{self.shaft_upgrade}", screen, [10, 160], 16, 16, "black")
        if self.shaft_upgrade == 6:
            self.draw_text(f"YOU'VE BEEN SCAMMEEDDD OF 10000 COINS!", screen, [10, 110], 16, 16, "black")
        screen.blit(self.corner_logo, (5, 10))
        screen.blit(self.buy_button, (10, 110))
        screen.blit(self.shaft_button, (10, 160))

        pygame.display.update()
