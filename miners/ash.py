import pygame.display


class Ash(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.loaded = False
        img = pygame.image.load('C:/Users/Brandon/PycharmProjects/RPG-MINING-PROJECT/assets/ash_slave.png').convert_alpha()
        self.image = pygame.transform.scale(img, (108, 108))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = pygame.display.get_surface()
        self.counter, self.text = 5, '5'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.ash_running = True
        self.coal = 0
        self.ready = False

    def move(self, moving_left, moving_right):
        # reset movement variables
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def walking(self):
            if not self.loaded:
                self.move(moving_left=0, moving_right=1)
                self.speed = 5
                if self.rect.x >= 1920 - 170:
                    self.loaded = True
                    self.ash_running = False

            if self.loaded:
                self.move(moving_left=1, moving_right=0)
                self.speed = 5
                if self.rect.x <= 386:
                    self.coal += 1
                    # print(f'Iron: {self.iron}')
                    self.loaded = False
                    self.ash_running = True

    def drawing(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

