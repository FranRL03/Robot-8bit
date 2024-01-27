import pygame.event

from models.button import Button
from models.enemy import Enemy
from models.ground import Ground
from models.wall import Wall
from models.sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('fonts/upheavtt.ttf', 32)

        self.character_spritesheet = Spritesheet('assets/character.png')
        self.terrain_spritesheet = Spritesheet('assets/terrain.png')
        self.enemy_sprintesheet = Spritesheet('assets/enemy.png')
        self.intro_background = pygame.image.load('assets/introbackground.png')
        self.go_background = pygame.image.load('assets/gameover.png')

    def create_map(self):
        for i, row in enumerate(map_design):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "M":
                    Wall(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "R":
                    Robot(self, j, i)

    # def create_map(self):
    #     tile_width = WIN_WIDTH // len(map_design[0])
    #     tile_height = WIN_HEIGHT // len(map_design)
    #
    #     for i, row in enumerate(map_design):
    #         for j, column in enumerate(row):
    #             Ground(self, j * tile_width, i * tile_height)
    #             if column == "M":
    #                 Wall(self, j * tile_width, i * tile_height)
    #             if column == "E":
    #                 Enemy(self, j * tile_width, i * tile_height)
    #             if column == "R":
    #                 Robot(self, j * tile_width, i * tile_height)

    def new(self):

        # empezar el juego
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.spikes = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()

        # se crea el mapa
        self.create_map()

    def events(self):
        # eventos del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    def update(self):
        # actualizar el juego
        self.all_sprites.update()
    def draw(self):
        # dibujar el mapa
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    def main(self):
        # bucle del juego
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))

        restart_button = Button(10, WIN_HEIGHT - 60, 150, 50, WHITE, BLACK, 'Restart', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            self.screen.blit(self.go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def intro_screen(self):
        intro = True

        title = self.font.render('ROBOT 8-BITS', True, BLACK)
        title_rect = title.get_rect(x=200, y=160)

        play_button = Button(250, 220, 100, 50, WHITE, BLACK, 'Jugar', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
