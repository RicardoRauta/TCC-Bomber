import pygame

class HumanMode():
    arena = None
    weight = None

    def get_input(self):
        input = [0,0,0,0]
        userInputArray = pygame.key.get_pressed()

        if userInputArray[pygame.K_UP]:
            input = [1,1,1,0]
        elif userInputArray[pygame.K_DOWN]:
            input = [1,1,0,0]
        elif userInputArray[pygame.K_LEFT]:
            input = [1,0,0,0]
        elif userInputArray[pygame.K_RIGHT]:
            input = [1,0,1,0]
        if userInputArray[pygame.K_SPACE]:
            input[3] = 1
        return input
    
    def set_arena(self, arena):
        self.arena = arena