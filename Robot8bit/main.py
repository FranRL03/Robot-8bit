import pygame

from Wall import Wall
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def createMap(self):
        for i, row in enumerate(map_design):
           for j, column in enumerate(row):
               if column == "M":
                    Wall(self, j, i)
                if column == "P":
                    Robot(self, j, i)



    def new(self):
        # se crea el mapa
        self.createMap()

        # empezar el juego
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.spikes = pygame.sprite.LayeredUpdates()

        self.robot = Robot(self, 1, 2)

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
        self.running = False
    def gameOver(self):
        pass
    def introScreen(self):
        pass

g = Game()
g.introScreen()
g.new()
while g.running:
    g.main()
    g.gameOver()

pygame.quit()
sys.exit()
