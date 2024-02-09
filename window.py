from tkinter import *
from const import *
from snake import Snake
from food import Food
from event import GameEvent
from effect import Effect

class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Snake game")
        self.window.resizable(False, False)
        self.window.configure(bg="black")

        self.top_frame = Frame(self.window, bg="black")
        self.top_frame.pack(side="top", fill="x")

        self.canvas = Canvas(
            self.window,
            bg=BACKGROUND_COLOR,
            height=GAME_HEIGHT,
            width=GAME_WIDTH,
            highlightthickness=3,
            highlightbackground="white",
        )
        self.canvas.pack()

        self.score_label = Label(self.top_frame, text="Score: 0", fg="white", bg="black", font=("Arial", 15))
        self.score_label.pack(side="right", padx=10, pady=5)

        # Create label for play/pause status
        self.play_icon = PhotoImage(file="./asset/pause.png")
        self.play_icon = self.play_icon.subsample(4) # Resize the icon to 1/4 of its original size
        self.status_label = Label(self.top_frame, image=self.play_icon, bg="black")
        self.status_label.pack(side="left", padx=10, pady=5)

    def get_window(self):
        return self.window

    def get_canvas(self):
        return self.canvas

    def get_score_label(self):
        return self.score_label

    def get_status_label(self):
        return self.status_label