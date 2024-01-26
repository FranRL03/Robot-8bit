import pygame.image

WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32
FPS = 60

ROBOT_LAYER = 3
WALL_LAYER = 2
GROUND_LAYER = 1

ROBOT_SPEED = 3

ROBOT_SKIN = pygame.image.load("assets/single.png")

RED = (250, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# TILEMAP
map_design = [
    'MMMMMMMMMMMMMMMMMMMM',
    'M R                M',
    'M    MMMMMMMMM     M',
    'M    M             M',
    'M    MMMMM         M',
    'M    M             M',
    'M    M             M',
    'M                  M',
    'M     MMMMMMMMMM   M',
    'M            MM    M',
    'M            MM    M',
    'M            MM    M',
    'M      MMMMMMMM    M',
    'M                  M',
    'MMMMMMMMMMMMMMMMMMMM',
]

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
# M               MMMMMMMMMMMMMMMMMMMMMMM
# M                      MM        D    M
# M                     MM     D        M
# M          MMMMMMMMMMMMMMMMMMMMMMMMMMMM
# M                                     M
# M                                     M
# M                                     M
# M                                     M
# M                                     M
# M                                     M
# M                                     M
# M                                     M
# M                                     M
# M                                     M
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
