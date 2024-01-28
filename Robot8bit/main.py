import pygame.event

from models.button import Button
from models.enemy import Enemy
from models.ground import Ground
from models.items import Diamond
from models.lake import Lake
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
        self.lake_spritsheet = Spritesheet('assets/terrain.png')
        self.enemy_sprintesheet = Spritesheet('assets/enemy.png')
        self.bomb = Spritesheet('assets/bomb.png')
        self.potion_sprintesheet = Spritesheet('assets/pocion.png')
        self.wetsuit_sprintesheet = Spritesheet('assets/waterBottle.png')
        self.diamond_sprintesheet = Spritesheet('assets/diamond.png')
        self.intro_background = pygame.image.load('assets/introbackground.png')
        self.go_background = pygame.image.load('assets/gameover.png')

    mapa_a_cargar = 'mapa.txt'


    def cargar_mapa(mapa):
        with open('mapa.txt', 'r') as archivo:
            contenido = [linea.strip() for linea in archivo]

        return contenido

    mapa = cargar_mapa(mapa_a_cargar)

    def create_map(self):
        for i, row in enumerate(self.mapa):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "M":
                    Wall(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "R":
                    Robot(self, j, i)
                if column == "A":
                    Lake(self, j, i)
                if column == "D":
                    Diamond(self, j, i)

    def new(self):

        # empezar el juego
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.lake = pygame.sprite.LayeredUpdates()
        self.spikes = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.potion = pygame.sprite.LayeredUpdates()
        self.wetsuit = pygame.sprite.LayeredUpdates()
        self.bomb = pygame.sprite.LayeredUpdates()
        self.diamond = pygame.sprite.LayeredUpdates()

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
        title_rect = title.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 - 30))

        play_button = Button(WIN_WIDTH/2 - 50, WIN_HEIGHT/2, 100, 50, WHITE, BLACK, 'Jugar', 32)

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
