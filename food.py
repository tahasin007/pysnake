from PIL import Image, ImageTk
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

        # Load the food image
        original_image = Image.open("./asset/apple.png")

        # Resize the image to SPACE_SIZE
        resized_image = original_image.resize((SPACE_SIZE, SPACE_SIZE))

        # Convert the resized image to a format compatible with Tkinter
        self.food_image = ImageTk.PhotoImage(resized_image)

        # Create food item at the specified coordinates
        self.food_item = canvas.create_image(
            x + SPACE_SIZE / 2, y + SPACE_SIZE / 2, image=self.food_image, tag="food"
        )