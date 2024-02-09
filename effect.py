import pygame


class Effect:
    def __init__(self):
        pygame.init()
        self.eat_sound = pygame.mixer.Sound("./asset/eat.wav")
        self.collision_sound = pygame.mixer.Sound("./asset/collision.wav")
        
    def play_eat_effect(self):
        # Play the sound effect
        self.eat_sound.play()
        
    def play_collision_effect(self):
        # Play the sound effect
        self.collision_sound.play()