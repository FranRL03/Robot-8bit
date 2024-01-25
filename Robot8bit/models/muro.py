import pygame


class Muro():
    def __init__(self, x, y, width, height):
        # self.position = [100, 100]
        self.size = [5, 5]
        self.image = pygame.image.load("assets/spikes.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y, self.rect.width, self.rect.height))

    def check_collision(player_one, obstacles):
        player_rect = pygame.Rect(player_one.position[0], player_one.position[1], player_one.size[1],
                                  player_one.size[1])

        for obstacle in obstacles:
            obstacle_rect = pygame.Rect(obstacle.rect.x, obstacle.rect.y, obstacle.rect.width, obstacle.rect.height)

            if player_rect.colliderect(obstacle_rect):
                return True

        return False