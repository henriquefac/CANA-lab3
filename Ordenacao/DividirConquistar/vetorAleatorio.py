import random as r

def vetorAleatorio():
    vetor = []
    for i in range(10):
        vetor.append(r.randint(1, 20))
    
    return vetor

