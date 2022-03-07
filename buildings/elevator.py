import pygame.display
from retard.miners.ash import *
from retard.miners.blockyguy import *
from retard.miners.jerome import *
from retard.miners.demtreuisdemarcusdejamesdathird import *
from retard.miners.head import *


class Elevator(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.loaded = False
        img = pygame.image.load('C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/elevator.png').convert_alpha()
        self.image = pygame.transform.scale(img, (270, 270))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = pygame.display.get_surface()
        self.elevator_running = True

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

        if self.loaded:
            self.move(moving_up=1, moving_down=0)
            if self.rect.y <= 268:
                self.loaded = False
                self.elevator_running = True
                # print(self.coins)

    def drawing(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

