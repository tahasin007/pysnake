from const import *
from food import *
from tkinter import *


class GameEvent:
    def __init__(self, window, canvas, snake, food, score_label, status_label, effect):
        self.window = window
        self.canvas = canvas
        self.snake = snake
        self.food = food
        self.score_label = score_label
        self.status_label = status_label
        self.effect = effect
        self.play_icon = PhotoImage(file="./asset/play.png").subsample(4)
        self.pause_icon = PhotoImage(file="./asset/pause.png").subsample(4)

    def next_turn(self):
        # check for the paused state
        if PAUSED:
            self.window.after(SPEED, self.next_turn)
            return
        
        x, y = self.snake.coordinates[0]

        if DIRECTION == "up":
            y -= SPACE_SIZE
        elif DIRECTION == "down":
            y += SPACE_SIZE
        elif DIRECTION == "left":
            x -= SPACE_SIZE
        elif DIRECTION == "right":
            x += SPACE_SIZE

        # Create the head rectangle separately with head color
        head_square = self.canvas.create_rectangle(
            x, y, x + SPACE_SIZE - PADDING, y + SPACE_SIZE - PADDING, fill=SNAKE_HEAD_COLOR
        )
        self.snake.squares.insert(0, head_square)

        # Insert new head coordinates at the beginning of the coordinates list
        self.snake.coordinates.insert(0, (x, y))

        # Change the color of existing rectangles for the rest of the snake
        for i in range(1, len(self.snake.coordinates)):
            self.canvas.itemconfig(self.snake.squares[i], fill=SNAKE_COLOR)

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            global SCORE
            SCORE += 1
            self.effect.play_eat_effect()
            self.score_label.config(text="Score:{}".format(SCORE))
            self.canvas.delete("food")
            self.food = Food(self.canvas, self.snake.coordinates)
        else:
            # Delete the tail segment and its square
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_collisions():
            self.game_over()
        else:
            self.window.after(SPEED, self.next_turn)

    def change_direction(self, new_direction):
        global DIRECTION, GAME_STARTED

        if not GAME_STARTED:
            GAME_STARTED = True
            self.next_turn()

        if new_direction == "left":
            if DIRECTION != "right":
                DIRECTION = new_direction
        elif new_direction == "right":
            if DIRECTION != "left":
                DIRECTION = new_direction
        elif new_direction == "up":
            if DIRECTION != "down":
                DIRECTION = new_direction
        elif new_direction == "down":
            if DIRECTION != "up":
                DIRECTION = new_direction

    def check_collisions(self):
        x, y = self.snake.coordinates[0]

        if x < 0 or x >= GAME_WIDTH:
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            return True

        # Check if snake is colliding with its body 
        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over(self):
        self.effect.play_collision_effect()
        self.canvas.delete(ALL)
        self.canvas.create_text(
            self.canvas.winfo_width() / 2,
            self.canvas.winfo_height() / 2,
            font=("consolas", 70),
            text="GAME OVER",
            fill="red",
            tag="gameover",
        )

    def toggle_pause(self, event):
        global PAUSED
        PAUSED = not PAUSED
        
        if PAUSED:
            self.status_label.config(image=self.pause_icon)
        else:
            self.status_label.config(image=self.play_icon)
