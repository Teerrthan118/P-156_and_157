from tkinter import *
from PIL import ImageTk, Image
import random

root=Tk()
root.title("Endless Pokemon Game")
root.geometry("1000x1000")
root.configure(background="orange2")

abra =ImageTk.PhotoImage(Image.open ("abra.jpg"))
bulbasour =ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
button=ImageTk.PhotoImage(Image.open ("button.jpg"))
charmender =ImageTk.PhotoImage(Image.open ("charmender.jpg"))
lyvasour =ImageTk.PhotoImage(Image.open ("lyvasour.jpg"))
jigglypuff =ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
kadabra =ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
meowth =ImageTk.PhotoImage(Image.open ("meowth.jpg"))
nidoking =ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
paras =ImageTk.PhotoImage(Image.open ("paras.jpg"))
persion =ImageTk.PhotoImage(Image.open ("persion.jpg"))
pikachu =ImageTk.PhotoImage(Image.open ("pikachu.jpg"))


player1 = Label(root, text = "Player 1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor =  CENTER)

player2 = Label(root, text = "Player 2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely = 0.3 , anchor =  CENTER)

player_1_score_label = Label(root , bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor =  CENTER)

player_2_score_label = Label(root , bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor =  CENTER)

image = Label(root,bg = "white", fg = "black")
image.place(relx = 0.5, rely = 0.5 , anchor =  CENTER)

name_list = [abra,bulbasour,charmender,lyvasour,jigglypuff,kadabra,meowth,nidoking,paras,persion,pikachu]
hp_list = [30,60,50,70,70,100,60,90,40,70,200,40,50]

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(0,10)
    random_pokemon = name_list[random_no]
    image["image"] = random_pokemon
    random_power_list = hp_list[random_no]
    player1_score = player1_score + random_power_list
    player_1_score_label["text"] = player1_score

player2_score = 0

def player2():
    global player2_score
    random_no2 = random.randint(0,10)
    random_pokemon2 = name_list[random_no2]
    image["image"] = random_pokemon2
    random_power_list2 = hp_list[random_no2]
    player2_score = player2_score + random_power_list2
    player_2_score_label["text"] = player2_score
    
player_1_btn = Button(root, image = button, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor =  CENTER)

player_2_btn = Button(root, image = button, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6 , anchor =  CENTER)

root.mainloop()