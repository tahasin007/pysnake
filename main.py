from tkinter import *
from const import *
from snake import *
from food import *


def next_turn(snake, food):
    # check for the paused state
    if PAUSED:
        window.after(SPEED, next_turn, snake, food)
        return
    
    x, y = snake.coordinates[0]

    if DIRECTION == "up":
        y -= SPACE_SIZE
    elif DIRECTION == "down":
        y += SPACE_SIZE
    elif DIRECTION == "left":
        x -= SPACE_SIZE
    elif DIRECTION == "right":
        x += SPACE_SIZE

    # Create the head rectangle separately head color
    head_square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE - PADDING, y + SPACE_SIZE - PADDING, fill=SNAKE_HEAD_COLOR
    )
    snake.squares.insert(0, head_square)

    # Insert new head coordinates at the beginning of the coordinates list
    snake.coordinates.insert(0, (x, y))

    # Change the color of existing rectangles for the rest of the snake
    for i in range(1, len(snake.coordinates)):
        canvas.itemconfig(snake.squares[i], fill=SNAKE_COLOR)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global SCORE
        SCORE += 1
        label.config(text="Score:{}".format(SCORE))
        canvas.delete("food")
        food = Food(canvas, snake.coordinates)
    else:
        # Delete the tail segment and its square
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global DIRECTION, GAME_STARTED

    if not GAME_STARTED:
        GAME_STARTED = True
        next_turn(snake, food)

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


def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    # Check if snake is colliding with its body 
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        font=("consolas", 70),
        text="GAME OVER",
        fill="red",
        tag="gameover",
    )

def toggle_pause(event):
    global PAUSED
    PAUSED = not PAUSED

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

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<space>", toggle_pause)

snake = Snake(canvas)
food = Food(canvas, snake.coordinates)

window.mainloop()
