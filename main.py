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
    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
                
        if SCREEN_ON:
            arena.drawnArena()
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