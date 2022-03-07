import pygame.display
from miners.ash import *
from miners.blockyguy import *
from miners.jerome import *
from miners.demtreuisdemarcusdejamesdathird import *
from miners.head import *


class Elevator(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.loaded = False
        img = pygame.image.load('C:/Users/Brandon/PycharmProjects/RPG-MINING-PROJECT/assets/elevator.png').convert_alpha()
        self.image = pygame.transform.scale(img, (270, 270))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = pygame.display.get_surface()
        '''self.counter, self.text = 5, '5'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT + 4, 5000)'''
        self.elevator_running = True

        '''self.ash = Ash('ash', 440, 325, 5)
        self.blocky_guy = BlockyGuy('blockyguy', 440, 485, 4)
        self.jerome = Jerome('jerome', 440, 810, 2)
        self.demtreuis_demarcus_dejames_dathird = DemtreuisDemarcusDejamesDathird('DemtreuisDemarcusDejamesDathird', 440, 645, 3)
        self.head = Head('head', 440, 970, 1)
        self.elevator = Elevator('elevator', 200, 400, 3)

        self.ores = [self.ash.coal, self.blocky_guy.iron, self.demtreuis_demarcus_dejames_dathird.gold, self.jerome.diamonds, self.head.bitcoins]'''

    def move(self, moving_up, moving_down):
        # reset movement variables
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_up:
            dy = -self.speed
            self.direction = -1
        if moving_down:
            dy = self.speed
            self.direction = 1

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def walking(self):
        if not self.loaded:
            self.move(moving_up=0, moving_down=1)
            if self.rect.y >= 750:
                # while self.elevator_running:
                self.loaded = True
                self.head_running = False
                '''for event in pygame.event.get():
                                        if event.type == pygame.USEREVENT + 4:'''

        if self.loaded:
            self.move(moving_up=1, moving_down=0)
            if self.rect.y <= 268:
                print(f'Unloaded: ')
                self.loaded = False
                self.elevator_running = True
                # print(self.coins)

    def drawing(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

