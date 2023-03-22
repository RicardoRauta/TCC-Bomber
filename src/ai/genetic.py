import random
from src.config import Config

def crossover(state1, state2, mutationRate, mutationRange):
    randPos = random.randint(0, len(state1))
    newState1 = state1[:randPos] + state2[randPos:]
    newState2 = state2[:randPos] + state1[randPos:]
    return [mutation(newState1, mutationRate, mutationRange), mutation(newState2, mutationRate, mutationRange)]

def mutation(state, mutationRate, mutationRange):
    aux = state.copy()
    state_size = len(state)
    for it in range(state_size):
        if random.random() < mutationRate:
            aux[it] = random.randint(-mutationRange/2,mutationRange/2)
    return aux