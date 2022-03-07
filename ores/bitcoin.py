import pygame

class Bitcoin(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('C:/Users/Brandon/PycharmProjects/RPG-MINING-PROJECT/assets/bitcoin_deposit.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(midtop=pos)
