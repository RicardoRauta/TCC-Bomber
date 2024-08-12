import pygame, random, os, datetime, math, multiprocessing

from src.config import Config
from src.components.game_status import GameStatus
from src.components.arena import Arena
from src.components.player import Player
from src.components.scoreboard import Scoreboard
from src.global_state import GlobalState
from src.ai.human import HumanMode
from src.ai.neural import Neural 
from src.ai.decision_tree import DecisionTree 
from src.ai.genetic import crossover

def playGame(input_system):
    arena = Arena(9,9)
    clock = pygame.time.Clock()
    players = []
    id = 0
    for input in input_system:
        players.append(Player(id, arena, input))
        id += 1
    arena.PLAYERS = players
    run = True
    while(run):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
        if arena.END:
            run = False

        if Config.SCREEN_ON:
            arena.drawn()

        dt = clock.tick(Config.FPS)
        #print(clock.get_fps(), dt)

        for player in players:
            player.update(dt)
        
        arena.check_end()
        
        
        if Config.SCREEN_ON:
            pygame.display.update()

    weight = None
    score = 0

    for p in players:
        if isinstance(p.MODE, Neural):
            score = p.SCORE
            weight = players[0].MODE.weight
        elif isinstance(p.MODE, HumanMode):
            score = p.SCORE
    
    return [score, weight]




######################################################################################

def runScore():
    now = datetime.datetime.now()
    
    if not os.path.exists("OutputScore"):
        os.makedirs("OutputScore")

    top_qtd = int(math.sqrt(Config.ARENA_QTD))
    totalScore = 0
    for x in range(10):
        if Config.HUMAN_MODE:
            input_system = [HumanMode(), DecisionTree(), DecisionTree(), DecisionTree()]
            score, _ = playGame(input_system)
        else:
            if Config.LOAD:
                loadFile = open("Output/best.save", "r")
                generation, best_score, neuron = load_best(loadFile, top_qtd)
                loadFile.close()
                input_system = [Neural(neuron[0][1], 1), DecisionTree(), DecisionTree(), DecisionTree()]
                score, _ = playGame(input_system)
        print ("Score " + str(x) + " = " + str(score))
        totalScore += score
    print ("Final Score = " + str(totalScore / 10))
    exit()
            

def run():
    now = datetime.datetime.now()
    
    if not os.path.exists("Output"):
        os.makedirs("Output")

    run = True
    player_result_list = []
    # arena deve ter raiz quadrada inteira
    # top_qtd^2 = 4*ARENA_QTD
    # top_qtd = 2 * sqrt 
    top_qtd = int(math.sqrt(Config.ARENA_QTD))
    best_score = -1000
    timer = pygame.time.get_ticks()

    if Config.HUMAN_MODE:
        input_system = [HumanMode(), HumanMode(), HumanMode(), HumanMode()]
        if Config.LOAD:
            loadFile = open("Output/best.save", "r")
            generation, best_score, neuron = load_best(loadFile, top_qtd)
            loadFile.close()
            input_system = [HumanMode(), Neural(neuron[0][1], 1), Neural(neuron[1][1], 2), Neural(neuron[2][1], 3)]
        
        playGame(input_system)
    else:
        #### Inicializar arquivo de log vazio
        log = "Output/log_{0:%y}_{0:%m}_{0:%d}.txt".format(now)
        logFile = open(log, "w")
        logFile.write("")
        ####

        #### Inicializar tabela de valores
        table = "Output/table_{0:%y}_{0:%m}_{0:%d}.csv".format(now)
        tableFile = open(table, "w")
        tableFile.write("Gen;Time;Best Score;First Place Generation Score;Second Place Generation Score;Third Place Generation Score\n")
        ####
        generation = 0
        if Config.LOAD:
            loadFile = open("Output/best.save", "r")
            generation, best_score, player_result_list = load_best(loadFile, top_qtd)
            loadFile.close()
        pool = multiprocessing.Pool(Config.CPU_CORE)
        player_result_list = []
        while(run):
            #print("Creating generation {0}".format(generation))
            neural_list = create_run_global(player_result_list, top_qtd, pool)

            input_multicore = []
            for neuron in neural_list:
                neuron_player_list = [Neural(neuron[0], 0), DecisionTree(), DecisionTree(), DecisionTree()]
                input_multicore.append(neuron_player_list)

            player_result_list.clear()
            #print("Running generation {0}".format(generation))
            player_result_list = pool.map(playGame, input_multicore)
            error = filter_player_list(player_result_list)
            player_result_list.sort(reverse=True)
            if player_result_list[0][0] > best_score:
                best_score = player_result_list[0][0]
            
            print("Gen {0} COMPLETE - BEST SCORE TOTAL = {2} BEST SCORE GEN {0} = {3} - {1} ERROR".format(generation, error, best_score, player_result_list[0][0]))
            bestFile = open("Output/best.save", "w")
            save_best(generation, best_score, player_result_list[0:top_qtd], bestFile)
            bestFile.close()
            logFile.write("Start generation {0}\n\n".format(generation))
            save_best(generation, best_score, player_result_list[0:top_qtd], logFile)
            logFile.write("\nEnd generation {0}\n\n".format(generation))
            genInfo = "{0};{1};{2};{3};{4};{5}\n".format(generation, pygame.time.get_ticks()-timer, best_score, player_result_list[0][0], player_result_list[1][0], player_result_list[2][0])
            tableFile.write(genInfo)
            
            generation += 1
            
        logFile.close()
        tableFile.close()

def save_best(generation, best_score, list, file):
    file.write(str(generation) + "\n")
    file.write(str(best_score) + "\n")
    for it in range(len(list)):
        file.write(str(list[it][0]) + "\n")
        for value in list[it][1]:
            file.write(str(value) + " ")
        file.write("\n")

def load_best(file, qtd):
    generation = int(file.readline())
    best_score = float(file.readline())
    list = []
    for it in range(qtd):
        score = float(file.readline())
        line = file.readline().split(' ')
        list_aux = []
        for l in line:
            try:
                value = int(l)
                list_aux.append(value)
            except:
                None
        list.append([score, list_aux])
    return generation+1, best_score, list

def filter_player_list(player_list):
    i = 0
    error_qtd = 0
    for p in player_list:
        if p == None:
            error_qtd += 1
            aux_list = []
            for aux in range(Config.WEIGHTS_QTD):
                aux_list.append(random.randint(-500, 500))
            player_list[i] = [-1, aux_list]
        i += 1
    return error_qtd

def create_run(player_list, top_qtd):
    if player_list == []:
        neural_list = []
        for k in range(Config.ARENA_QTD):
            neuron = []
            for j in range(4):
                aux_list = []
                for i in range(Config.WEIGHTS_QTD):
                    aux_list.append(random.randint(-500, 500))
                neuron.append(aux_list)
            neural_list.append(neuron)
        return neural_list
    else:
        neural_list = []
        new_list = []
        i = -1
        for k in range(top_qtd):
            i += 1
            if k == None:
                continue
            neural_list.append(player_list[i][1])
        i = 0
        for aux_list_1 in neural_list:
            for aux_list_2 in neural_list[i:len(neural_list)]:
                if aux_list_1 == aux_list_2:
                    continue
                new_list += crossover(aux_list_1, aux_list_2, 0.01, Config.WEIGHTS_RANGE)
            new_list.append(aux_list_1)
            i += 1
        if len(player_list) < Config.ARENA_QTD:
            for k in range(Config.ARENA_QTD-len(player_list)):
                neuron = []
                for j in range(4):
                    aux_list = []
                    for i in range(Config.WEIGHTS_QTD):
                        aux_list.append(random.randint(-500, 500))
                    new_list.append(aux_list)
        random.shuffle(new_list)
        aux = 0
        neural_final_list = []
        for k in range(Config.ARENA_QTD):
            neuron = []
            for j in range(4):
                neuron.append(new_list[aux])
                aux += 1
            neural_final_list.append(neuron)
        return neural_final_list

def create_run_global(player_list, top_qtd, pool):
    #print("Input list size = " + str(len(player_list)))
    neural_list = []
    input_multicore = []
    if player_list == []:
        for id in range(Config.ARENA_QTD):
            input_multicore.append([id])
    else:
        top_list = []
        for id in range(top_qtd):
            top_list.append(player_list[id][1])
        for id in range(top_qtd-1):
            input_multicore.append([top_list, id])
        #print("Top list size = " + str(len(top_list)))
    if player_list == []:
        neural_list = pool.map(create_random_weights, input_multicore)
    else:
        #print("Input to create list size = " + str(len(input_multicore)))
        result = pool.map(create_run_thread, input_multicore)
        #print("List middle result size = " + str(len(result)))
        for list in result:
            for neuron in list:
                neural_list.append(neuron)
        #print("List neural result added size = " + str(len(neural_list)))
        for id in range(top_qtd):
            neural_list.append(top_list[id])
    #none_values = 0
    #id = 0
    #for neuron in neural_list:
    #    id += 1
    #    if neuron == None:
    #        none_values += 1
    #        print("ERROR ID = {0}".format(id))
    #print("{0} values error".format(none_values))
    #print("Estimative list size = " + str(len(neural_list)))
    random.shuffle(neural_list)
    neural_final_list = []
    aux = 0
    for k in range(Config.ARENA_QTD):
        neuron = []
        for j in range(1):
            neuron.append(neural_list[aux])
            aux += 1
        neural_final_list.append(neuron)
    #print("Output list size = " + str(len(neural_final_list)))
    return neural_final_list

def create_random_weights(id):
    neuron = []
    for i in range(Config.WEIGHTS_QTD):
        neuron.append(random.randint(-500, 500))
    return neuron

def create_run_thread(input):
    top_list, id = input
    if len(top_list) - 1 == id:
        return []
    new_list = []
    for top in top_list[id+1:len(top_list)]:
        new_list += crossover(top_list[id], top, 0.05, Config.WEIGHTS_RANGE)
    #print ("New List size = " + str(len(new_list)) + " from id = " + str(id))
    return new_list