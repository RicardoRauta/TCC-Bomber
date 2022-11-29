

def crossover(state1, state2, childrensQtd, mutationRate):
    childrens = []
    for it in range(childrensQtd):
        randPos = random.randint(0, len(state1))
        newState = state1[:randPos] + state2[randPos:]
        childrens.append(mutation(newState, mutationRate))
    return childrens