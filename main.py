from tkinter import *
from const import *
from snake import *
from food import *
from event import *
from effect import *
from window import *


if __name__ == "__main__":
    window = Window()
    canvas = window.get_canvas()
    score_label = window.get_score_label()
    status_label = window.get_status_label()
    
    window.get_window().update()

    snake = Snake(canvas)
    food = Food(canvas, snake.coordinates)
    effect = Effect()
    game_event = GameEvent(window.get_window(), canvas, snake, food, score_label, status_label, effect)

    window.get_window().bind("<Left>", lambda event: game_event.change_direction("left"))
    window.get_window().bind("<Right>", lambda event: game_event.change_direction("right"))
    window.get_window().bind("<Up>", lambda event: game_event.change_direction("up"))
    window.get_window().bind("<Down>", lambda event: game_event.change_direction("down"))
    window.get_window().bind("<space>", lambda event: game_event.toggle_pause())

    window.get_window().mainloop()