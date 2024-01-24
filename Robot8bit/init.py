import pygame

from models.muro import Muro
from models.robot import Robot

pygame.init()
player_one = Robot()
obstacle = Muro()

player_one = pygame.image.load("assets/robot.png")

font = pygame.font.Font(None, 36)
score = 0
def check_collision(player, obstacle):
    if player.position[0] == obstacle.position[0] and player.position[1] == obstacle.position[1]:
        return True
    return False

screen = pygame.display.set_mode((800, 600))

game_running = True
while game_running:

    collision = check_collision(player_one, obstacle)

    if collision:
        game_running = False
    else:
        score += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_one.move_right()
            if event.key == pygame.K_LEFT:
                player_one.move_left()
            if event.key == pygame.K_UP:
                player_one.move_up()
            if event.key == pygame.K_DOWN:
                player_one.move_down()

    pygame.draw.rect(screen, (255, 255, 255), (player_one.position[0], player_one.position[1],
                                               player_one.size[0], player_one.size[1]))
    pygame.draw.rect(screen, (255, 0, 0),(obstacle.position[0], obstacle.position[1],
                                          obstacle.size[0], obstacle.size[1]))
    pygame.display.flip()

    text = font.render("Score: " + str(score), 1, (10, 10, 10))
    screen.blit(text, (10, 10))
