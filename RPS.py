import tkinter as tk
from PIL import Image, ImageTk
from random import randint

rules = "1.Rock beats Sciccors, Sciccors beats Paper, Paper beats Rock\n2.First to score 10 is the winner\n3.Game Ends after scoring 10 points"

# Window Setup
window = tk.Tk()
window.geometry('640x480')
window.title("Rock Paper Scissors")
pick = 0
user_score = 0
Smith_score = 0
Champian =''

# Name Submission Button
def name_submit():
    global user_score, Smith_score, Champian, pick
    pick = 0
    user_score = 0
    Smith_score = 0
    Champian =''
    main.pack_forget()
    text = user_name.get()
    user_label.config(text=text)
    game.pack(fill='both',expand=True)

def bot_choice(pick_value):
    bot_list = [rock,paper,scissors]
    global pick 
    pick = randint(0,2)
    bot_img = tk.Label(game, image=bot_list[pick], bg='#FFA586')
    bot_img.place(x=400,y=125)

# Rock Button
def rock_button():
    bot_choice(pick)
    cho_img = tk.Label(game, image=rock, bg='#FFA586')
    cho_img.place(x=130,y=125)
    winner(0,pick)

# Scisscor Button
def sciccor_button():
    bot_choice(pick)
    cho_img = tk.Label(game, image=scissors, bg='#FFA586')
    cho_img.place(x=130,y=125)
    winner(2,pick)

# Paper Button
def paper_button():
    bot_choice(pick)
    cho_img = tk.Label(game, image=paper, bg='#FFA586')
    cho_img.place(x=130,y=125)
    winner(1,pick)

def winner(user_value,pick_value):   # Rock 0  Paper 1 Sciccors 2
    global user_score, Smith_score, Champian, pick
    if user_value == pick_value :
        winner_label.config(text="TIE. . . .")
    if user_value == 0:
        if pick_value == 1:
            winner_label.config(text="You Lose. . .! Paper covers Stone")
            Smith_score += 1
            U_score_label.config(text=user_score)
            bot_score_label.config(text=Smith_score)
        elif pick_value == 2:
            winner_label.config(text="You Win. . .! Rock Smashes Scissors")
            user_score += 1
            U_score_label.config(text=user_score)
            bot_score_label.config(text=Smith_score)
    if user_value == 1:
        if pick_value == 0:
            winner_label.config(text="You Win. . .! Paper covers Stone")
            user_score += 1
            U_score_label.config(text=user_score)
            bot_score_label.config(text=Smith_score)
        elif pick_value == 2:
            winner_label.config(text="You Lose. . .! Scissors cuts Paper")
            Smith_score += 1
            U_score_label.config(text=user_score)
            bot_score_label.config(text=Smith_score)
    if user_value == 2:
        if pick_value == 0:
            winner_label.config(text="You Lose. . .! Rock smashes Scissors")
            Smith_score += 1
            U_score_label.config(text=user_score)
            bot_score_label.config(text=Smith_score)
        elif pick_value == 1:
            winner_label.config(text="You Win. . .! Scissors cuts Paper")
            user_score +=1
            U_score_label.config(text=user_score)
            bot_score_label.config(text=Smith_score)
    
    if user_score == 10 or Smith_score == 10:
        if user_score > Smith_score:
            Champian = "Congratulations You Won the Game"
        else:
            Champian = "Better luck next time. . .Smith Won the Game"
        game.pack_forget()
        result.pack(fill='both',expand=True)
        result_text.config(text=Champian)
        pick = 0
        user_score = 0
        Smith_score = 0
        Champian =''

def new_game():
    result.pack_forget()
    main.pack(fill="both", expand=True)

# Main Menu Image Setup
img = Image.open('rrrr.png')
resize_img = img.resize((375,215))
m_img = ImageTk.PhotoImage(resize_img)

# Rock Image Setup
r_img = Image.open('rock.png')
rock_img = r_img.resize((103,95))
rock = ImageTk.PhotoImage(rock_img)

# Scissor Image Setup
s_img = Image.open('scissors.png')
scissors_img = s_img.resize((103,95))
scissors = ImageTk.PhotoImage(scissors_img)

# Paper Image Setup
p_img = Image.open('paper.png')
paper_img = p_img.resize((103,95))
paper = ImageTk.PhotoImage(paper_img)

# PAGE 1 MAIN MENU 
main = tk.Frame(window, bg="#E8BCB9")
main.pack(fill='both',expand=True)

main_title = tk.Label(main, text="ROCK PAPER SCISSOR", font=('Arial Rounded MT Bold',20), bg='#E8BCB9')
main_title.pack()
main_img_label = tk.Label(main, image=m_img, bg='#E8BCB9', relief='solid', bd=2)
main_img_label.place(x=125,y=65)

get_info = tk.Label(main, text="Enter You Name", font=('Arial Rounded MT Bold',16), bg='#E8BCB9')
get_info.place(x=225,y=290)

user_name = tk.Entry(main, width=25, bg='#E8BCB9')
user_name.config(bg='#FBE4D8')
user_name.place(x=233,y=325)

name_submit = tk.Button(main, text='Start', width=20,command=name_submit)
name_submit.place(x=236,y=360)

rules_name = tk.Label(main, text="Rules", font=('Arial Rounded MT Bold',14), bg='#E8BCB9')
rules_name.place(x=280,y=390)

rules_info = tk.Label(main, text=rules, font=('Arial Rounded MT Bold',12), bg='#E8BCB9')
rules_info.place(x=60,y=415)

# PAGE 2 GAME STARTS HERE
game = tk.Frame(window, bg='#FFA586')

game_label = tk.Label(game, text='ROCK PAPER SCISSOR', font=('Arial Rounded MT Bold',20), bg='#FFA586')
game_label.pack()

user_label = tk.Label(game, text='', font=('Arial Rounded MT Bold',16), bg='#FFA586')
user_label.place(x=130, y=50)

U_score_label = tk.Label(game, font=('Arial Rounded MT Bold',16), bg='#FFA586')
U_score_label.place(x=260,y=50)

pc_label = tk.Label(game, text='Smith', font=('Arial Rounded MT Bold',16), bg='#FFA586')
pc_label.place(x=400,y=50)

bot_score_label = tk.Label(game, font=('Arial Rounded MT Bold',16), bg='#FFA586')
bot_score_label.place(x=490,y=50)

# rock_sel = tk.Label(game, image=rock, bg='#FFA586', relief='solid', bd=2)
rock_button = tk.Button(game, image=rock, command=rock_button, relief='solid', bd=2)
rock_button.place(x=75,y=300)

# paper_sel = tk.Label(game, image=paper, bg='#FFA586', relief='solid', bd=2)
paper_button = tk.Button(game, image=paper, command=paper_button ,relief='solid', bd=2)
paper_button.place(x=265,y=300)

# scissor_sel = tk.Label(game, image=scissors, bg='#FFA586', relief='solid', bd=2)
scissor_button = tk.Button(game, image=scissors, command=sciccor_button, relief='solid', bd=2)
scissor_button.place(x=450,y=300)

winner_label = tk.Label(game, font=('Arial Rounded MT Bold',16), bg='#FFA586')
winner_label.place(x=175,y=425)

# Result Page
result = tk.Frame(window, bg='#C38EB4')
result_text = tk.Label(result, font=('Arial Rounded MT Bold',20), bg='#C38EB4')
result_text.place(x=50,y=150)

new_game_button = tk.Button(result, text="New Game",font=('Arial Rounded MT Bold',12), bg='#C38EB4', command=new_game)
new_game_button.place(x=265,y=300)

window.mainloop()