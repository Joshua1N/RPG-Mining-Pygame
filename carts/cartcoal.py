import pygame.display


class Cart(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.loaded = False
        img = pygame.image.load('C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/Cart-Empty.png').convert_alpha()
        self.image = pygame.transform.scale(img, (54, 54))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = pygame.display.get_surface()
        self.elevator_running = True

    def move(self, moving_left, moving_right):
        # reset movement variables
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.direction = 1

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def walking(self):
        if not self.loaded:
            img = pygame.image.load('C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/Cart-Gold.png')
            self.image = pygame.transform.scale(img, (54, 54))
            self.move(moving_left=0, moving_right=1)
            self.speed = self.speed
            pygame.display.update()
            if self.rect.x >= 1670:
                self.loaded = True
                self.ash_running = False

        if self.loaded:
            img = pygame.image.load('C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/Cart-Empty.png')
            self.image = pygame.transform.scale(img, (54, 54))
            self.move(moving_left=1, moving_right=0)
            self.speed = self.speed
            pygame.display.update()
            if self.rect.x <= 400:
                # print(f'Iron: {self.iron}')
                self.loaded = False
                self.ash_running = True

    def drawing(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

