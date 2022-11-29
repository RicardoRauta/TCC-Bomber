from math import exp
from game import Arena, GameMode

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

    def __init__(self, weight, id):
        self.weight = weight
        self.id = id

    def inputSelector(self, array):
        
        op = self.neuronsOp(array, [121, 60, 4], [sigmoid, degrau]) # Total = 7260+240 = 7500
        
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
        if self.arena != None:
            array.append(self.arena.PLAYERS[self.id].X_ARENA_POS)
            array.append(self.arena.PLAYERS[self.id].Y_ARENA_POS)
        else:
            array.append(0)
            array.append(0)
        if self.clock != None:
            array.append(self.clock.get_time())
        else:
            array.append(0)
            
        for i in self.arena.MATRIX:
            for k in i:
                if k == 'o':
                    array.append(0)
                elif k == '-':
                    array.append(1)
                elif k == '*':
                    array.append(2)
                elif k == '0':
                    array.append(3)
                elif k == 'X':
                    array.append(4)
                else:
                    array.append(5)

        return self.inputSelector(array)