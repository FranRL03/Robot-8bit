import pygame
from config import *
import math
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


class Robot(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ROBOT_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
        # image_to_load = ROBOT_SKIN
        # self.image = pygame.Surface([self.width, self.height])
        # self.image.set_colorkey(BLACK)
        # self.image.blit(image_to_load, (0,0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.collide_walls('x')
        self.rect.y += self.y_change
        self.collide_walls('y')

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= ROBOT_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += ROBOT_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= ROBOT_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += ROBOT_SPEED
            self.facing = 'down'

    def collide_walls(self, direccion):
        if direccion == "x":
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.x_change > 0:
                     self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direccion == "y":
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
