import random
from const import *


class Snake:
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Head position 
        head_x = random.randint(2, (GAME_WIDTH / SPACE_SIZE) - 2) * SPACE_SIZE
        head_y = random.randint(2, (GAME_HEIGHT / SPACE_SIZE) - 2) * SPACE_SIZE

        # Generate initial coordinates for the snake body relative to the head
        for i in range(BODY_PARTS):
            self.coordinates.append([head_x - (i * SPACE_SIZE), head_y])

        # Create rectangles for each body segment
        for i, coordinate in enumerate(self.coordinates):
            x = coordinate[0]
            y = coordinate[1]
            if i == 0:
                fill_color = SNAKE_HEAD_COLOR
            else:
                fill_color = SNAKE_COLOR
                
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=fill_color, tag="snake"
            )
            self.squares.append(square)