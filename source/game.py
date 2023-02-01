from menu import *
from gameplay import *
import os
class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.CHOOSE_KEY, self.BACK_KEY = False, False, False, False
        self.NUM1, self.NUM2, self.NUM3, self.NUM4, self.NUM5 = False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1280, 720
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name_title = 'font/title.otf'
        self.font_menu = 'font/menu.ttf'
        self.font_credit = 'font/credit.ttf'
        self.BLACK, self.WHITE, self.YELLOW, self.RED = (0, 0, 0), (255, 255, 255), (255, 255, 0), (255, 0, 0)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.choosing = ChoosingMenu(self)
        self.Volume = VolumeMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.CHOOSE_KEY:
                self.playing = False
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.CHOOSE_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_1:
                    self.NUM1 = True
                if event.key == pygame.K_2:
                    self.NUM2 = True
                if event.key == pygame.K_3:
                    self.NUM3 = True
                if event.key == pygame.K_4:
                    self.NUM4 = True
                if event.key == pygame.K_5:
                    self.NUM5 = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.CHOOSE_KEY, self.BACK_KEY = False, False, False, False
        self.NUM1, self.NUM2, self.NUM3, self.NUM4, self.NUM5 = False, False, False, False, False

    def draw_tile(self, text, size, x, y):
        font = pygame.font.Font(self.font_name_title, size)
        text_surface = font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_menu, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_credit(self, text, size, x, y):
        font = pygame.font.Font(self.font_credit, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_credit1(self, text, size, x, y):
        font = pygame.font.Font(self.font_credit, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def cursor_option(self, text, size, x, y):
        font = pygame.font.Font(self.font_name_title, size)
        text_surface = font.render(text, True, self.YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_ingame_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_menu, size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_text_black(self, text, size, x, y):
        font = pygame.font.Font(self.font_menu, size)
        text_surface = font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
class bienphu():
    g=Game()
