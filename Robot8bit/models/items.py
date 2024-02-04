import pygame
from config import *
import math
import random


class Item(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = ITEM_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Diamond (Item):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.game.diamond.add(self)
        image_to_load = pygame.transform.scale(DIAMOND_SKIN, (self.width, self.height))
        self.image.blit(image_to_load, (0, 0))

class Potion (Item):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.game.potion.add(self)
        image_to_load = pygame.transform.scale(POTION_SKIN, (self.width, self.height))
        self.image.blit(image_to_load, (0, 0))

class Wetsuit (Item):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.game.wetsuit.add(self)
        image_to_load = pygame.transform.scale(WETSUIT_SKIN, (self.width, self.height))
        self.image.blit(image_to_load, (0, 0))


class Bomb (Item):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.game.bomb.add(self)
        image_to_load = pygame.transform.scale(BOMB_SKIN, (self.width, self.height))
        self.image.blit(image_to_load, (0, 0))
    def collide_with_item(self):
        hits = pygame.sprite.spritecollide(self, self.game.spikes, True)


