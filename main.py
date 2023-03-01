from tkinter import *
import pandas as pd
import random
# setup
BACKGROUND_COLOR = "#B1DDC6"
df = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
finally:
    data_dict = df.to_dict(orient="records")

current_random_card = {}

# functions


def known_word():
    data_dict.remove(current_random_card)
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    get_new_word()


def get_new_word():
    global current_random_card, flip_timer
    window.after_cancel(flip_timer)
    current_random_card = random.choice(data_dict)
    random_word_question = current_random_card['French']
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word_question, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(1000, func=flip_card)


def flip_card():
    random_word_answer = current_random_card['English']
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word_answer, fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ui
window = Tk()
window.title("Flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
flip_timer = window.after(1000, func=flip_card)

canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, fill="black", text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, fill="black", text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=get_new_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=known_word)
known_button.grid(row=1, column=1)

get_new_word()

window.mainloop()
