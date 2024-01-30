import pygame
from config import *
import math
import time
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
        self.vida = 10
        self.water_shirt = False
        self.wetsuit_inventory = False
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
        self.animation_loop = 1

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
        if self.water_shirt == True:
            self.animateWetsuit()
        else:
            self.animate()

        self.collide_enemy()
        self.collide_lake()
        self.water_shirt_collide()
        self.desvestir_vestir()
        self.potion_collide()

        self.rect.x += self.x_change
        self.collide_walls('x')
        self.collide_spikes('x')
        self.rect.y += self.y_change
        self.collide_walls('y')
        self.collide_spikes('y')

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

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.playing = False

    def collide_lake(self):
        if self.water_shirt == True:
            return

        hits = pygame.sprite.spritecollide(self, self.game.lake, False)
        if hits:
            time.sleep(0.1)
            self.vida -= 3

            if self.vida <= 0:
                self.kill()
                self.game.playing = False


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

    def collide_spikes(self, direccion):
        if direccion == "x":
            hits = pygame.sprite.spritecollide(self, self.game.spikes, False)
            if hits:
                if self.x_change > 0:
                     self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

                time.sleep(0.1)
                self.vida -= 1

        if direccion == "y":
            hits = pygame.sprite.spritecollide(self, self.game.spikes, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

                time.sleep(0.1)
                self.vida -= 1

        if self.vida == 0:
            self.kill()
            self.game.playing = False


    def water_shirt_collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.wetsuit, True)
        if hits:
            self.water_shirt = True
            self.wetsuit_inventory = True
            print("Traje cogido")
            print("Traje cambiado")

    def potion_collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.potion, True)
        if hits:
            cantidad = random.randint(1, 5)
            self.vida = min(10, self.vida + cantidad)


    def animate(self):
        down_animations = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]

        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

    def animateWetsuit(self):
        down_animations = [self.game.character_wetsuit_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_wetsuit_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_wetsuit_spritesheet.get_sprite(68, 2, self.width, self.height)]

        up_animations = [self.game.character_wetsuit_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.character_wetsuit_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_wetsuit_spritesheet.get_sprite(68, 34, self.width, self.height)]

        left_animations = [self.game.character_wetsuit_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_wetsuit_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_wetsuit_spritesheet.get_sprite(68, 98, self.width, self.height)]

        right_animations = [self.game.character_wetsuit_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_wetsuit_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_wetsuit_spritesheet.get_sprite(68, 66, self.width, self.height)]

        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_wetsuit_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_wetsuit_spritesheet.get_sprite(3, 34, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.character_wetsuit_spritesheet.get_sprite(3, 98, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.character_wetsuit_spritesheet.get_sprite(3, 66, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1


    # def desvestir_vestir(self):
    #     keys = pygame.key.get_pressed()
    #
    #     if keys[pygame.K_t]:
    #         if self.wetsuit_inventory == True and self.water_shirt == False:
    #             self.water_shirt = True
    #             print("Traje equipado")
    #         elif self.water_shirt == True:
    #             self.water_shirt = False
    #             print("Traje quitado")

    def desvestir_vestir(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    if self.wetsuit_inventory == True and self.water_shirt == False:
                        self.water_shirt = True
                        print("Traje equipado")
                    elif self.water_shirt == True:
                        self.water_shirt = False
                        print("Traje quitado")

    # con esta funcion tengo que presionar muchas veces la tecla