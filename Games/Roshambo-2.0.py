from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import random

Window = Tk()

Window.geometry("420x380")
Window.title("Ro-Sham-Bo")

font = font.Font(family="Helvetica", size=23, weight="bold")
size = 100, 100

rock = Image.open(r"")    # RECONFIGURE PATH TO
paper = Image.open(r"")   # YOUR ABSOLUTE
scissor = Image.open(r"") # FILE PATH
sword = Image.open(r"")   # FOR IT
reset = Image.open(r"")   # TO WORK

rock = rock.resize(size)
paper = paper.resize(size)
scissor = scissor.resize(size)
sword = sword.resize(size)
reset = reset.resize(size)

rock = ImageTk.PhotoImage(rock)
paper = ImageTk.PhotoImage(paper)
scissor = ImageTk.PhotoImage(scissor)
sword = ImageTk.PhotoImage(sword)
reset = ImageTk.PhotoImage(reset)

VS = Label(Window, image=sword)
VS.grid(column=1, row=1, padx=30)

choices = ["rock", "paper", "scissor"]


def rock_logic():
    enemy_choice = random.choice(choices)
    if enemy_choice == "rock":
        rock_rock()
    elif enemy_choice == "paper":
        rock_paper()
    elif enemy_choice == "scissor":
        rock_scissor()


def paper_logic():
    enemy_choice = random.choice(choices)
    if enemy_choice == "rock":
        paper_rock()
    elif enemy_choice == "paper":
        paper_paper()
    elif enemy_choice == "scissor":
        paper_scissor()


def scissor_logic():
    enemy_choice = random.choice(choices)
    if enemy_choice == "rock":
        scissor_rock()
    elif enemy_choice == "paper":
        scissor_paper()
    elif enemy_choice == "scissor":
        scissor_scissor()


def home():
    player_R = Button(Window, image=rock, command=rock_logic)
    player_P = Button(Window, image=paper, command=paper_logic)
    player_S = Button(Window, image=scissor, command=scissor_logic)

    enemy_R = Label(Window, image=rock)
    enemy_P = Label(Window, image=paper)
    enemy_S = Label(Window, image=scissor)

    player_R.grid(column=0, row=0, padx=10, pady=10)
    player_P.grid(column=0, row=1, padx=10, pady=10)
    player_S.grid(column=0, row=2, padx=10, pady=10)

    enemy_R.grid(column=2, row=0, padx=10, pady=10)
    enemy_P.grid(column=2, row=1, padx=10, pady=10)
    enemy_S.grid(column=2, row=2, padx=10, pady=10)

    tie = Label(Window, text="               ", font=font)
    tie.grid(column=1, row=2, padx=10, pady=10)


def rock_rock():
    player_R = Label(Window, image=rock, bg="gray")
    player_P = Button(Window, image=paper)
    player_S = Button(Window, image=scissor)

    enemy_R = Label(Window, image=rock, bg="gray")
    enemy_P = Label(Window, image=paper)
    enemy_S = Label(Window, image=scissor)

    player_R.grid(column=0, row=0, padx=10, pady=10)
    player_P.grid(column=0, row=1, padx=10, pady=10)
    player_S.grid(column=0, row=2, padx=10, pady=10)

    enemy_R.grid(column=2, row=0, padx=10, pady=10)
    enemy_P.grid(column=2, row=1, padx=10, pady=10)
    enemy_S.grid(column=2, row=2, padx=10, pady=10)

    tie = Label(Window, text="It's a Tie", font=font)
    tie.grid(column=1, row=2, padx=10, pady=10)


def rock_paper():
    player_R = Label(Window, image=rock, bg="red")
    player_P = Button(Window, image=paper)
    player_S = Button(Window, image=scissor)

    enemy_R = Label(Window, image=rock)
    enemy_P = Label(Window, image=paper, bg="green")
    enemy_S = Label(Window, image=scissor)

    player_R.grid(column=0, row=0, padx=10, pady=10)
    player_P.grid(column=0, row=1, padx=10, pady=10)
    player_S.grid(column=0, row=2, padx=10, pady=10)

    enemy_R.grid(column=2, row=0, padx=10, pady=10)
    enemy_P.grid(column=2, row=1, padx=10, pady=10)
    enemy_S.grid(column=2, row=2, padx=10, pady=10)

    tie = Label(Window, text="You Lose", font=font)
    tie.grid(column=1, row=2, padx=10, pady=10)


def rock_scissor():
    player_R = Label(Window, image=rock, bg="green")
    player_P = Button(Window, image=paper)
    player_S = Button(Window, image=scissor)

    enemy_R = Label(Window, image=rock)
    enemy_P = Label(Window, image=paper)
    enemy_S = Label(Window, image=scissor, bg="red")

    player_R.grid(column=0, row=0, padx=10, pady=10)
    player_P.grid(column=0, row=1, padx=10, pady=10)
    player_S.grid(column=0, row=2, padx=10, pady=10)

    enemy_R.grid(column=2, row=0, padx=10, pady=10)
    enemy_P.grid(column=2, row=1, padx=10, pady=10)
    enemy_S.grid(column=2, row=2, padx=10, pady=10)

    tie = Label(Window, text="You Win", font=font)
    tie.grid(column=1, row=2, padx=10, pady=10)


def paper_rock():
    player_R = Button(Window, image=rock)
    player_P = Label(Window, image=paper, bg="green")
    player_S = Button(Window, image=scissor)

    enemy_R = Label(Window, image=rock, bg="red")
    enemy_P = Label(Window, image=paper)
    enemy_S = Label(Window, image=scissor)

    player_R.grid(column=0, row=0, padx=10, pady=10)
    player_P.grid(column=0, row=1, padx=10, pady=10)
    player_S.grid(column=0, row=2, padx=10, pady=10)

    enemy_R.grid(column=2, row=0, padx=10, pady=10)
    enemy_P.grid(column=2, row=1, padx=10, pady=10)
    enemy_S.grid(column=2, row=2, padx=10, pady=10)

    tie = Label(Window, text="You Win", font=font)
    tie.grid(column=1, row=2, padx=10, pady=10)


def paper_paper():
    player_R = Button(Window, image=rock)
    player_P = Label(Window, image=paper, bg="gray")
    player_S = Button(Window, image=scissor)

    enemy_R = Label(Window, image=rock)
    enemy_P = Label(Window, image=paper, bg="gray")
    enemy_S = Label(Window, image=scissor)

    player_R.grid(column=0, row=0, padx=10, pady=10)
    player_P.grid(column=0, row=1, padx=10, pady=10)
    player_S.grid(column=0, row=2, padx=10, pady=10)

    enemy_R.grid(column=2, row=0, padx=10, pady=10)
    enemy_P.grid(column=2, row=1, padx=10, pady=10)
    enemy_S.grid(column=2, row=2, padx=10, pady=10)

    tie = Label(Window, text="It's a Tie", font=font)
    tie.grid(column=1, row=2, padx=10, pady=10)


def paper_scissor():
    player_R = Button(Window, image=rock)
    player_P = Label(Window, image=paper, bg="red")
    player_S = Button(Window, image=scissor)

    enemy_R = Label(Window, image=rock)
    enemy_P = Label(Window, image=paper)
    enemy_S = Label(Window, image=scissor, bg="green")

    player_R.grid(column=0, row=0, padx=10, pady=10)
    player_P.grid(column=0, row=1, padx=10, pady=10)
    player_S.grid(column=0, row=2, padx=10, pady=10)

    enemy_R.grid(column=2, row=0, padx=10, pady=10)
    enemy_P.grid(column=2, row=1, padx=10, pady=10)
    enemy_S.grid(column=2, row=2, padx=10, pady=10)

    tie = Label(Window, text="You Lose", font=font)
    tie.grid(column=1, row=2, padx=10, pady=10)


def scissor_rock():
    player_R = Button(Window, image=rock)
    player_P = Button(Window, image=paper)
    player_S = Label(Window, image=scissor, bg="red")

    enemy_R = Label(Window, image=rock, bg="green")
    enemy_P = Label(Window, image=paper)
    enemy_S = Label(Window, image=scissor)

    player_R.grid(column=0, row=0, padx=10, pady=10)
    player_P.grid(column=0, row=1, padx=10, pady=10)
    player_S.grid(column=0, row=2, padx=10, pady=10)

    enemy_R.grid(column=2, row=0, padx=10, pady=10)
    enemy_P.grid(column=2, row=1, padx=10, pady=10)
    enemy_S.grid(column=2, row=2, padx=10, pady=10)

    tie = Label(Window, text="You Lose", font=font)
    tie.grid(column=1, row=2, padx=10, pady=10)


def scissor_paper():
    player_R = Button(Window, image=rock)
    player_P = Button(Window, image=paper)
    player_S = Label(Window, image=scissor, bg="green")

    enemy_R = Label(Window, image=rock)
    enemy_P = Label(Window, image=paper, bg="red")
    enemy_S = Label(Window, image=scissor)

    player_R.grid(column=0, row=0, padx=10, pady=10)
    player_P.grid(column=0, row=1, padx=10, pady=10)
    player_S.grid(column=0, row=2, padx=10, pady=10)

    enemy_R.grid(column=2, row=0, padx=10, pady=10)
    enemy_P.grid(column=2, row=1, padx=10, pady=10)
    enemy_S.grid(column=2, row=2, padx=10, pady=10)

    tie = Label(Window, text="You Win", font=font)
    tie.grid(column=1, row=2, padx=10, pady=10)


def scissor_scissor():
    player_R = Button(Window, image=rock)
    player_P = Button(Window, image=paper)
    player_S = Label(Window, image=scissor, bg="gray")

    enemy_R = Label(Window, image=rock)
    enemy_P = Label(Window, image=paper)
    enemy_S = Label(Window, image=scissor, bg="gray")

    player_R.grid(column=0, row=0, padx=10, pady=10)
    player_P.grid(column=0, row=1, padx=10, pady=10)
    player_S.grid(column=0, row=2, padx=10, pady=10)

    enemy_R.grid(column=2, row=0, padx=10, pady=10)
    enemy_P.grid(column=2, row=1, padx=10, pady=10)
    enemy_S.grid(column=2, row=2, padx=10, pady=10)

    tie = Label(Window, text="It's a Tie", font=font)
    tie.grid(column=1, row=2, padx=10, pady=10)


restart = Button(Window, image=reset, command=home)
restart.grid(column=1, row=0, padx=30)

home()
Window.mainloop()
