import pygame


class Effect:
    def __init__(self):
        pygame.init()
        self.eat_sound = pygame.mixer.Sound("./asset/eat.wav")
        
    def play_eat_effect(self):
        # Play the sound effect
        self.eat_sound.play()