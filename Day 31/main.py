from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ------------------------------- CREATE FLASH CARDS -------------------------------#
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French", fill='black',)
    canvas.itemconfig(translated_text, text=current_card["French"], fill='black',)
    canvas.itemconfig(canvas_background, image=card_front_photo)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_background, image=card_back_photo)
    canvas.itemconfig(language_text, text='English', fill='white', font=('arial', 25, 'italic'))
    canvas.itemconfig(translated_text, text=current_card["English"], fill='white', font=('arial', 40, 'bold'))


def is_know():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)


    next_card()


# ----------------------------------- UI SET UP -----------------------------------#

window = Tk()
window.title('Flash Cards')
window.config(padx=200, pady=100, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_photo = PhotoImage(file='./images/card_back.png')
card_front_photo = PhotoImage(file='./images/card_front.png')
canvas_background = canvas.create_image(400, 263, image=card_back_photo)
language_text = canvas.create_text(400, 163, text='', fill='white', font=('arial', 25, 'italic'))
translated_text = canvas.create_text(400, 263, text="", fill='white', font=('arial', 40, 'bold'))
canvas.grid(column=0, row=0, columnspan=3)

# Buttons
right_photo = PhotoImage(file='./images/right.png')
right_button = Button(image=right_photo, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right_button.grid(column=2, row=2)

wrong_photo = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_photo, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_know)
wrong_button.grid(column=0, row=2)


next_card()


window.mainloop()
