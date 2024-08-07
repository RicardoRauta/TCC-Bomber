from math import exp
from src.config import Config

def sigmoid(x):
    if x >= 0:
        z = exp(-x)
        sig = 1 / (1 + z)
        return sig
    else:
        z = exp(x)
        sig = z / (1 + z)
        return sig
    
class Neural():
    arena = None
    clock = None
    weight = None
    id = 0

    def __init__(self, weight, id):
        self.weight = weight
        self.id = id

    def inputSelector(self, array):
        
        #print("len array {0} neurons {1}".format(len(array), Config.NEURONS))

        op = self.neuronsOp(array, Config.NEURONS, [sigmoid, sigmoid])
        for i in range(len(op)):
            if (op[i] < 0.5):
                op[i] = 0
            else:
                op[i] = 1
        return op

    def neuronsOp(self, value, neurons, func_list):
        newNeurons = value.copy()
        prevNeurons = []
        position = 0
        for n in range(len(neurons)):
            if n == 0:
                continue
            func = func_list[n-1]
            prevNeurons = newNeurons.copy()
            newNeurons.clear()
            for it in range(neurons[n]):
                sum = 0
                for it2 in range(neurons[n-1]):
                    #print(it, it2, position, Config.WEIGHTS_QTD, neurons, n, len(self.weight), len(value))
                    sum += prevNeurons[it2] * self.weight[position]
                    position += 1
                newNeurons.append(func(sum))
        return newNeurons

    def updateWeight(self, weight):
        self.weight = weight

    def get_input(self):
        array = []
        if self.clock != None:
            array.append(self.clock.get_time())
        else:
            array.append(0)
            
        if Config.SENSOR_TOTAL:
            array += self.getTotaVisionlArena()   # len(array) = 81 * 8 + 9
        else:
            array += self.getLimitedVisionArena() # len(array) = 45 * 8 + 9 ## 45 * 4 + 10
        
        #print ("{0} {1} {2} {3} - ID {4}".format(len(array), len(array)/2, 4, len(array)*(len(array)/2)+(len(array)/2)*4, self.id))
        return self.inputSelector(array)

    def getTotaVisionlArena(self):
        array = []
         # Primeiro coloca o ID do jogador, 0-3
        array.append(self.id)
        # Coloca as posições de cada jogador
        if self.arena != None:
            for player in self.arena.PLAYERS:
                array.append(player.X_ARENA_POS)
                array.append(player.Y_ARENA_POS)
        else:
            for i in range(4*2):
                array.append(0)
        # Coloca cada objeto da arena
        for k in self.arena.MATRIX:
            array += self.sensorValues(k)
        return array

    def getLimitedVisionArena(self):
        array = []
        # Primeiro coloca o ID do jogador, 0-3
        array.append(self.id)
        # Coloca as posições de cada jogador
        if self.arena != None:
            for player in self.arena.PLAYERS:
                array.append(player.X_ARENA_POS)
                array.append(player.Y_ARENA_POS)
        else:
            for i in range(4*2):
                array.append(0)
        # Coloca o tempo de jogo
        array.append(self.arena.arena_time())

        player = self.arena.PLAYERS[self.id]

        y_player = (int) (player.Y_ARENA_POS) - 1
        x_player = (int) (player.X_ARENA_POS) - 1

        if x_player == 0 : x_player = 1
        if x_player == self.arena.WIDTH - 1 : x_player = self.arena.WIDTH - 2
        if y_player == 0 : y_player = 1
        if y_player == self.arena.HEIGHT - 1 : y_player = self.arena.HEIGHT - 2

        for x in range(3):
            auxX = x_player - 1 + x
            for y in range(self.arena.HEIGHT):
                array += self.sensorValues(self.arena.getObjectInPosition(auxX, y))
        for x in range(self.arena.WIDTH):
            if not(x == x_player - 1 or x == x_player or x == x_player + 1):
                for y in range(3):
                    auxY = y_player - 1 + y
                    array += self.sensorValues(self.arena.getObjectInPosition(x, auxY))
        #print(len(array), x_player, y_player)
        return array

    def sensorValues(self, obj):
        array = [0,0,0,0]#,0,0,0,0]
        if obj == None or obj == Config.ARENA_WALL:      # Verifica se tem bloco indestrutivel ou vazio
            array[0] = 1
        elif obj == Config.ARENA_VOID:      # Verifica se tem espaço vazio
            array[1] = 1
        #elif obj == Config.ARENA_BLOCK:      # Verifica se tem bloco quebravel
        #    array[2] = 1
        elif obj == Config.ARENA_BOMB:      # Verifica se tem bomba
            array[2] = 1
        elif obj == Config.ARENA_EXPLOSION:      # Verifica se tem explosão
            array[3] = 1
        #elif obj == Config.ARENA_UPGRADE_BOMB:      # Verifica se tem item bomba
        #    array[5] = 1
        #elif obj == Config.ARENA_UPGRADE_POWER:      # Verifica se tem item fogo
        #    array[6] = 1
        #elif obj == Config.ARENA_UPGRADE_SPEED:      # Verifica se tem item velocidade
        #    array[7] = 1
        return array