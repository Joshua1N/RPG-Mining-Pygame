import pygame, sys
from map import *
from level import Level
from miners.ash import *
from miners.blockyguy import *
from miners.jerome import *
from miners.demtreuisdemarcusdejamesdathird import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
vec = pygame.math.Vector2


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'playing'
        self.level = Level(map, screen)
        self.loaded = False

        self.load()

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
        # Miners
        self.ash = Ash('ash', 440, 325, 5)
        self.blocky_guy = BlockyGuy('blockyguy', 440, 485, 5)
        self.jerome = Jerome('jerome', 440, 810, 5)
        self.demtreuis_demarcus_dejames_dathird = DemtreuisDemarcusDejamesDathird('DemtreuisDemarcusDejamesDathird', 440, 645, 5)

    ############### INTRO FUNCTIONS ###############
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    def start_update(self):
        pass

    def start_draw(self):
        pass

    ############### PLAYING FUNCTIONS ###############

    def playing_events(self):
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Events while Playing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'start'

    def playing_update(self):
        self.ash.walking()
        self.blocky_guy.walking()
        self.jerome.walking()
        self.demtreuis_demarcus_dejames_dathird.walking()

    def playing_draw(self):
        screen.fill('white')

        self.level.run()
        self.ash.drawing()
        self.blocky_guy.drawing()
        self.jerome.drawing()
        self.demtreuis_demarcus_dejames_dathird.drawing()

        pygame.display.update()
