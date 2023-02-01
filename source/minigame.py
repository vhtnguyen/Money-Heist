from gameplay import *
import pygame, random, sys


class Minigame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.gamerunning = True
        self.xSCREEN, self.ySCREEN = 1280, 720
        self.SCREEN = pygame.display.set_mode((self.xSCREEN, self.ySCREEN))
        # vi tri cac ruong
        self.x1, self.y1 = 380, 80
        self.x2, self.y2 = 680, 80
        self.x3, self.y3 = 980, 80
        self.x4, self.y4 = 380, 380
        self.x5, self.y5 = 680, 380
        self.x6, self.y6 = 980, 380
        self.dx, self.dy = 25, 25
        # vi tri huong dan
        self.xhd, self.yhd = 0, 250
        self.x0hd, self.y0hd = 20, 60
        # vi tri ket qua
        self.xkq, self.ykq = 50, 180
        # vi tri tien
        self.xMoney, self.yMoney = 20, 0
        # cac bien kiem tra
        self.DEM = 0
        self.b1 = self.b2 = self.b3 = self.b4 = self.b5 = self.b6 = 0
        self.dung = 0
        # tien
        self.money = 0
        self.file = open('money/player_money.txt', 'r')
        self.money = int(self.file.readline().split('=')[0])
        self.file.close()
        self.moneyplus = 0
        # phim
        self.K_DONE = False
        self.K_TAB = False
        self.K_1 = self.K_2 = self.K_3 = self.K_4 = self.K_5 = self.K_6 = False
        # image
        self.background = pygame.image.load("image/minigame/bgminigame.jpg")
        self.chest1 = pygame.image.load("image/minigame/chest1.png")
        self.chest2 = pygame.image.load("image/minigame/chest2.png")
        self.chest3 = pygame.image.load("image/minigame/chest3.png")
        self.chest4 = pygame.image.load("image/minigame/chest4.png")
        self.chest5 = pygame.image.load("image/minigame/chest5.png")
        self.chest6 = pygame.image.load("image/minigame/chest6.png")
        self.help = pygame.image.load("image/minigame/help.png")
        self.over = pygame.image.load("image/minigame/gameover.png")
        self.ex = pygame.image.load("image/minigame/x.png")
        # image ket qua
        self.kq1 = pygame.image.load("image/minigame/0.png")
        self.empty = pygame.image.load("image/minigame/empty.png")
        self.kq2 = pygame.image.load("image/minigame/100.png")
        self.gold = pygame.image.load("image/minigame/gold.png")
        self.kq3 = pygame.image.load("image/minigame/1000.png")
        self.diamond = pygame.image.load("image/minigame/diamond.png")
        # delay
        self.FPS = 60
        self.t = 1

    # hien thi tien kiem duoc
    def show_money(self, x, y, money, size):
        font = pygame.font.Font("font/minigame.ttf", size)
        money = font.render(str(money), True, (255, 255, 0))
        self.SCREEN.blit(money, (x, y))

    # hien thi rule
    def show_help(self, x, y, money, size):
        font = pygame.font.Font("font/credit.ttf", size)
        money = font.render(str(money), True, (255, 255, 255))
        self.SCREEN.blit(money, (x, y))

    # in ra ket qua
    def kq(self, DEM, x, y):
        if DEM == 1:
            self.SCREEN.blit(self.kq1, (self.xkq, self.ykq))
            self.SCREEN.blit(self.empty, (x, y))
        elif DEM == 10:
            self.SCREEN.blit(self.kq3, (self.xkq, self.ykq))
            self.SCREEN.blit(self.diamond, (x, y))
        else:
            self.SCREEN.blit(self.kq2, (self.xkq, self.ykq))
            self.SCREEN.blit(self.gold, (x, y))

    # delay
    def detime(self, x):
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(x * 1500)


    def run(self):
        global MONEY, xacnhan
        self.file = open('sounds/battat.txt','r')
        self.file.seek(0)
        self.sound = str(self.file.readline())
        if self.sound == 'On':
            pygame.mixer.init()
            pygame.mixer.music.load('sounds/minigame.mp3')
            pygame.mixer.music.play()
        # vong lap game
        while self.gamerunning:
            # khung hinh tren giay
            self.clock.tick(self.FPS)
            # insert image
            self.SCREEN.blit(self.background, (0, 0))
            self.SCREEN.blit(self.chest1, (self.x1, self.y1))
            self.SCREEN.blit(self.chest2, (self.x2, self.y2))
            self.SCREEN.blit(self.chest3, (self.x3, self.y3))
            self.SCREEN.blit(self.chest4, (self.x4, self.y4))
            self.SCREEN.blit(self.chest5, (self.x5, self.y5))
            self.SCREEN.blit(self.chest6, (self.x6, self.y6))
            self.show_money(self.xMoney, self.yMoney, "Money: {}".format(self.money + self.moneyplus), 32)
            self.show_help(self.xMoney, 700, "Hold TAB to know the rule".format(self.money), 20)
            # self.test('SPECIAL THANK', 30, 200, 140)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # su kien nhan thoat
                    self.gamerunning = False
                    self.file.close()
                    pygame.quit()
                    sys.exit()  # thoat chuong trinh

                if event.type == pygame.KEYDOWN:  # su kien co phim nhan xuong
                    if event.key == pygame.K_1:
                        self.K_1 = True
                    if event.key == pygame.K_2:
                        self.K_2 = True
                    if event.key == pygame.K_3:
                        self.K_3 = True
                    if event.key == pygame.K_4:
                        self.K_4 = True
                    if event.key == pygame.K_5:
                        self.K_5 = True
                    if event.key == pygame.K_6:
                        self.K_6 = True
                    if event.key == pygame.K_TAB:
                        self.K_TAB = True
                    if event.key == pygame.K_RETURN:
                        self.K_DONE = True

                if event.type == pygame.KEYUP:  # su kien nha phim
                    if event.key == pygame.K_1:
                        self.K_1 = False
                    if event.key == pygame.K_2:
                        self.K_2 = False
                    if event.key == pygame.K_3:
                        self.K_3 = False
                    if event.key == pygame.K_4:
                        self.K_4 = False
                    if event.key == pygame.K_5:
                        self.K_5 = False
                    if event.key == pygame.K_6:
                        self.K_6 = False
                    if event.key == pygame.K_TAB:
                        self.K_TAB = False

                # phim 1
                if self.K_1 and self.b1 == 0 and self.dung < 3:
                    self.b1 = self.b1 + 1
                    self.dung = self.dung + 1
                    self.DEM = random.randint(1, 10)
                    self.kq(self.DEM, self.x1 - self.dx, self.y1 - self.dy)
                    self.detime(self.t)
                    if self.DEM == 1:
                        self.moneyplus = self.moneyplus + 0
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    elif self.DEM == 10:
                        self.moneyplus = self.moneyplus + 1000
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    else:
                        self.moneyplus = self.moneyplus + 100
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                # phim 2
                if self.K_2 and self.b2 == 0 and self.dung < 3:
                    self.b2 = self.b2 + 1
                    self.dung = self.dung + 1
                    self.DEM = random.randint(1, 10)
                    self.kq(self.DEM, self.x2 - self.dx, self.y2 - self.dy)
                    self.detime(self.t)
                    if self.DEM == 1:
                        self.moneyplus = self.moneyplus + 0
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    elif self.DEM == 10:
                        self.moneyplus = self.moneyplus + 1000
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    else:
                        self.moneyplus = self.moneyplus + 100
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                # phim 3
                if self.K_3 and self.b3 == 0 and self.dung < 3:
                    self.b3 = self.b3 + 1
                    self.dung = self.dung + 1
                    self.DEM = random.randint(1, 10)
                    self.kq(self.DEM, self.x3 - self.dx, self.y3 - self.dy)
                    self.detime(self.t)
                    if self.DEM == 1:
                        self.moneyplus = self.moneyplus + 0
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    elif self.DEM == 10:
                        self.moneyplus = self.moneyplus + 1000
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    else:
                        self.moneyplus = self.moneyplus + 100
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                # phim 4
                if self.K_4 and self.b4 == 0 and self.dung < 3:
                    self.b4 = self.b4 + 1
                    self.dung = self.dung + 1
                    self.DEM = random.randint(1, 10)
                    self.kq(self.DEM, self.x4 - self.dx, self.y4 - self.dy)
                    self.detime(self.t)
                    if self.DEM == 1:
                        self.moneyplus = self.moneyplus + 0
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    elif self.DEM == 10:
                        self.moneyplus = self.moneyplus + 1000
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    else:
                        self.moneyplus = self.moneyplus + 100
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0

                # phim 5
                if self.K_5 and self.b5 == 0 and self.dung < 3:
                    self.b5 = self.b5 + 1
                    self.dung = self.dung + 1
                    self.DEM = random.randint(1, 10)
                    self.kq(self.DEM, self.x5 - self.dx, self.y5 - self.dy)
                    self.detime(self.t)
                    if self.DEM == 1:
                        self.moneyplus = self.moneyplus + 0
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    elif self.DEM == 10:
                        self.moneyplus = self.moneyplus + 1000
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    else:
                        self.moneyplus = self.moneyplus + 100
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                # phim 6
                if self.K_6 and self.b6 == 0 and self.dung < 3:
                    self.b6 = self.b6 + 1
                    self.dung = self.dung + 1
                    self.DEM = random.randint(1, 10)
                    self.kq(self.DEM, self.x6 - self.dx, self.y6 - self.dy)
                    self.detime(self.t)
                    if self.DEM == 1:
                        self.moneyplus = self.moneyplus + 0
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    elif self.DEM == 10:
                        self.moneyplus = self.moneyplus + 1000
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0
                    else:
                        self.moneyplus = self.moneyplus + 100
                        self.file = open('money/player_money.txt', 'w')
                        self.money = self.money + self.moneyplus
                        self.file.write(str(self.money))
                        self.file.seek(0)
                        self.file.close()
                        self.moneyplus = 0

                MONEY = self.money

            # phim TAB
            if self.K_TAB:
                self.SCREEN.blit(self.help, (self.xhd, self.yhd - 70))

            # danh dau ruong da mo
            if self.b1 == 1:
                self.SCREEN.blit(self.ex, (self.x1, self.y1))
            if self.b2 == 1:
                self.SCREEN.blit(self.ex, (self.x2, self.y2))
            if self.b3 == 1:
                self.SCREEN.blit(self.ex, (self.x3, self.y3))
            if self.b4 == 1:
                self.SCREEN.blit(self.ex, (self.x4, self.y4))
            if self.b5 == 1:
                self.SCREEN.blit(self.ex, (self.x5, self.y5))
            if self.b6 == 1:
                self.SCREEN.blit(self.ex, (self.x6, self.y6))

            if self.dung >= 3:
                self.SCREEN.blit(self.over, (self.xhd, self.yhd - 70))
                if self.K_DONE == True:
                    display_gameplay()
                    self.gamerunning = False


            pygame.display.update()

# MINIGAME = Minigame()
# MINIGAME.run()