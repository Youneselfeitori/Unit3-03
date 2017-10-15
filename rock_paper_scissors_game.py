
# Created by : Younes Elfeitori
# Created on : Oct 2017
# Created for : ICS3UR
# This program is a game of rock, paper or scissors 

import ui
import random 

number_to_guess = random.randint(1,3)
print(number_to_guess)

ROCK = 1
PAPER = 2
SCISSORS = 3

def Rock_button_touch_up_inside(sender):
    
    #process
    global number_to_guess
    if ROCK == number_to_guess:
        view['answer_label'].text = "Draw!"
     
    elif PAPER == number_to_guess:
        view['answer_label'].text = "You lost"
     
    else:
        view['answer_label'].text = "You won!"
    
def Paper_button_touch_up_inside(sender):
    
    global number_to_guess
    if number_to_guess == ROCK:
          view['answer_label'].text = "You won!"
     
    elif number_to_guess == PAPER:
          view['answer_label'].text = "Draw!"
     
    else: 
          view['answer_label'].text = "You lost"


def Scissors_button_touch_up_inside(sender):
    
    global number_to_guess
    if number_to_guess == ROCK:
        view['answer_label'].text = "You lost"
     
    elif number_to_guess == SCISSORS:
          view['answer_label'].text = "Draw!"
     
    else: 
          view['answer_label'].text = "You won!" 

view = ui.load_view()
view.present('full_screen')
