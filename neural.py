from math import exp
from game import Arena, GameMode
from config import NEURONS

def sigmoid(x):
    if x >= 0:
        z = exp(-x)
        sig = 1 / (1 + z)
        return sig
    else:
        z = exp(x)
        sig = z / (1 + z)
        return sig
def degrau(x):
    if x > 0:
        return 1
    return 0

class Neural(GameMode):
    arena = None
    clock = None
    weight = None

    def __init__(self, weight, id):
        self.weight = weight
        self.id = id

    def inputSelector(self, array):
        
        op = self.neuronsOp(array, NEURONS, [sigmoid, degrau]) # Total = 7260+240 = 7500
        
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
                    sum += prevNeurons[it2] * self.weight[position]
                    position += 1
                newNeurons.append(func(sum))
        return newNeurons

    def updateWeight(self, weight):
        self.weight = weight

    def get_input(self):
        array = []
        # Primeiro coloca o ID do jogador, 0-3
        array.append(self.id)
        if self.arena != None:
            # Coloca as posições de cada jogador
            for player in self.arena.PLAYERS:
                array.append(player.X_ARENA_POS)
                array.append(player.Y_ARENA_POS)
        else:
            for i in range(4*2):
                array.append(0)
        if self.clock != None:
            array.append(self.clock.get_time())
        else:
            array.append(0)
            
        for i in self.arena.MATRIX:
            # Coloca cada objeto da arena
            for k in i:
                if k == 'o':      # Verifica se tem bloco indestrutivel
                    array.append(1)
                else:
                    array.append(0)
                if k == '-':      # Verifica se tem espaço vazio
                    array.append(1)
                else:
                    array.append(0)
                if k == '*':      # Verifica se tem bloco quebravel
                    array.append(1)
                else:
                    array.append(0)
                if k == '0':      # Verifica se tem bomba
                    array.append(1)
                else:
                    array.append(0)
                if k == 'X':      # Verifica se tem explosão
                    array.append(1)
                else:
                    array.append(0)
                if k == 'b':      # Verifica se tem item bomba
                    array.append(1)
                else:
                    array.append(0)
                if k == 'p':      # Verifica se tem item fogo
                    array.append(1)
                else:
                    array.append(0)
                if k == 's':      # Verifica se tem item velocidade
                    array.append(1)
                else:
                    array.append(0)
        #print ("{0} {1} {2} {3}".format(len(array), len(array)/2, 4, len(array)*(len(array)/2)+(len(array)/2)*4))
        return self.inputSelector(array)