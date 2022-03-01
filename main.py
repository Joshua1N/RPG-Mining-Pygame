import pygame, sys
from map import *
from level import Level

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
vec = pygame.math.Vector2


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'playing'
        self.level = Level(map, screen)

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
        # Player
        self.player = pygame.Rect(100, 100, 30, 60)
        # Elevator
        self.elevator = pygame.Rect(185, 200, 235, 20)
        # Grass Ground
        self.ground = pygame.image.load('assets/Grass.png').convert_alpha()
        self.ground = pygame.transform.scale(self.ground, (1500, 20))
        self.ground_rect = self.ground.get_rect()
        # Stone Ground
        self.stone = pygame.image.load('assets/Stone.png').convert_alpha()
        self.stone = pygame.transform.scale(self.stone, (1500, 20))
        self.stone_rect = self.stone.get_rect()
        '''self.ground = pygame.Rect(420, 200, 1500, 20)
        self.coal_floor = pygame.Rect(420, 372, 1500, 20)
        self.iron_floor = pygame.Rect(420, 544, 1500, 20)
        self.gold_floor = pygame.Rect(420, 716, 1500, 20)
        self.platinum_floor = pygame.Rect(420, 888, 1500, 20)
        self.diamond_floor = pygame.Rect(420, 1060, 1500, 20)
        self.stone = pygame.image.load('assets/stone.png').convert_alpha()
        self.stone = pygame.transform.scale(self.stone, (50, 50))'''

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Events while Playing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'start'
        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
            self.elevator.y = self.elevator.y + 4

    def playing_update(self):
        pass

    def playing_draw(self):
        screen.fill('white')

        self.level.run()

        pygame.display.update()


'''        pygame.draw.rect(screen, 'grey', self.coal_floor)
        pygame.draw.rect(screen, 'grey', self.iron_floor)
        pygame.draw.rect(screen, 'grey', self.gold_floor)
        pygame.draw.rect(screen, 'grey', self.platinum_floor)
        pygame.draw.rect(screen, 'grey', self.diamond_floor)
        screen.blit(self.stone, (1800, 300))
        pygame.draw.rect(screen, 'blue', self.player)
        pygame.draw.rect(screen, 'red', self.elevator)
        # pygame.draw.rect(screen, 'dark green', self.ground)
        screen.blit(self.stone, (420, 372))
        screen.blit(self.ground, (420, 200))
        '''
