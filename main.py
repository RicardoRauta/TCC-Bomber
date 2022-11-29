import datetime
from math import atanh
import pygame
import os
import random
import time
from sys import exit
from game import Arena, Player
from graph import SCREEN_ON

GAME_MODE = "HUMAN_MODE"


pygame.init()

def playGame():
    PLAYER_ID = 0
    arena = Arena(9,9)
    clock = pygame.time.Clock()
    players = [Player(0, arena), Player(1, arena), Player(2, arena), Player(3, arena)]
    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()

        input = [0,0,0,0]

        if GAME_MODE == "HUMAN_MODE":
            userInputArray = pygame.key.get_pressed()

            if userInputArray[pygame.K_UP]:
                input = [1,1,1,0]
            elif userInputArray[pygame.K_DOWN]:
                input = [1,1,0,0]
            elif userInputArray[pygame.K_LEFT]:
                input = [1,0,0,0]
            elif userInputArray[pygame.K_RIGHT]:
                input = [1,0,1,0]
            elif userInputArray[pygame.K_0]:
                PLAYER_ID = 0
            elif userInputArray[pygame.K_1]:
                PLAYER_ID = 1
            elif userInputArray[pygame.K_2]:
                PLAYER_ID = 2
            elif userInputArray[pygame.K_3]:
                PLAYER_ID = 3
            if userInputArray[pygame.K_SPACE]:
                input[3] = 1
        

        if SCREEN_ON:
            arena.drawn()
            
            for player in players:
                if player.ID == PLAYER_ID:
                    player.update(input)
                else:
                    player.update([0,0,0,0])
           
            clock.tick(60)
            pygame.display.update()

def run():
    now = datetime.datetime.now()
    
    if not os.path.exists("Output"):
        os.makedirs("Output")

    #### Inicializar arquivo de log vazio
    f = open("Output/log_{0:%y}_{0:%m}_{0:%d}_{0:%H}_{0:%M}.txt".format(now), "w")
    f.write("")
    f.close()
    ####

    #### Inicializar tabela de valores
    f = open("Output/table_{0:%y}_{0:%m}_{0:%d}_{0:%H}_{0:%M}.csv".format(now), "w")
    f.write("Gen;Time;Best Score;First Place Generation;Second Place Generation;Third Place Generation\n")
    f.close()
    ####

#run()

playGame()

#  Arena:
#[['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 
# ['o', '-', '-', '*', '*', '*', '*', '*', '-', '-', 'o'], 
# ['o', '-', 'o', '*', 'o', '*', 'o', '*', 'o', '-', 'o'], 
# ['o', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'o'], 
# ['o', '*', 'o', '*', 'o', '*', 'o', '*', 'o', '*', 'o'], 
# ['o', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'o'], 
# ['o', '*', 'o', '*', 'o', '*', 'o', '*', 'o', '*', 'o'],
# ['o', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'o'], 
# ['o', '-', 'o', '*', 'o', '*', 'o', '*', 'o', '-', 'o'], 
# ['o', '-', '-', '*', '*', '*', '*', '*', '-', '-', 'o'], 
# ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']]
