SOLUONGBUA = 1
DEM123=0
LOCKENTERGAME = False
LOCKCHONSET=0
RUN=False
LOAD=False
COWLOAD=0
LOCKFIX=False
import game
import menu
# shop
import math


# shop
class SHOP:
    def __init__(self):
        pygame.init()
        self.shoprunning = True
        self.xSCREEN, self.ySCREEN = 1280, 720
        self.SCREEN = pygame.display.set_mode((self.xSCREEN, self.ySCREEN))
        # image
        self.bgshop = pygame.image.load("image/shop/bgshop1.png")
        self.note1 = pygame.image.load("image/shop/note1.png")
        self.note2 = pygame.image.load("image/shop/note2.png")
        self.note3 = pygame.image.load("image/shop/note3.png")
        self.ball = pygame.image.load("image/shop/ball1.png")
        self.hand1 = pygame.image.load("image/shop/hand1.png")
        self.hand2 = pygame.image.load("image/shop/hand2.png")
        self.hand3 = pygame.image.load("image/shop/hand3.png")
        self.hand4 = pygame.image.load("image/shop/hand4.png")
        self.hand5 = pygame.image.load("image/shop/hand5.png")
        self.sold = pygame.image.load("image/shop/sold1.png")
        # tien
        self.file = open('money/player_money.txt', 'r')
        self.money = int(self.file.readline().split('=')[0])
        self.file.close()
        self.moneyplus = 0
        # vi tri
        self.dx, self.dy = 10, 10
        self.xnote, self.ynote = 0, 150
        self.xMoney, self.yMoney = 10, 40
        self.r = 150
        self.xI, self.yI = 770, 350
        self.x1 = self.xI
        self.y1 = self.yI - self.r
        self.x2 = self.xI + self.r * math.sin(math.pi / 5 * 2)
        self.y2 = self.yI - self.r * math.cos(math.pi / 5 * 2)
        self.x3 = self.xI + self.r * math.sin(math.pi / 5)
        self.y3 = self.yI + self.r * math.cos(math.pi / 5)
        self.x4 = self.xI - self.r * math.sin(math.pi / 5)
        self.y4 = self.yI + self.r * math.cos(math.pi / 5)
        self.x5 = self.xI - self.r * math.sin(math.pi / 5 * 2)
        self.y5 = self.yI - self.r * math.cos(math.pi / 5 * 2)
        # cac bien kiem tra
        self.k = 1
        self.s = 0
        # phim
        self.K_LEFT = self.K_RIGHT = self.K_SPACE = self.K_DONE = False        
        # bua
        self.num = 0
        self.num_bua1 = 0
        self.num_bua2 = 0
        self.num_bua3 = 0
        self.num_bua4 = 0
        # delay
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def show_note(self, s):
        if s == 0:
            self.SCREEN.blit(self.note1, (self.xnote, self.ynote))
        if s >= 1:
            self.SCREEN.blit(self.note2, (self.xnote, self.ynote))
            self.show_money(600, 620, "ENTER TO CONTINUE", 40)

    def show_money(self, x, y, money, size):
        font = pygame.font.Font("font/minigame.ttf", size)
        money = font.render(str(money), True, (255, 255, 255))
        self.SCREEN.blit(money, (x, y))

    def move_hand(self, k):
        if k == 1:
            self.SCREEN.blit(self.hand1, (self.xI + self.dx, self.yI - self.dy))
        if k == 2:
            self.SCREEN.blit(self.hand2, (self.xI + self.dx, self.yI - self.dy))
        if k == 3:
            self.SCREEN.blit(self.hand3, (self.xI + self.dx, self.yI - self.dy))
        if k == 4:
            self.SCREEN.blit(self.hand4, (self.xI + self.dx, self.yI - self.dy))
        if k == 5:
            self.SCREEN.blit(self.hand5, (self.xI + self.dx, self.yI - self.dy))

    def sold_ball(self, k, s):
        if s == 2:
            if k == 1:
                self.SCREEN.blit(self.sold, (self.x1, self.y1))
            if k == 2:
                self.SCREEN.blit(self.sold, (self.x2, self.y2))
            if k == 3:
                self.SCREEN.blit(self.sold, (self.x3, self.y3))
            if k == 4:
                self.SCREEN.blit(self.sold, (self.x4, self.y4))
            if k == 5:
                self.SCREEN.blit(self.sold, (self.x5, self.y5))

    def num_bua(self, num):
        if num == 1:
            self.num_bua1 = self.num_bua1 + 1
        if num == 2:
            self.num_bua2 = self.num_bua2 + 1
        if num == 3:
            self.num_bua3 = self.num_bua3 + 1
        if num == 4:
            self.num_bua4 = self.num_bua4 + 1

    def run(self):
        global lock_shop, MONEY
        while self.shoprunning and lock_shop == False:
            self.clock.tick(self.FPS)
            # insert image
            self.SCREEN.blit(self.bgshop, (0, 0))
            self.show_money(self.xMoney, self.yMoney, "Money: {}".format(self.money), 32)
            self.show_money(self.x1 + 50, self.y1 - 30, "100", 20)
            self.show_money(self.x2 + 50, self.y2 - 30, "100", 20)
            self.show_money(self.x3 + 50, self.y3 - 30, "100", 20)
            self.show_money(self.x4 + 50, self.y4 - 30, "100", 20)
            self.show_money(self.x5 + 50, self.y5 - 30, "100", 20)
            self.SCREEN.blit(self.ball, (self.x1, self.y1))
            self.SCREEN.blit(self.ball, (self.x2, self.y2))
            self.SCREEN.blit(self.ball, (self.x3, self.y3))
            self.SCREEN.blit(self.ball, (self.x4, self.y4))
            self.SCREEN.blit(self.ball, (self.x5, self.y5))
            self.move_hand(self.k)
            self.show_note(self.s)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # su kien nhan thoat
                    self.file.close()
                    self.shoprunning = False
                    pygame.quit()
                    sys.exit()  # thoat chuong trinh

                if event.type == pygame.KEYDOWN:  # su kien co phim nhan xuong
                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = True
                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = True
                    if event.key == pygame.K_SPACE:
                        self.K_SPACE = True
                        pygame.mixer.init()
                        pygame.mixer.music.load('sounds/sold.mp3')
                        pygame.mixer.music.play()

                    if event.key == pygame.K_RETURN:
                        self.K_DONE = True

                if event.type == pygame.KEYUP:  # su kien tha phm
                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = False
                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = False
                    if event.key == pygame.K_SPACE:
                        self.K_SPACE = False
                    if event.key == pygame.K_RETURN:
                        self.K_DONE = False

            if self.K_LEFT and self.s == 0:
                self.k = self.k - 1
                if self.k < 1:
                    self.k = self.k + 5
                if self.k > 5:
                    self.k = self.k - 5
                self.K_LEFT = False
            if self.K_RIGHT and self.s == 0:
                self.k = self.k + 1
                if self.k < 1:
                    self.k = self.k + 5
                if self.k > 5:
                    self.k = self.k - 5
                self.K_RIGHT = False
            if self.K_SPACE and self.s == 0:
                self.file = open('sounds/battat.txt','r')
                self.file.seek(0)
                self.sound = str(self.file.readline())
                # if self.sound == 'On':
                    # pygame.mixer.init()
                    # pygame.mixer.music.load('sounds/sold.mp3')
                    # pygame.mixer.music.play()

                self.s = self.s + 1
                self.K_SPACE = False

            if self.s == 1 and self.money >= 100:
                self.moneyplus = self.moneyplus - 100
                self.num = random.randint(1, 4)
                self.file = open('money/player_money.txt', 'w')
                self.money = self.money + self.moneyplus
                self.file.write(str(self.money))
                self.file.seek(0)
                self.file.close()
                self.s = self.s + 1

            self.num_bua(self.num)
            self.sold_ball(self.k, self.s)
            MONEY = self.money

            if self.s == 1 and self.money <= 99:
                self.SCREEN.blit(self.note3, (self.xnote, self.ynote))

            if self.K_DONE and self.s >= 1:
                lock_shop = True
                self.file = open('sounds/battat.txt','r')
                self.file.seek(0)
                self.sound = str(self.file.readline())
                if self.sound == 'On':
                    if numMap == 1:
                        pygame.mixer.music.load('sounds/cheering1.mp3')
                        pygame.mixer.music.play()
                    if numMap == 2:
                        pygame.mixer.music.load('sounds/cheering2.mp3')
                        pygame.mixer.music.play()
                    if numMap == 3:
                        pygame.mixer.music.load('sounds/cheering3.mp3')
                        pygame.mixer.music.play()
                    if numMap == 4:
                        pygame.mixer.music.load('sounds/cheering4.mp3')
                        pygame.mixer.music.play()
                    if numMap == 5:
                        pygame.mixer.music.load('sounds/cheering5.mp3')
                        pygame.mixer.music.play()
                self.K_DONE = False
            pygame.display.update()


# SHOP = shop()
# SHOP.run()
# main gameplay
class amulet(object):
    def __init__(self, x, y, width, height, hieuung):
        self.x = x
        self.y = y
        self.width = width
        self.height = height  # hộp không thể thay đổi giá trị kể từ lần gán đầu
        self.hieuung = hieuung
        self.LOCKFAST1 = False
        self.LOCKFAST2 = False
        self.LOCKSLOW1 = False
        self.LOCKSLOW2 = False
        self.turn = 0
        self.MOVE = False
        self.MOVEX = 0
        self.MOVEY = 0
        self.STOP = 0
        self.STOPSPEED = 0

    def draw(self, window):
        if numChar != 0:
            if self.hieuung == 1 and self.turn == 0:
                window.blit(chamhoi, (self.x, self.y))
            elif self.hieuung == 2 and self.turn == 0:
                window.blit(chamhoi, (self.x, self.y))
            elif self.hieuung == 3 and self.turn == 0:
                window.blit(chamhoi, (self.x, self.y))
            elif self.hieuung == 4 and self.STOP == 0:
                window.blit(chamhoi, (self.x, self.y))
            elif self.hieuung == 5 and self.turn == 0:
                window.blit(chamhoi, (self.x, self.y))

    def effect(self, chars):
        for char in chars:  # char là biến tượng trưng
            if char.amulet == 5:
                if char.x <= 40 and self.turn == 1:
                    char.amulet = 0
            if char.box[1] + char.height < self.y + self.height and char.box[1] > self.y:
                if char.box[0] + char.width > self.x + 10 and char.box[0] < self.x:
                    if self.turn != 1:
                        char.amulet = self.hieuung
                    if char.amulet == 5 and self.turn == 0:
                        self.turn += 1
                if char.box[0] + char.width < self.x + self.width and char.box[0] > self.x:
                    if char.amulet == 1:
                        window.blit(fast, (char.x, char.y))
                        if self.turn == 0:
                            if self.LOCKFAST1 == False:
                                char.vel += 3
                                self.LOCKFAST1 = True
                                self.turn += 1
                    if char.amulet == 2:
                        window.blit(slow, (char.x, char.y))
                        if self.turn == 0:
                            if self.LOCKSLOW1 == False:
                                char.vel -= 2.2
                                self.LOCKSLOW1 = True
                                self.turn += 1
                    if char.amulet == 3 and self.turn == 0:
                        if self.MOVE == False:
                            self.MOVEX = char.x
                            self.MOVEY = char.y
                            char.x += 200
                            self.MOVE = True
                            self.turn += 1
                    if char.amulet == 4:
                        if self.STOP == 0:
                            self.STOPSPEED = char.vel
                            self.STOP += 1
                        if self.STOP <= 100:
                            char.vel = 0
                            self.STOP += 1
                            window.blit(rock, (char.x + 50, char.y - 10))
                        else:
                            char.vel = self.STOPSPEED
                            self.turn += 1
                    if char.amulet != 1:
                        if self.LOCKFAST2 == False and self.LOCKFAST1 == True:
                            char.vel -= 3
                            self.LOCKFAST2 = True
                    if char.amulet != 2:
                        if self.LOCKSLOW2 == False and self.LOCKSLOW1 == True:
                            char.vel += 2.2
                            self.LOCKSLOW2 = True
                elif char.box[0] + char.width > self.x + self.width:
                    if self.LOCKFAST2 == False and self.LOCKFAST1 == True:
                        char.vel -= 3
                        self.LOCKFAST2 = True
                    if self.LOCKSLOW2 == False and self.LOCKSLOW1 == True:
                        char.vel += 2.2
                        self.LOCKSLOW2 = True
        if self.MOVE == True:
            window.blit(khucgo, (self.MOVEX, self.MOVEY))


class amuletuse(object):
    def __init__(self, AMULETUSE):        
        self.screen = pygame.display.set_mode((1280, 720))
        self.AMULETUSE = AMULETUSE
        self.TURN = 1
        self.EFFECT = False
        self.LOCKFAST1 = False
        self.LOCKSLOW1 = False
        self.RETURN = False
        self.MOVEX = 0
        self.MOVEY = 0
        self.USED = 0
        self.STOP = 0
        self.STOPSPEED = 0
        self.LOCKUSE = False
        self.way = False
        self.AMULET4LOCK = False
    # def notic(self, x, y, money, size):
    #     font = pygame.font.Font("font/minigame.ttf", size)
    #     money = font.render(str(money), True, (255, 255, 255))
    #     self.screen.blit(money, (x, y))
    #     time.sleep(3)    

    def pressenter(self, chars):
        global SOLUONGBUA
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and self.LOCKUSE == False:
                self.LOCKUSE = True
        if keys[pygame.K_RETURN] and self.LOCKUSE == True:
            self.EFFECT = True
        if self.EFFECT == True:
            for char in chars:
                if char.number == numChar:
                    if SOLUONGBUA >= 1:
                        char.amulet = 0
                        if self.AMULETUSE == 1 and self.USED == 0:
                            window.blit(fast, (char.x, char.y))
                            if self.LOCKFAST1 == False:
                                char.vel += 3
                                self.LOCKFAST1 = True
                                self.USED = 1
                        elif self.AMULETUSE == 2 and self.USED == 0:
                            window.blit(slow, (char.x, char.y))
                            if self.LOCKSLOW1 == False:
                                char.vel -= 2
                                self.LOCKSLOW1 = True
                                self.USED = 1
                        elif self.AMULETUSE == 3 and self.USED == 0:
                            self.MOVEX = char.x
                            self.MOVEY = char.y
                            char.x += 200
                            SOLUONGBUA -= 1
                            self.USED = 1
                        elif self.AMULETUSE == 4 and self.USED == 0:
                            self.AMULET4LOCK = True
                        elif self.AMULETUSE == 5 and self.USED == 0:
                            char.amulet = 5
                            self.way = True
                            SOLUONGBUA -= 1
                    if char.amulet != 0 and self.USED == 1:
                        if self.AMULETUSE == 1:
                            char.vel -= 3
                        elif self.AMULETUSE == 2:
                            char.vel += 2
                        SOLUONGBUA -= 1
            self.EFFECT = False
            self.LOCKUSE = False
        if self.AMULETUSE == 3 and self.MOVEX != 0:
            window.blit(khucgo, (self.MOVEX, self.MOVEY))
        for char in chars:
            if char.number == numChar:
                if char.x <= 40 and self.way == True:
                    char.amulet = 0
                    self.way = False
                if self.AMULET4LOCK == True:
                    if self.STOP == 0:
                        self.STOPSPEED = char.vel
                        self.STOP += 1
                    if self.STOP <= 50:
                        window.blit(rock, (char.x + 50, char.y - 10))
                        char.vel = 0
                        self.STOP += 1
                    elif self.STOP > 50:
                        char.vel = self.STOPSPEED
                        SOLUONGBUA -= 1
                        self.AMULET4LOCK = False
                        self.STOP = 0
                if self.AMULETUSE == 1 and char.amulet == 0 and self.LOCKFAST1 == True and self.USED == 1:
                    window.blit(fast, (char.x, char.y))
                elif self.AMULETUSE == 2 and char.amulet == 0 and self.LOCKSLOW1 == True and self.USED == 1:
                    window.blit(slow, (char.x, char.y))


run = True


class player(object):
    def __init__(self, x, y, width, height, vel, number, amulet):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.left = False
        self.right = False
        self.walkCount = 0
        self.top = 0
        self.number = number
        self.slot = 0
        self.K_DONE = False
        self.box = (self.x + 10, self.y + 10, self.width, self.height)
        self.amulet = amulet
        self.LOCKCHOOSE = False
        self.ENTER = False
        self.file = open('money/player_money.txt', 'r')
        self.file.close()

    # ve animation
    def draw(self, win):
        self.box = (self.x + 10, self.y + 10, self.width, self.height)
        if self.walkCount + 1 >= 9 and numMap != 1:
            self.walkCount = 0
        elif self.walkCount + 1 >= 12 and numMap == 1:
            self.walkCount = 0
        if numMap == 1:
            if self.number == 1:
                if self.left:
                    window.blit(nguoi1Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s1_1r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s1_1r[0], (self.x, self.y))
            if self.number == 2:
                if self.left:
                    window.blit(nguoi2Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s1_2r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s1_2r[0], (self.x, self.y))
            if self.number == 3:
                if self.left:
                    window.blit(nguoi3Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s1_3r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s1_3r[0], (self.x, self.y))
            if self.number == 4:
                if self.left:
                    window.blit(nguoi4Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s1_4r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s1_4r[0], (self.x, self.y))
            if self.number == 5:
                if self.left:
                    window.blit(nguoi5Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s1_5r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s1_5r[0], (self.x, self.y))
        if numMap == 2:
            if self.number == 1:
                if self.left:
                    window.blit(ga1Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s2_1r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s2_1r[0], (self.x, self.y))
            if self.number == 2:
                if self.left:
                    window.blit(ga2Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s2_2r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s2_2r[0], (self.x, self.y))
            if self.number == 3:
                if self.left:
                    window.blit(ga3Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s2_3r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s2_3r[0], (self.x, self.y))
            if self.number == 4:
                if self.left:
                    window.blit(ga4Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s2_4r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s2_4r[0], (self.x, self.y))
            if self.number == 5:
                if self.left:
                    window.blit(ga5Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s2_5r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s2_5r[0], (self.x, self.y))
        if numMap == 3:
            if self.number == 1:
                if self.left:
                    window.blit(gau1Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s3_1r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s3_1r[0], (self.x, self.y))
            if self.number == 2:
                if self.left:
                    window.blit(gau2Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s3_2r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s3_2r[0], (self.x, self.y))
            if self.number == 3:
                if self.left:
                    window.blit(gau3Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s3_3r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s3_3r[0], (self.x, self.y))
            if self.number == 4:
                if self.left:
                    window.blit(gau4Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s3_4r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s3_4r[0], (self.x, self.y))
            if self.number == 5:
                if self.left:
                    window.blit(gau5Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s3_5r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s3_5r[0], (self.x, self.y))
        if numMap == 4:
            if self.number == 1:
                if self.left:
                    window.blit(sutu1Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s4_1r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s4_1r[0], (self.x, self.y))
            if self.number == 2:
                if self.left:
                    window.blit(sutu2Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s4_2r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s4_2r[0], (self.x, self.y))
            if self.number == 3:
                if self.left:
                    window.blit(sutu3Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s4_3r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s4_3r[0], (self.x, self.y))
            if self.number == 4:
                if self.left:
                    window.blit(sutu4Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s4_4r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s4_4r[0], (self.x, self.y))
            if self.number == 5:
                if self.left:
                    window.blit(sutu5Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s4_5r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s4_5r[0], (self.x, self.y))
        if numMap == 5:
            if self.number == 1:
                if self.left:
                    window.blit(chon1Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s5_1r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s5_1r[0], (self.x, self.y))
            if self.number == 2:
                if self.left:
                    window.blit(chon2Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s5_2r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s5_2r[0], (self.x, self.y))
            if self.number == 3:
                if self.left:
                    window.blit(chon3Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s5_3r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s5_3r[0], (self.x, self.y))
            if self.number == 4:
                if self.left:
                    window.blit(chon4Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s5_4r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s5_4r[0], (self.x, self.y))
            if self.number == 5:
                if self.left:
                    window.blit(chon5Left[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(s5_5r[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    window.blit(s5_5r[0], (self.x, self.y))

    def keys(self):
        global RUN
        keys = pygame.key.get_pressed()
        if self.amulet == 5:
            self.x -= self.vel
            self.left = True
            self.right = False
        if numChar != 0 and self.x < 1280 - self.width - self.vel - 100 and self.ENTER == True and self.amulet != 5 and RUN==True:  # toc do animation(buoc nhay)
            self.x += self.vel
            self.right = True
            self.left = False

    # xac dinh top ending
    def xdtop(self, TOP, LOCK2, MONEY):
        global SOLUONGBUA, MONEY_CUOC
        if self.x >= (1280 - self.width - self.vel - 100) and self.top == 0:
            self.left = False
            self.right = False
            TOP += 1
            self.top = TOP
        if self.top == 1 and TOP != 5:
            window.blit(cup, (self.x + 65, self.y - 5))
            window.blit(chucmung, (self.x - 300, self.y))
            window.blit(chucmung1, (self.x + -280, self.y - 100))
            window.blit(phaohoa, (self.x + 65, self.y - 50))
        if TOP == 5 and LOCK2 == False and numChar == self.number:
            if self.top == 1:
                self.file = open('sounds/battat.txt', 'r')
                self.file.seek(0)
                self.sound = str(self.file.readline())
                if self.sound == 'On':
                    pygame.mixer.init()
                    pygame.mixer.music.load('sounds/victory.mp3')
                    pygame.mixer.music.play()
                window.blit(s_win, (0, 0))
                keys = pygame.key.get_pressed()
                font = pygame.font.Font("font/minigame.ttf", 40)
                money_image = font.render("Money: {}".format(str(MONEY)), True, (255, 255, 0))
                window.blit(money_image, (20, 0))
                if keys[pygame.K_1]:
                    LOCK2 = True
                    MONEY += MONEY_CUOC * 5
                    MONEY_CUOC = 0
                    self.file = open('money/player_money.txt', 'w')
                    self.file.write(str(MONEY))
                    self.file.seek(0)
                    self.file.close()
                elif keys[pygame.K_2]:
                    LOCK2 = True
                    SOLUONGBUA += 1
            else:
                self.file = open('sounds/battat.txt', 'r')
                self.file.seek(0)
                self.sound = str(self.file.readline())
                if self.sound == 'On':
                    pygame.mixer.init()
                    pygame.mixer.music.load('sounds/lose.mp3')
                    pygame.mixer.music.play()
                window.blit(s_lose, (0, 0))
                font = pygame.font.Font("font/minigame.ttf", 40)
                money_image = font.render("Money: {}".format(str(MONEY)), True, (255, 255, 0))
                window.blit(money_image, (20, 0))
            if pygame.key.get_pressed()[pygame.K_RETURN] and self.top != 0:
                LOCK2 = True
        if LOCK2 == True:
            # if pygame.key.get_pressed()[pygame.K_RETURN]:
            # self.K_DONE = True
            # MainMenu().display_menu()
            if self.top == 1:
                self.x = 475
                self.y = 155
                self.draw(window)
            elif self.top == 2:
                self.x = 475
                self.y = 270
                self.draw(window)
            elif self.top == 3:
                self.x = 475
                self.y = 385
                self.draw(window)
            elif self.top == 4:
                self.x = 475
                self.y = 500
                self.draw(window)
            elif self.top == 5:
                self.x = 475
                self.y = 615
                self.draw(window)

        return TOP, LOCK2, MONEY


def ingame(CHOOSECHAR):
    if CHOOSECHAR != 0:
        if numMap == 1:
            window.blit(race_s1, (0, 0))
        if numMap == 2:
            window.blit(race_s2, (0, 0))
        if numMap == 3:
            window.blit(race_s3, (0, 0))
        if numMap == 4:
            window.blit(race_s4, (0, 0))
        if numMap == 5:
            window.blit(race_s5, (0, 0))


# bat dau game
import time


def redrawGameWindow():
    global LOCKENTERGAME,DEM123,RUN
    if numChar != 0:
        AMULET1.draw(window)
        AMULET2.draw(window)
        AMULET3.draw(window)
        AMULET4.draw(window)
        AMULET5.draw(window)
        AMULET6.draw(window)
        AMULET7.draw(window)
        AMULET1.effect(chars)
        AMULET2.effect(chars)
        AMULET3.effect(chars)
        AMULET4.effect(chars)
        AMULET5.effect(chars)
        AMULET6.effect(chars)
        AMULET7.effect(chars)
        if CHAR1.x == 40:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and LOCKENTERGAME == False:
                    LOCKENTERGAME = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN] and LOCKENTERGAME == True:               
                for char in chars:
                    char.ENTER = True
        if CHAR1.ENTER==True:
            DEM123+=1
            if (DEM123>=1 and DEM123<=15):
                window.blit(so3,(500,300))
            if (DEM123>15 and DEM123<=30):
                window.blit(so2,(500,300))
            if (DEM123>30 and DEM123<=45):
                window.blit(so1,(500,300))
            if (DEM123>45 and DEM123<=60):
                window.blit(start,(500,300))    
            if DEM123>60:
                RUN=True
        if CHAR1.x >= 41 and RUN == True:
            BUA.pressenter(chars)
        CHAR1.keys()
        CHAR1.draw(window)
        CHAR2.keys()
        CHAR2.draw(window)
        CHAR3.keys()
        CHAR3.draw(window)
        CHAR4.keys()
        CHAR4.draw(window)
        CHAR5.keys()
        CHAR5.draw(window)


# run gameplay
run_race = True


def run_gameplay():
    global LOCK2, top, MONEY, lock_rank,LOCKFIX
    global run_race
    while run_race:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_race = False
                pygame.quit()
                sys.exit()

        ingame(numChar)
        redrawGameWindow()
        if LOCK2 == True:
            window.blit(s_ranking, (0, 0))
            pygame.mixer.init()
            pygame.mixer.music.load('sounds/menu.mp3')
            # pygame.mixer.music.play()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                font = pygame.font.Font("font/minigame.ttf", 40)
                money_image = font.render("Money: {}".format(str(MONEY)), True, (255, 255, 0))
                window.blit(money_image, (20, 0))
                lock_rank = False
                #time.sleep(3)
                run_race = False

        top, LOCK2, MONEY = CHAR1.xdtop(top, LOCK2, MONEY)
        top, LOCK2, MONEY = CHAR2.xdtop(top, LOCK2, MONEY)
        top, LOCK2, MONEY = CHAR3.xdtop(top, LOCK2, MONEY)
        top, LOCK2, MONEY = CHAR4.xdtop(top, LOCK2, MONEY)
        top, LOCK2, MONEY = CHAR5.xdtop(top, LOCK2, MONEY)
        pygame.display.update()
    if LOCK2 == True and run_race == False:
        # time.sleep(2)
        window.blit(s_history, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN] and LOCKFIX==False:
                    LOCKFIX=True

                    

# khai bao chung cho ca file
import pygame, random, sys
# toc doc
speed = random.sample((3.9, 4.2, 4.5, 4.8, 5.1), 5)
stt = random.sample((360, 435, 510, 585, 660), 5)
# setting san thuoc tinh mac dinh cho 5 nv
CHAR1 = player(40, stt[0], 30, 30, speed[0], 1, 0)
CHAR2 = player(40, stt[1], 30, 30, speed[1], 2, 0)
CHAR3 = player(40, stt[2], 30, 30, speed[2], 3, 0)
CHAR4 = player(40, stt[3], 30, 30, speed[3], 4, 0)
CHAR5 = player(40, stt[4], 30, 30, speed[4], 5, 0)
LOCK2 = False
run_GP = False
chars = [CHAR1, CHAR2, CHAR3, CHAR4, CHAR5]
# thuoc tinh cho bua
Y = random.sample((360, 435, 510, 585, 660), 5)
X = random.sample((350, 450, 550, 650), 4)
BUA = amuletuse(random.randint(4, 5))  # bua kich hoat
AMULET1 = amulet(X[0], Y[0], 400, 60, 2)
AMULET2 = amulet(X[0], Y[1], 400, 60, 2)
AMULET3 = amulet(X[2], Y[2], 400, 60, 3)
AMULET4 = amulet(X[1], Y[4], 400, 60, 4)
AMULET5 = amulet(X[2], Y[1], 400, 60, 1)
AMULET6 = amulet(X[1], Y[0], 400, 60, 5)
AMULET7 = amulet(X[3], Y[3], 400, 60, random.randint(1, 5))
amulets = [AMULET1, AMULET2, AMULET3, AMULET4, AMULET5, AMULET6, AMULET7]
# cac file do hoa can dung den
s1_1r = [pygame.image.load('image/gameplay/1.1-01.png'), pygame.image.load('image/gameplay/1.2-01.png'),
         pygame.image.load('image/gameplay/1.3-01.png'), pygame.image.load('image/gameplay/1.4-01.png')]
s1_2r = [pygame.image.load('image/gameplay/2.1-01.png'), pygame.image.load('image/gameplay/2.2-01.png'),
         pygame.image.load('image/gameplay/2.3-01.png'), pygame.image.load('image/gameplay/2.4-01.png')]
s1_3r = [pygame.image.load('image/gameplay/3.1-01.png'), pygame.image.load('image/gameplay/3.2-01.png'),
         pygame.image.load('image/gameplay/3.3-01.png'), pygame.image.load('image/gameplay/3.4-01.png')]
s1_4r = [pygame.image.load('image/gameplay/4.1-01.png'), pygame.image.load('image/gameplay/4.2-01.png'),
         pygame.image.load('image/gameplay/4.3-01.png'), pygame.image.load('image/gameplay/4.4-01.png')]
s1_5r = [pygame.image.load('image/gameplay/5.1-01.png'), pygame.image.load('image/gameplay/5.2-01.png'),
         pygame.image.load('image/gameplay/5.3-01.png'), pygame.image.load('image/gameplay/5.4-01.png')]

nguoi1Left = [pygame.image.load('image/gameplay/1.5-01.png'), pygame.image.load('image/gameplay/1.6-01.png'),
              pygame.image.load('image/gameplay/1.7-01.png'), pygame.image.load('image/gameplay/1.8-01.png')]
nguoi2Left = [pygame.image.load('image/gameplay/2.5-01.png'), pygame.image.load('image/gameplay/2.6-01.png'),
              pygame.image.load('image/gameplay/2.7-01.png'), pygame.image.load('image/gameplay/2.8-01.png')]
nguoi3Left = [pygame.image.load('image/gameplay/3.5-01.png'), pygame.image.load('image/gameplay/3.6-01.png'),
              pygame.image.load('image/gameplay/3.7-01.png'), pygame.image.load('image/gameplay/3.8-01.png')]
nguoi4Left = [pygame.image.load('image/gameplay/4.5-01.png'), pygame.image.load('image/gameplay/4.6-01.png'),
              pygame.image.load('image/gameplay/4.7-01.png'), pygame.image.load('image/gameplay/4.8-01.png')]
nguoi5Left = [pygame.image.load('image/gameplay/5.5-01.png'), pygame.image.load('image/gameplay/5.6-01.png'),
              pygame.image.load('image/gameplay/5.7-01.png'), pygame.image.load('image/gameplay/5.8-01.png')]

s2_1r = [pygame.image.load('image/gameplay/ga1.1.png'), pygame.image.load('image/gameplay/ga1.2.png'),
         pygame.image.load('image/gameplay/ga1.3.png')]
s2_2r = [pygame.image.load('image/gameplay/ga2.1.png'), pygame.image.load('image/gameplay/ga2.2.png'),
         pygame.image.load('image/gameplay/ga2.3.png')]
s2_3r = [pygame.image.load('image/gameplay/ga3.1.png'), pygame.image.load('image/gameplay/ga3.2.png'),
         pygame.image.load('image/gameplay/ga3.3.png')]
s2_4r = [pygame.image.load('image/gameplay/ga4.1.png'), pygame.image.load('image/gameplay/ga4.2.png'),
         pygame.image.load('image/gameplay/ga4.3.png')]
s2_5r = [pygame.image.load('image/gameplay/ga5.1.png'), pygame.image.load('image/gameplay/ga5.2.png'),
         pygame.image.load('image/gameplay/ga5.3.png')]

ga1Left = [pygame.image.load('image/gameplay/gaL1.1.png'), pygame.image.load('image/gameplay/gaL1.2.png'),
           pygame.image.load('image/gameplay/gaL1.3.png')]
ga2Left = [pygame.image.load('image/gameplay/gaL2.1.png'), pygame.image.load('image/gameplay/gaL2.2.png'),
           pygame.image.load('image/gameplay/gaL2.3.png')]
ga3Left = [pygame.image.load('image/gameplay/gaL3.1.png'), pygame.image.load('image/gameplay/gaL3.2.png'),
           pygame.image.load('image/gameplay/gaL3.3.png')]
ga4Left = [pygame.image.load('image/gameplay/gaL4.1.png'), pygame.image.load('image/gameplay/gaL4.2.png'),
           pygame.image.load('image/gameplay/gaL4.3.png')]
ga5Left = [pygame.image.load('image/gameplay/gaL5.1.png'), pygame.image.load('image/gameplay/gaL5.2.png'),
           pygame.image.load('image/gameplay/gaL5.3.png')]

s3_1r = [pygame.image.load('image/gameplay/gau1.1.png'), pygame.image.load('image/gameplay/gau1.2.png'),
         pygame.image.load('image/gameplay/gau1.3.png')]
s3_2r = [pygame.image.load('image/gameplay/gau2.1.png'), pygame.image.load('image/gameplay/gau2.2.png'),
         pygame.image.load('image/gameplay/gau2.3.png')]
s3_3r = [pygame.image.load('image/gameplay/gau3.1.png'), pygame.image.load('image/gameplay/gau3.2.png'),
         pygame.image.load('image/gameplay/gau3.3.png')]
s3_4r = [pygame.image.load('image/gameplay/gau4.1.png'), pygame.image.load('image/gameplay/gau4.2.png'),
         pygame.image.load('image/gameplay/gau4.3.png')]
s3_5r = [pygame.image.load('image/gameplay/gau5.1.png'), pygame.image.load('image/gameplay/gau5.2.png'),
         pygame.image.load('image/gameplay/gau5.3.png')]

gau1Left = [pygame.image.load('image/gameplay/gauL1.1.png'), pygame.image.load('image/gameplay/gauL1.2.png'),
            pygame.image.load('image/gameplay/gauL1.3.png')]
gau2Left = [pygame.image.load('image/gameplay/gauL2.1.png'), pygame.image.load('image/gameplay/gauL2.2.png'),
            pygame.image.load('image/gameplay/gauL2.3.png')]
gau3Left = [pygame.image.load('image/gameplay/gauL3.1.png'), pygame.image.load('image/gameplay/gauL3.2.png'),
            pygame.image.load('image/gameplay/gauL3.3.png')]
gau4Left = [pygame.image.load('image/gameplay/gauL4.1.png'), pygame.image.load('image/gameplay/gauL4.2.png'),
            pygame.image.load('image/gameplay/gauL4.3.png')]
gau5Left = [pygame.image.load('image/gameplay/gauL5.1.png'), pygame.image.load('image/gameplay/gauL5.2.png'),
            pygame.image.load('image/gameplay/gauL5.3.png')]

s4_1r = [pygame.image.load('image/gameplay/sutu1.1.png'), pygame.image.load('image/gameplay/sutu1.2.png'),
         pygame.image.load('image/gameplay/sutu1.3.png')]
s4_2r = [pygame.image.load('image/gameplay/sutu2.1.png'), pygame.image.load('image/gameplay/sutu2.2.png'),
         pygame.image.load('image/gameplay/sutu2.3.png')]
s4_3r = [pygame.image.load('image/gameplay/sutu3.1.png'), pygame.image.load('image/gameplay/sutu3.2.png'),
         pygame.image.load('image/gameplay/sutu3.3.png')]
s4_4r = [pygame.image.load('image/gameplay/sutu4.1.png'), pygame.image.load('image/gameplay/sutu4.2.png'),
         pygame.image.load('image/gameplay/sutu4.3.png')]
s4_5r = [pygame.image.load('image/gameplay/sutu5.1.png'), pygame.image.load('image/gameplay/sutu5.2.png'),
         pygame.image.load('image/gameplay/sutu5.3.png')]

sutu1Left = [pygame.image.load('image/gameplay/sutuL1.1.png'), pygame.image.load('image/gameplay/sutuL1.2.png'),
             pygame.image.load('image/gameplay/sutuL1.3.png')]
sutu2Left = [pygame.image.load('image/gameplay/sutuL2.1.png'), pygame.image.load('image/gameplay/sutuL2.2.png'),
             pygame.image.load('image/gameplay/sutuL2.3.png')]
sutu3Left = [pygame.image.load('image/gameplay/sutuL3.1.png'), pygame.image.load('image/gameplay/sutuL3.2.png'),
             pygame.image.load('image/gameplay/sutuL3.3.png')]
sutu4Left = [pygame.image.load('image/gameplay/sutuL4.1.png'), pygame.image.load('image/gameplay/sutuL4.2.png'),
             pygame.image.load('image/gameplay/sutuL4.3.png')]
sutu5Left = [pygame.image.load('image/gameplay/sutuL5.1.png'), pygame.image.load('image/gameplay/sutuL5.2.png'),
             pygame.image.load('image/gameplay/sutuL5.3.png')]

s5_1r = [pygame.image.load('image/gameplay/chon1.1.png'), pygame.image.load('image/gameplay/chon1.2.png'),
         pygame.image.load('image/gameplay/chon1.3.png')]
s5_2r = [pygame.image.load('image/gameplay/chon2.1.png'), pygame.image.load('image/gameplay/chon2.2.png'),
         pygame.image.load('image/gameplay/chon2.3.png')]
s5_3r = [pygame.image.load('image/gameplay/chon3.1.png'), pygame.image.load('image/gameplay/chon3.2.png'),
         pygame.image.load('image/gameplay/chon3.3.png')]
s5_4r = [pygame.image.load('image/gameplay/chon4.1.png'), pygame.image.load('image/gameplay/chon4.2.png'),
         pygame.image.load('image/gameplay/chon4.3.png')]
s5_5r = [pygame.image.load('image/gameplay/chon5.1.png'), pygame.image.load('image/gameplay/chon5.2.png'),
         pygame.image.load('image/gameplay/chon5.3.png')]

chon1Left = [pygame.image.load('image/gameplay/chonL1.1.png'), pygame.image.load('image/gameplay/chonL1.2.png'),
             pygame.image.load('image/gameplay/chonL1.3.png')]
chon2Left = [pygame.image.load('image/gameplay/chonL2.1.png'), pygame.image.load('image/gameplay/chonL2.2.png'),
             pygame.image.load('image/gameplay/chonL2.3.png')]
chon3Left = [pygame.image.load('image/gameplay/chonL3.1.png'), pygame.image.load('image/gameplay/chonL3.2.png'),
             pygame.image.load('image/gameplay/chonL3.3.png')]
chon4Left = [pygame.image.load('image/gameplay/chonL4.1.png'), pygame.image.load('image/gameplay/chonL4.2.png'),
             pygame.image.load('image/gameplay/chonL4.3.png')]
chon5Left = [pygame.image.load('image/gameplay/chonL5.1.png'), pygame.image.load('image/gameplay/chonL5.2.png'),
             pygame.image.load('image/gameplay/chonL5.3.png')]
# do hoa main gameplay
tiencuoc = pygame.image.load('image/chontiencuoc.png')
s_ranking = pygame.image.load('image/gameplay/xephang.png')
lock_rank = False
s_history = pygame.image.load('image/gameplay/history.png')
s_win = pygame.image.load('image/gameplay/win.png')
s_lose = pygame.image.load('image/gameplay/lose.png')
cup = pygame.image.load('image/gameplay/cup.png')
phaohoa = pygame.image.load('image/gameplay/phaohoa.png')
chucmung = pygame.image.load('image/gameplay/chucmung.png')
chucmung1 = pygame.image.load('image/gameplay/chucmung1.png')

c_map = pygame.image.load('image/gameplay/chonset.png')
c_s1 = pygame.image.load('image/gameplay/set1chon.png')
c_s2 = pygame.image.load('image/gameplay/set2chon.png')
c_s3 = pygame.image.load('image/gameplay/set3chon.png')
c_s4 = pygame.image.load('image/gameplay/set4chon.png')
c_s5 = pygame.image.load('image/gameplay/set5chon.png')

race_s1 = pygame.image.load('image/gameplay/set1.png')
race_s2 = pygame.image.load('image/gameplay/set2.png')
race_s3 = pygame.image.load('image/gameplay/set3.png')
race_s4 = pygame.image.load('image/gameplay/set4.png')
race_s5 = pygame.image.load('image/gameplay/set5.png')

rock = pygame.image.load('image/bua/rock.png')  # NEW
slow = pygame.image.load('image/bua/slow.png')  # NEW
fast = pygame.image.load('image/bua/fast.png')  # NEW
khucgo = pygame.image.load('image/bua/khucgo.png')  # NEW
chamhoi = pygame.image.load('image/bua/chamhoi.png')  # NEW
so1=pygame.image.load('image/gameplay/1.png')
so2=pygame.image.load('image/gameplay/2.png')
so3=pygame.image.load('image/gameplay/3.png')
start = pygame.image.load('image/gameplay/batdau.png')
top = 0
MONEY = 0
MONEY_CUOC = 0
c_char = 0
clock = pygame.time.Clock()
choose_key = False
number = 0
tempt_num1 = 0
tempt_num2 = 0

numMap = 0
numChar = 0
back_key = False
lock_map = False
lock_shop = False
lock_money = False
count_pressKey = 0
count_pressNumKey = 0
# kiem tra screen dang run
running_map = False
running_display = False
running_datcuoc = False
running_shop = False
desktop = c_map
wrong_key = False


def check_input():
    global choose_key, back_key, number, numChar, count_pressKey, count_pressNumKey
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5:
                count_pressKey = count_pressKey + 1
            if event.key == pygame.K_RETURN:
                choose_key = True
            if event.key == pygame.K_ESCAPE:
                back_key = True
            if event.key == pygame.K_1:
                number = 1
            if event.key == pygame.K_2:
                number = 2
            if event.key == pygame.K_3:
                number = 3
            if event.key == pygame.K_4:
                number = 4
            if event.key == pygame.K_5:
                number = 5

def reset_keys():
    global choose_key, number, back_key, count_pressKey
    choose_key, number, back_key, count_pressKey = False, 0, False, 0


def choose_map_and_char():
    global LOCKCHONSET,running_map, numChar, numMap, tempt_num, count_pressKey, lock_map
    if count_pressKey <= 1 and lock_map == False:
        running_map = True
    if running_map:
        tempt_num = number
        if tempt_num == 1 and (LOCKCHONSET==0 or LOCKCHONSET==tempt_num):
            window.blit(c_s1, (0, 0))
            LOCKCHONSET=1
        if tempt_num == 2 and (LOCKCHONSET==0 or LOCKCHONSET==tempt_num):
            window.blit(c_s2, (0, 0))
            LOCKCHONSET=2
        if tempt_num == 3 and (LOCKCHONSET==0 or LOCKCHONSET==tempt_num):
            window.blit(c_s3, (0, 0))
            LOCKCHONSET=3
        if tempt_num == 4 and (LOCKCHONSET==0 or LOCKCHONSET==tempt_num):
            window.blit(c_s4, (0, 0))
            LOCKCHONSET=4
        if tempt_num == 5 and (LOCKCHONSET==0 or LOCKCHONSET==tempt_num):
            window.blit(c_s5, (0, 0))
            LOCKCHONSET=5
        if count_pressKey == 1:
            numMap = tempt_num
    if count_pressKey == 2 and lock_map == False and numChar == 0:
        numChar = number
        running_map = False
        count_pressKey = count_pressKey + 1
        lock_map = True
        reset_keys()
        return numMap, numChar

def datcuoc():
    global running_datcuoc, lock_map, running_map, number, MONEY, MONEY_CUOC, desktop, lock_money
    file = open('money/player_money.txt', 'r')
    money = int(file.readline().split('=')[0])
    file.close()
    money_cuoc = 0
    if count_pressKey <= 1 and lock_money == False and lock_map == True:
        running_datcuoc = True
    if running_datcuoc:
        pygame.init()
        desktop = tiencuoc
        font = pygame.font.Font("font/minigame.ttf", 32)
        money_image = font.render("Money: {}".format(str(money)), True, (255, 255, 0))
        desktop.blit(money_image, (20, 0))
        if number == 1 and money >= 200:
            money_cuoc = 200
            lock_money = True
            file = open('money/player_money.txt', 'w')
            money = money - money_cuoc
            file.write(str(money))
            file.close()

        if number == 2 and money >= 500:
            money_cuoc = 500
            lock_money = True
            file = open('money/player_money.txt', 'w')
            money = money - money_cuoc
            file.write(str(money))
            file.close()

        if number == 3 and money >= 1000:
            money_cuoc = 1000
            lock_money = True
            file = open('money/player_money.txt', 'w')
            money = money - money_cuoc
            file.write(str(money))
            file.close()

        if number == 4 and money >= 2000:
            money_cuoc = 2000
            lock_money = True
            file = open('money/player_money.txt', 'w')
            money = money - money_cuoc
            file.write(str(money))
            file.close()

        reset_keys()
        MONEY_CUOC = money_cuoc
        return money


def shopping():
    global running_shop, desktop
    if lock_money == True and lock_shop == False:
        running_shop = True
    if running_shop:
        SHOP().run()
    if lock_shop == True:
        run_gameplay()


def display_gameplay():
    i=0
    global LOCKFIX,LOCKCHONSET,speed,Y,LOCK2,run_GP,run_race,lock_rank,DEM123,LOCKENTERGAME,RUN,DEMLOAD,LOAD,window,top,c_char,choose_key,number,tempt_num1,tempt_num2,numMap,numChar,back_key,lock_map,lock_shop,lock_money,count_pressKey,count_pressNumKey,running_map,running_display,running_datcuoc,running_shop,wrong_key,desktop,wrong_key#NEW
    window = pygame.display.set_mode((1280, 720))
    global running_display
    running_display = True
    while running_display:
        window.blit(desktop, (0, 0))
        check_input()
        choose_map_and_char()
        datcuoc()
        shopping()
        if LOCK2==True and run_race==False and LOCKFIX==True:
            pygame.mixer.music.play()
            SHOP.shoprunning = True
            game.bienphu.g.run_display = True
            game.bienphu.g.gamerunning=True
            c_char = 0
            clock = pygame.time.Clock()
            choose_key = False
            number = 0
            tempt_num1 = 0
            tempt_num2 = 0
            LOAD=True
            top=0
            numMap = 0
            numChar = 0
            back_key = False
            lock_map = False
            lock_shop = False
            lock_money = False
            count_pressKey = 0
            count_pressNumKey = 0
            running_map = False
            running_display = False
            running_datcuoc = False
            running_shop = False
            desktop = c_map
            wrong_key = False
            TAM.BIENTAM=1
            DEM123=0
            LOCKENTERGAME = False
            RUN=False

            LOCK2 = False
            run_GP = False
            run_race = True
            lock_rank = False
            for char in chars:
                char.left=False
                char.right=False
                char.walkCount=0
                char.top = 0
                char.slot = 0
                char.K_DONE = False
                char.LOCKCHOOSE = False
                char.ENTER = False
                char.x=40
                char.y=Y[i]
                char.vel=speed[i]
                char.amulet=0
                i+=1
            i=0
            for amulet in amulets:
                amulet.LOCKFAST1 = False
                amulet.LOCKFAST2 = False
                amulet.LOCKSLOW1 = False
                amulet.LOCKSLOW2 = False
                amulet.turn = 0
                amulet.MOVE = False
                amulet.MOVEX = 0
                amulet.MOVEY = 0
                amulet.STOP = 0
                amulet.STOPSPEED = 0
            BUA = amuletuse(random.randint(4, 5))
            BUA.TURN=1
            BUA.EFFECT=False
            BUA.LOCKFAST1=False
            BUA.LOCKSLOW1=False
            BUA.RETURN=False
            BUA.MOVEX=0
            BUA.MOVEY=0
            BUA.USED=0
            BUA.STOP=0
            BUA.STOPSPEED=0
            BUA.LOCKUSE=False
            BUA.way=False
            BUA.AMULET4LOCK=False
            LOCKCHONSET=0
            LOCKFIX=False
        pygame.display.update()
class TAM():
    BIENTAM=0
# display_gameplay()
