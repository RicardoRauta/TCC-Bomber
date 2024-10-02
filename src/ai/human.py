import pygame

class HumanMode():
    arena = None
    weight = None
    active = False

    def __init__(self, active):
        self.active = active

    def get_input(self):
        id = 0
        input = [0,0,0,0, 0]

        if not self.active:
            return input

        userInputArray = pygame.key.get_pressed()

        if userInputArray[pygame.K_UP]:
            input[0] = 1
        if userInputArray[pygame.K_DOWN]:
            input[1] = 1
        if userInputArray[pygame.K_LEFT]:
            input[2] = 1
        if userInputArray[pygame.K_RIGHT]:
            input[3] = 1
        if userInputArray[pygame.K_SPACE]:
            input[4] = 1
        return input
    
    def set_arena(self, arena):
        self.arena = arena