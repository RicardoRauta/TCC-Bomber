import datetime
from math import atanh
import pygame
import os
import random
import time
from sys import exit
from game import Arena, Player, HumanMode
from neural import Neural
from genetic import crossover
from graph import SCREEN_ON
import numpy as np
from threading import Thread

GAME_MODE = "HUMAN_MODE"

pygame.init()

def playGame(modes):
    arena = Arena(9,9)
    clock = pygame.time.Clock()
    for mode in modes:
        if isinstance(mode, Neural):
            mode.arena = arena
            mode.clock = clock
    players = [Player(0, arena, modes[0]), Player(1, arena, modes[1]), Player(2, arena, modes[2]), Player(3, arena, modes[3])]
    arena.PLAYERS = players
    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
        if arena.END:
            run = False
            for p in players:
                if not p.death:
                    return p

        if SCREEN_ON:
            arena.drawn()

        for player in players:
            player.update()
        
        arena.check_end()
           
        if SCREEN_ON:
            clock.tick(60)
            pygame.display.update()
        
        #if clock.get_time() > 10:
        #    return

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
    run = True
    player_list = []
    thread_list = []

    while(run):
        neural_list = create_run(player_list)
        player_list.clear()
        thread_list.clear()
        i = 0
        for neuron in neural_list:
            i += 1
            t = Thread(target=playGame, args=[[Neural(neuron[0], 0), Neural(neuron[1], 1), Neural(neuron[2], 2), Neural(neuron[3], 3)]])
            thread_list.append(t)
            t.start()
            print(i)
            for thread in thread_list:
                thread.join()
            print("end " + str(i))
        

def create_run(player_list):
    if player_list == []:
        neural_list = []
        for k in range(50):
            neuron = []
            for j in range(4):
                aux_list = []
                for i in range(7502):
                    aux_list.append(random.randint(-500, 500))
                neuron.append(aux_list)
            neural_list.append(neuron)
        return neural_list
    else:
        neural_list = []
        new_list = []
        for p in player_list:
            neural_list.append(p.MODE.weight)
        i = 0
        for aux_list_1 in neural_list:
            for aux_list_2 in neural_list[i:len(neural_list)]:
                if aux_list_1 == aux_list_2:
                    continue
                new_list += crossover(aux_list_1, aux_list_2, 0.1)
            i += 1
        print("LISTA:")
        print(len(new_list))
        #todo: second+ generation

run()



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
