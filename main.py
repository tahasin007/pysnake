from tkinter import *
from const import *
from snake import *
from food import *
from event import *


window = Tk()
window.title("Snake game")
window.resizable(False, False)

label = Label(window, text="Score:{}".format(SCORE), font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake(canvas)
food = Food(canvas, snake.coordinates)
game_event = GameEvent(window, canvas, snake, food, label)

window.bind("<Left>", lambda event: game_event.change_direction("left"))
window.bind("<Right>", lambda event: game_event.change_direction("right"))
window.bind("<Up>", lambda event: game_event.change_direction("up"))
window.bind("<Down>", lambda event: game_event.change_direction("down"))
window.bind("<space>", game_event.toggle_pause)

window.mainloop()