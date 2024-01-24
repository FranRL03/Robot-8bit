import pygame


class Muro():
    def __init__(self, x, y, width, height):
        # self.position = [100, 100]
        # self.size = [20, 20]
        self.image = pygame.image.load("assets/spikes.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y, self.rect.width, self.rect.height))


