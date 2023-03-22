import pygame
from src.components.game_status import GameStatus
from src.config import Config

class GlobalState:
    GAME_STATE = GameStatus.MAIN_MENU
    SCREEN = None

    @staticmethod
    def load_main_screen():
        screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        screen.fill((25, 10, 54))
        GlobalState.SCREEN = screen
