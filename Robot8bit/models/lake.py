import pygame

class Lake():
    def __init__(self, x, y, width, height):
        self.image = pygame.image.load("assets/lake.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def renderLake(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y, self.rect.width, self.rect.height))