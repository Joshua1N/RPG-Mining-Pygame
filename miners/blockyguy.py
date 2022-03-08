import pygame.display


class BlockyGuy(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.loaded_speed = 4
        self.direction = 1
        self.flip = False
        self.loaded = False
        img = pygame.image.load('C:/Users/jlnelson/PycharmProjects/RPG-Mining-Pygame-main/retard/assets/blockyguy.png').convert_alpha()
        self.image = pygame.transform.scale(img, (108, 108))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = pygame.display.get_surface()
        self.counter, self.text = 5, '5'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT + 1, 2000)
        self.blockyguy_running = True
        self.iron = 0

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
                self.blockyguy_running = False

        if self.loaded:
            self.move(moving_left=1, moving_right=0)
            self.speed = self.loaded_speed
            if self.rect.x <= 386:
                self.iron += 1
                # print(f'Iron: {self.iron}')
                self.loaded = False
                self.blockyguy_running = True

    def drawing(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

