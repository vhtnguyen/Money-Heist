from minigame import Minigame
from gameplay import *


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 250
        self.back_ground = pygame.image.load('image/nen.png')
        self.icon = pygame.image.load('image/icon.png')
        self.file = open('sounds/battat.txt', 'w')
        self.file.write('On')
        self.file.close()

    def draw_cursor(self):
        self.game.cursor_option('$', 50, self.cursor_rect.x, self.cursor_rect.y + 10)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def set_title_bar(self):
        # title and icon
        self.Title = pygame.display.set_caption("Game nay rat hoanh trang")
        self.set_icon = pygame.display.set_icon(self.icon)


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 100
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 170
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.back_ground, (0, 0))
            self.game.draw_tile('MONEY HEI$T', 120, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 270)
            self.game.draw_text("Start Game", 40, self.startx, self.starty)
            self.game.draw_text("Options", 40, self.optionsx, self.optionsy)
            self.game.draw_text("Quit", 40, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()
            self.set_title_bar()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Quit'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    # loi re
    def check_input(self):
        self.move_cursor()
        if self.game.CHOOSE_KEY:
            if self.state == 'Start':
                self.game.curr_menu = self.game.choosing
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Quit':
                self.game.curr_menu = self.game.credits
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        self.back_ground = pygame.image.load('image/choosing.jpg')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.display.blit(self.back_ground, (0, 0))
            self.game.draw_text('Options', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text("Volume", 40, self.volx, self.voly)
            self.game.draw_text("Screen", 40, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Screen'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Screen':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.CHOOSE_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            if self.state == 'Volume':
                self.game.curr_menu = self.game.Volume
                self.run_display = False
            if self.state == 'Screen':
                pass


class sound_theme(Menu):
    menu_theme_song = 'sounds/menu.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(menu_theme_song)
    playing_sound = True
    if playing_sound:
        pygame.mixer.music.play()


class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'On'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        self.back_ground = pygame.image.load('image/choosing.jpg')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.display.blit(self.back_ground, (0, 0))
            self.game.draw_text('Volume', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.on_off()
            self.draw_cursor()
            self.blit_screen()
        pygame.display.update()

    def on_off(self):
        if sound_theme.playing_sound:
            self.game.draw_text("On", 60, self.volx, self.voly)
        else:
            self.game.draw_text("Off", 60, self.volx, self.voly)

    def check_input(self):

        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        if self.game.CHOOSE_KEY:
            if self.state == 'Off':
                self.state = 'On'
                self.file = open('sounds/battat.txt','w')
                self.file.write('On')
                self.file.close()
                pygame.mixer.music.play()
                sound_theme.playing_sound = True
            elif self.state == 'On':
                self.state = 'Off'
                self.file = open('sounds/battat.txt', 'w')
                self.file.write('Off')
                self.file.close()
                pygame.mixer.music.stop()
                sound_theme.playing_sound = False


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.pic = pygame.image.load('image/team.png')
        self.back_ground = pygame.image.load('image/end.png')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            if self.game.CHOOSE_KEY:
                pygame.quit()
                sys.exit()
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.back_ground, (0, 0))
            self.game.draw_text('Thanks for playing', 50, self.game.DISPLAY_W / 2, 40)
            self.game.draw_credit1('DEVELOPED BY CODEDAOSQUAD.FIT@HCMUS 2021', 15, self.game.DISPLAY_W / 2,
                                   self.game.DISPLAY_H - 40)
            self.blit_screen()


class ChoosingMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.file = open('money/player_money.txt', 'r')
        self.money = int(self.file.readline().split('=')[0])
        self.file.seek(0)
        self.file.close()
        self.state = 'New Game'
        self.newgx, self.newgy = self.mid_w, self.mid_h + 20
        self.loadgx, self.loadgy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.newgx + self.offset, self.newgy)
        self.back_ground = pygame.image.load('image/choosing.jpg')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.display.blit(self.back_ground, (0, 0))
            self.game.draw_text('please choose', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text("NEW GAME", 40, self.newgx, self.newgy)
            self.game.draw_text("LOAD GAME", 40, self.loadgx, self.loadgy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if TAM.BIENTAM==1:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
            TAM.BIENTAM=0;
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'New Game':
                self.state = 'Load Game'
                self.cursor_rect.midtop = (self.loadgx + self.offset, self.loadgy)
            elif self.state == 'Load Game':
                self.state = 'New Game'
                self.cursor_rect.midtop = (self.newgx + self.offset, self.newgy)

    def check_input(self):
        global MONEY
        self.move_cursor()
        if self.game.CHOOSE_KEY:
            if self.state == 'Load Game':
                self.file = open('money/player_money.txt', 'r')
                self.file.seek(0)
                self.money = int(self.file.readline().split('=')[0])
                self.file.close()
                MONEY = self.money
                if self.money >= 300:
                    display_gameplay()
                else:
                    MINIGAME = Minigame()
                    MINIGAME.run()

            if self.state == 'New Game':
                self.file = open('money/player_money.txt', 'w')
                self.money = 5000
                self.file.write(str(self.money))
                self.file.seek(0)
                self.file.close()
                MONEY = self.money
                MINIGAME = Minigame()
                MINIGAME.run()
