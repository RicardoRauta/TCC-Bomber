from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

from src.components.game_status import GameStatus
from src.config import Config
from src.screen_manager import main_menu_screen, game_play_screen, exit_game_screen, game_score_screen
from src.global_state import GlobalState

pygame.init()

FramePerSec = pygame.time.Clock()


def update_game_display():
    pygame.display.update()
    FramePerSec.tick(Config.FPS)


def main():
    while True:
        if GlobalState.GAME_STATE == GameStatus.MAIN_MENU:
            main_menu_screen()
        elif GlobalState.GAME_STATE == GameStatus.GAME_PLAY:
            game_play_screen()
        elif GlobalState.GAME_STATE == GameStatus.GAME_END:
            exit_game_screen()
        elif GlobalState.GAME_STATE == GameStatus.GAME_SCORE:
            game_score_screen()

        update_game_display()


if __name__ == "__main__":
    GlobalState.GAME_STATE = GameStatus.GAME_PLAY
    #GlobalState.GAME_STATE = GameStatus.GAME_SCORE
    main()