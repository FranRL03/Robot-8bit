import pygame.event

from models.button import Button
from models.enemy import Enemy
from models.ground import Ground
from models.items import Potion, Diamond, Wetsuit, Bomb
from models.lake import Lake
from models.spikes import Spikes
from models.wall import Wall
from models.robot import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('fonts/upheavtt.ttf', 32)

        self.character_spritesheet = Spritesheet('assets/character2.png')
        self.character_wetsuit_spritesheet = Spritesheet('assets/characterWithWetsuit2.png')
        self.terrain_spritesheet = Spritesheet('assets/terrain.png')
        self.lake_spritsheet = Spritesheet('assets/terrain.png')
        self.enemy_spritesheet = Spritesheet('assets/enemy.png')
        self.spikes_spritesheet = Spritesheet('assets/terrain.png')
        self.bomb_spritesheet = Spritesheet('assets/bomb.png')
        self.potion_spritesheet = Spritesheet('assets/pocion.png')
        self.wetsuit_spritesheet = Spritesheet('assets/waterBottle.png')
        self.diamond_spritesheet = Spritesheet('assets/diamond.png')
        self.intro_background = pygame.image.load('assets/introbackground.png')
        self.go_background = pygame.image.load('assets/gameover.png')

    def cargar_mapa(mapa):
        with open(mapa, 'r') as archivo:
            primera_linea = archivo.readline().strip().split(', ')
            diccionario = {item.split(':')[0]: int(item.split(':')[1]) for item in primera_linea}
            contenido = [linea.strip() for linea in archivo]

        return diccionario, contenido

    objetos, mapa = cargar_mapa(mapa_a_cargar)
    print(objetos)

    def imprimir_objetos(self):
        for clave, valor in self.objetos.items():
            for valoresRandom in range(valor):
                x = random.randint(0, len(self.mapa[0]) - 1)
                y = random.randint(0, len(self.mapa) - 1)

                # comprobar la posicion que este vacia para colocar el objeto
                while self.mapa[y][x] != ' ':
                    # saca la longitud del mapa y le resta 1 para que no empieze a contar
                    # desde el 0
                    x = random.randint(0, len(self.mapa[0]) - 1)
                    y = random.randint(0, len(self.mapa) - 1)

                if clave == "P":
                    Potion(self, x, y)
                if clave == "D":
                    Diamond(self, x, y)
                if clave == "T":
                    Wetsuit(self, x, y)
                if clave == "B":
                    Bomb(self, x, y)

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
                if column == "S":
                    Spikes(self, j, i)

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
        self.imprimir_objetos()

    def events(self):
        # eventos del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
                # self.playing = False
                # self.running = False
                self.leave()

    def update(self):
        # actualizar el juego
        self.all_sprites.update()

    def draw(self):
        # dibujar el mapa
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        for sprite in self.all_sprites:
            if isinstance(sprite, Robot):
                vida_text = self.font.render(f'x {sprite.vida}', True, WHITE)
                self.screen.blit(vida_text, (1300,40))
                self.screen.blit(HEART, (1250, 35))

                diamond_text = self.font.render(f'x {sprite._diamond_inventory}', True, WHITE)
                self.screen.blit(DIAMOND, (1250, 100))
                self.screen.blit(diamond_text, (1300, 110))

                bomb_text = self.font.render(f'x {sprite._bomb_inventory}', True, WHITE)
                self.screen.blit(BOMB, (1250, 170))
                self.screen.blit(bomb_text, (1300, 180))

                self.screen.blit(WETSUIT, (1250, 240))
                if sprite.wetsuit_inventory == True:
                    traje_text = self.font.render('x 1', True, WHITE)
                    self.screen.blit(traje_text, (1300, 250))
                else:
                    traje_text = self.font.render('x 0', True, WHITE)
                    self.screen.blit(traje_text, (1300, 250))

                if sprite.water_shirt == True:
                    # traje = self.font.render('Traje puesto', True, WHITE)
                    # self.screen.blit(traje, (1240, 240))
                    self.screen.blit(CON_TRAJE, (1270, 320))
                else:
                    self.screen.blit(SIN_TRAJE, (1270, 320))

                score_text = self.font.render(f'Score: {sprite._score}', True, WHITE)
                self.screen.blit(score_text, (1060, 50))



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
        go_background = pygame.transform.scale(self.go_background, (WIN_WIDTH, WIN_HEIGHT))

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

            self.screen.blit(go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def intro_screen(self):
        intro = True

        title = self.font.render('ROBOT 8-BITS', True, BLACK)
        title_rect = title.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 - 30))

        play_button = Button(WIN_WIDTH/2 - 50, WIN_HEIGHT/2, 100, 50, WHITE, BLACK, 'Jugar', 32)

        intro_background = pygame.transform.scale(self.intro_background, (WIN_WIDTH, WIN_HEIGHT))

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def leave(self):
        text = self.font.render('¿Quieres salir?', True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

        si_button = Button(10, WIN_HEIGHT - 60, 130, 50, WHITE, BLACK, 'Salir', 32)
        no_button = Button(330, WIN_HEIGHT - 60, 170, 50, WHITE, BLACK, 'Cancelar', 32)

        leave_background = pygame.transform.scale(self.go_background, (WIN_WIDTH, WIN_HEIGHT))

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if si_button.is_pressed(mouse_pos, mouse_pressed):
                self.playing = False
                self.running = False
            elif no_button.is_pressed(mouse_pos, mouse_pressed):
                return

            self.screen.blit(leave_background, (0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(si_button.image, si_button.rect)
            self.screen.blit(no_button.image, no_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()