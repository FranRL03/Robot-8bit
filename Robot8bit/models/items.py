import pygame
from config import *
import math
import random

class Diamond (pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = DIAMOND_LAYER
        self.groups = self.game.all_sprites, self.game.diamond
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        image_to_load = DIAMOND_SKIN
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(BLACK)
        self.image.blit(image_to_load, (10,10))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y



