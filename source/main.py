from tkinter import *

username_info = ''
password_info = ''
username = ''
password = ''
username_entry = ''
password_entry = ''
lock_login = False
pass_checked = 0
id_checked = 0
money_checked = 0
# main_screen()
from game import Game,bienphu
def start_game():  # ham bat dau game
    g = bienphu.g
    while g.running:
        g.curr_menu.display_menu()
        g.game_loop()


import glob, os, time, pygame


def find_file(username):  # tim xem co file nao ten username.txt trong thu muc player_date khong neu co return 1
    # os.chdir("./player_data")
    dataPath="./player_data"
    dataFol=os.listdir(dataPath)
    username=username+".txt"
    if username in dataFol:
       return 1
   


def check_user():
    username_info = username.get()
    password_info = password.get() + "\n"
    if find_file(
            username.get()):  # tim xem co file txt nao ten trung khop voi id nhap vao khong. neu co nghia la id dung
        global lock_login
        userPath=f"./player_data/{username_info}.txt"
        with open(userPath, "r") as file:
            lines = file.readlines()
            correct_pass = lines[0]
            correct_money = lines[1]
        if password_info == correct_pass:  # so sanh neu pass nhap vao dung voi dong 1 trong txt thi pass nhap vao dung
            global pass_checked, id_checked, money_checked
            pass_checked = password.get()
            id_checked = username_info
            money_checked = correct_money
            print("Welcome back " + username_info)
            lock_login = True
            # os.chdir("./")
            loginbox.destroy()
            start_game()
        else:  # neu pass khong khop bat nhap lai
            print("wrong password TRY AGAIN")
            Label(screen1, text="Wrong password please TRY AGAIN!", fg="red", font=("calibri", 11),bg='#242254').pack()


    else:
        print("New register " + username_info)
        file = open(userPath, "w")
        file.write(password_info)  # ghi vao dong 1 trong file txt : id +enter
        file.write("5000")  # ghi vao dong 2 so tien mat dinh cho tai khoan moi tao 5000$
        file.close()
        Label(screen1, text="Registration Sucess\n Welcome "+username_info+" !\nPlease login and enjoy ^^!", fg="green", font=("calibri", 12),bg='#242254').pack()

    username_entry.delete(0, END)
    password_entry.delete(0, END)


def login():
    global screen1
    screen1 = loginbox
    screen1.title("Login MONEY_HEI$T")
    screen1.geometry("420x500")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="WELCOME\n",font=('font/title', 15),bg='#242254',fg="#00FFFF").pack()
    Label(screen1, text="Please login or Register",font=('font/title', 8),bg='#242254',fg="#00FFFF").pack()
    Label(screen1, text="",bg='#242254').pack()
    Label(screen1, text="Username",bg='#242254',fg="#00FFFF").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password",bg='#242254',fg="#00FFFF").pack()
    password_entry = Entry(screen1, textvariable=password,show="*")
    password_entry.pack()
    Label(screen1, text="",bg='#242254').pack()
    Button(screen1, text="Login/Register", width=12, height=1, command=check_user).pack()


def main_screen_login():
    global loginbox
    if lock_login == False:
        loginbox = Tk()
        loginbox.wm_iconbitmap('image/icon.png')
        loginbox.configure(background='#242254')
        courtImg = PhotoImage(file='image/title.png')
        photo = Label(loginbox, image=courtImg, height=160, width=420)
        photo.image = courtImg
        photo.pack()
        login()
        loginbox.mainloop()


# id pass va money khi nguoi choi login duoc vao game duoc lay tu ham check_user
# money_checked
# id_checked
# pass_checked
# lay thong tin nguoi dung
# class Player_info():
#     def __init__(self):
#         self.user_name = 0
#         self.user_pass = 0
#         self.user_money = 0

#     def check_money(self):
#         self.user_money = money_checked
#         return self.user_money

#     def check_id(self):
#         self.user_name = id_checked
#         return self.user_name

#     def check_pass(self):
#         self.user_pass = pass_checked
#         return self.user_pass

#     pass


main_screen_login()
# test thu lay thong tin tien hien co cua 1 tai khoan
# tai khoan dung de test id : Admin pass: 123 hien dang co 1000 tien
# class nay dung de lay thong tin qua file khac sai tiep. vi du lay thong tin money qua file gameplay sai tiep
# info=Player_info()
# money=info.check_money()

