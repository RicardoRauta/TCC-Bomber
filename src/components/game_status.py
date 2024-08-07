from enum import Enum


class GameStatus(Enum):
    MAIN_MENU = 0
    GAME_PLAY = 1
    GAME_END = 2
    GAME_SCORE = 3