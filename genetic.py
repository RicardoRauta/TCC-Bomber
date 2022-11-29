import random

def crossover(state1, state2, mutationRate):
    childrens = []
    randPos = random.randint(0, len(state1))
    newState1 = state1[:randPos] + state2[randPos:]
    newState2 = state2[:randPos] + state1[randPos:]
    return [mutation(newState1, mutationRate), mutation(newState2, mutationRate)]

def mutation(state, mutationRate):
    aux = state.copy()
    state_size = len(state)
    for it in range(state_size):
        if random.random() < mutationRate:
            aux[it] = random.randint(-500,500)
    return aux