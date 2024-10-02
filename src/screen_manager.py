from src.global_state import GlobalState
from src.game import run, runScore, run_decision_tree

GlobalState.load_main_screen()

def main_menu_screen():
    print("batata")

def game_play_screen():
    run()
    #run_decision_tree()

def exit_game_screen():
    print("batata")

def game_score_screen():
    runScore()