import pygame.image

# pygame.init()
#
# screen_info = pygame.display.Info()
# WIN_WIDTH = screen_info.current_w
# WIN_HEIGHT = screen_info.current_h

WIN_WIDTH = 1245
WIN_HEIGHT = 725
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

DIAMOND_SKIN = pygame.image.load("assets/diamond.png")
POTION_SKIN = pygame.image.load("assets/pocion.png")
BOMB_SKIN = pygame.image.load("assets/bomb.png")


RED = (250, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# TILEMAP
# map_design = [
#     'MMMMMMMMMMMMMMMMMMMM',
#     'M R                M',
#     'M    MMMMMMMMM     M',
#     'M    M             M',
#     'M    MMMMM         M',
#     'M    M             M',
#     'M                  M',
#     'M                  M',
#     'M               E  M',
#     'M            MM    M',
#     'M            MM    M',
#     'M   E        MM    M',
#     'M      MMMMMMMM    M',
#     'M                  M',
#     'MMMMMMMMMMMMMMMMMMMM',
# ]

# def cargar_mapa(nombre_archivo):
#     with open(nombre_archivo, 'r') as archivo:
#         contenido = [linea.strip() for linea in archivo]
#
#     return contenido

# Cargar el mapa desde el archivo
# nombre_archivo = 'mapa.txt'
# mapa = cargar_mapa(nombre_archivo)

# Ahora puedes utilizar el contenido del mapa en tu juego con pygame
# Por ejemplo, imprimirlo en la consola
# for fila in mapa:
#     print(fila)

# ===================================================================================

# EJEMPLO DE COMO SERIA LA CREACION DEL MAPA EN UN FICHERO SEGUN LUISMO
# BOMVAS DIAMANTES TRAJE Y POCIONES CON SU CANTIDAD

# TRANSFORMAR ESTO EN UN ARRAY DE CLAVE Y VALOR (DICCIONARIO)
# B:7, D:6, T:1, P:3
#
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
# M                                     M
# M     A                               M
# M     AAAAAA                          M
# M       AAA                           M
# M     AAAAA                           M
# M                                     M
# M                                     M
# M    R          MMMMMMMMMMMMMMMMMMMMMMM
# M                      MM             M
# M                     MM              M
# M          MMMMMMMMMMMMMMMMMMMMMMMMMMMM
# M                                     M
# M        E                            M
# M                                     M
# M                                     M
# M                   E                 M
# M                                     M
# M                                     M
# M          AAAAA                      M
# M         AAAAAAAA                    M
# M          AAAA                       M
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
