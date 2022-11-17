import datetime
from math import atanh
import pygame
import os
import random
import time
from sys import exit
from game import Arena, Player
from graph import SCREEN_ON


pygame.init()

def playGame():
    arena = Arena(9,9)
    clock = pygame.time.Clock()
    players = [Player(0, arena), Player(1, arena), Player(2, arena), Player(3, arena)]
    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
                
        if SCREEN_ON:
            arena.drawn()
            for player in players:
                player.update([1,1,0,0])
                player.drawn()
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
