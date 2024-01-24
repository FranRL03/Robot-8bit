import pygame

from models.muro import Muro
from models.robot import Robot

pygame.init()

# CLASES INSTANCIADAS
player_one = Robot()
obstacle = Muro()

# CARGA DEL FONDO
background_image = pygame.image.load("assets/fondo.png")
background_rect = background_image.get_rect()

# CONFIGURACION DE PANTALLA
player_one.image = pygame.transform.scale(player_one.image, (80, 80))
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
# screen = pygame.display.set_mode((800, 600))

vida_icon = pygame.image.load("assets/heart.png")
vida_icon = pygame.transform.scale(vida_icon, (55, 55))

# CONFIGURACION DEL TEXTO
font = pygame.font.Font(None, 36)
score = 0

def check_collision(player_one, obstacle):
    if player_one.position[0] == obstacle.position[0] and player_one.position[1] == obstacle.position[1]:
        return True
    return False

barra_vida = pygame.Surface((screen_width, 50))
barra_vida.fill((181, 193, 152))

game_running = True
while game_running:

    # VERIFICACION DE COLISIONES
    collision = check_collision(player_one, obstacle)

    if collision:
        game_running = False
    else:
        score += 1

    # ALGUNOS EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # MANEJO DEL MOVIMIENTO
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_one.move_right()
    if keys[pygame.K_LEFT]:
        player_one.move_left()
    if keys[pygame.K_UP]:
        player_one.move_up()
    if keys[pygame.K_DOWN]:
        player_one.move_down()

    # RENDERIZACIÓN
    screen.blit(background_image, background_rect)
    screen.blit(player_one.image, (player_one.position[0], player_one.position[1], player_one.size[0], player_one.size[1]))

    screen.blit(barra_vida, (0, screen_height - 50))

    # Renderiza el texto de los puntos de vida
    text = font.render("Vida: " + str(player_one.vida), 1, (10, 10, 10))
    screen.blit(text, (10, screen_height - 40))
    screen.blit(vida_icon, (95, screen_height - 55))

    pygame.display.flip()


