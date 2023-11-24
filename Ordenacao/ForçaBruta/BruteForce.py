#Gerar vetor
from vetorAleatorio import vetorAleatorio

vetor = vetorAleatorio()

print(vetor)
aux = 0
for i in range(len(vetor)):
    for j in range(len(vetor)):
        if vetor[i] > vetor[j]:
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux
            print(vetor)
