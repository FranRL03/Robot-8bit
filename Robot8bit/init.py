import pygame

from models.muro import Muro
from models.robot import Robot

pygame.init()

# CLASES INSTANCIADAS
robot = Robot()
obstacles = [Muro(100, 200, 80, 80), Muro(300, 400, 80, 80), Muro(500, 100, 80, 80)]

# CARGA DEL FONDO
background_image = pygame.image.load("assets/fondo.png")
background_rect = background_image.get_rect()

# CARGA DE OBSTACULOS
lake = pygame.image.load("assets/lake.png")
lake = pygame.transform.scale(lake, (150, 150))

# lake2 = pygame.image.load("assets/lake.png")
# lake2 = pygame.transform.scale(lake, (150, 150))

# CONFIGURACION DE PANTALLA
for obstacle in obstacles:
    obstacle.image = pygame.transform.scale(obstacle.image, (50, 50))

robot.image = pygame.transform.scale(robot.image, (80, 80))
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

barra_vida = pygame.Surface((screen_width, 50))
barra_vida.fill((181, 193, 152))

vida_icon = pygame.image.load("assets/heart.png")
vida_icon = pygame.transform.scale(vida_icon, (55, 55))

# CONFIGURACION DEL TEXTO
font = pygame.font.Font(None, 36)

def check_collision(player_one, obstacles):
    player_rect = pygame.Rect(player_one.position[0], player_one.position[1], player_one.size[0], player_one.size[1])

    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle.rect.x, obstacle.rect.y, obstacle.rect.width, obstacle.rect.height)

        if player_rect.colliderect(obstacle_rect):
            return True

    return False



game_running = True
while game_running:

    # VERIFICACION DE COLISIONES
    collision = check_collision(robot, obstacles)

    if collision:
        robot.vida -= 1

    if robot.vida == 0:
        game_running = False

    robot.position = [max(0, min(robot.position[0], screen_width - robot.size[0])),
                      max(0, min(robot.position[1], screen_height - robot.size[1]))]

    # ALGUNOS EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # MANEJO DEL MOVIMIENTO
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        robot.move_right()
    if keys[pygame.K_LEFT]:
        robot.move_left()
    if keys[pygame.K_UP]:
        robot.move_up()
    if keys[pygame.K_DOWN]:
        robot.move_down()

    # RENDERIZACIÓN
    screen.blit(background_image, background_rect)

    # CREACION DEL LAGO
    screen.blit(lake, (220, 100))
    screen.blit(lake, (520, 300))

    # CREACION DE LOS MUROS
    for obstacle in obstacles:
        screen.blit(obstacle.image, (obstacle.rect.x, obstacle.rect.y, obstacle.rect.width, obstacle.rect.height))

    screen.blit(barra_vida, (0, screen_height - 50))

    # Renderiza el texto de los puntos de vida
    text = font.render("Vida: " + str(robot.vida), 1, (10, 10, 10))
    screen.blit(text, (10, screen_height - 40))
    screen.blit(vida_icon, (95, screen_height - 55))

    screen.blit(robot.image, (robot.position[0], robot.position[1], robot.size[0], robot.size[1]))


    pygame.display.flip()