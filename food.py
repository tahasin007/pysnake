import random
from const import *


class Food:
    def __init__(self, canvas, snake_coordinates):
        while True:
            # Generate random coordinates for the food
            x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

            # Check if the food's coordinates collide with the snake's coordinates
            if (x, y) not in snake_coordinates:
                break  # Exit the loop if there's no collision

        self.coordinates = [x, y]

        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food"
        )