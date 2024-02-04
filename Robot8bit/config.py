import pygame.image

# pygame.init()
#
# screen_info = pygame.display.Info()
# WIN_WIDTH = screen_info.current_w
# WIN_HEIGHT = screen_info.current_h

WIN_WIDTH = 1375
WIN_HEIGHT = 735
TILESIZE = 32
FPS = 60

ROBOT_LAYER = 6
ENEMY_LAYER = 5
ITEM_LAYER = 4
WALL_LAYER = 3
LAKE_LAYER = 2
GROUND_LAYER = 1

ROBOT_SPEED = 3
ENEMY_SPEED = 2

WETSUIT_SKIN = pygame.image.load("assets/water.png")
ROBOT_SKIN = pygame.image.load("assets/single.png")
DIAMOND_SKIN = pygame.image.load("assets/diamond.png")
POTION_SKIN = pygame.image.load("assets/pocion.png")
BOMB_SKIN = pygame.image.load("assets/bomb.png")
HEART_SKIN = pygame.image.load("assets/heart.png")
SINGLE_WETSUIT = pygame.image.load("assets/singleWetSuit.png")

diamond_tamano = (40, 40)
bomb_tamano = (35, 35)
heart_tamano = (40, 40)
traje_estado = (80, 80)

WETSUIT = pygame.transform.scale(SINGLE_WETSUIT, heart_tamano)
HEART = pygame.transform.scale(HEART_SKIN, heart_tamano)
DIAMOND = pygame.transform.scale(DIAMOND_SKIN, diamond_tamano)
BOMB = pygame.transform.scale(BOMB_SKIN, bomb_tamano)
CON_TRAJE = pygame.transform.scale(SINGLE_WETSUIT, traje_estado)
SIN_TRAJE = pygame.transform.scale(ROBOT_SKIN, traje_estado)

RED = (250, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

mapa_a_cargar = 'mapa.txt'