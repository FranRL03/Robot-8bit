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

        self.character_spritesheet = Spritesheet('assets/character.png')
        self.terrain_spritesheet = Spritesheet('assets/terrain.png')
    def create_map(self):
        for i, row in enumerate(map_design):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "M":
                    Wall(self, j, i)
                if column == "R":
                    Robot(self, j, i)

    def new(self):

        # empezar el juego
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.spikes = pygame.sprite.LayeredUpdates()

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
        self.running = False
    def game_over(self):
        pass
    def intro_screen(self):
        pass

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
