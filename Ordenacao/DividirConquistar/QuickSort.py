from vetorAleatorio import vetorAleatorio

def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p ,r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
    pass


def Partition(A, p, r):
    x = A[r]
    i = p-1
    aux = 0
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            aux = A[j]
            A[j] = A[i]
            A[i] = aux 
    aux = A[r]
    A[r] = A[i+1]
    A[i+1] = aux
    return i+1

A = vetorAleatorio()
p=0
r = len(A) -1

print(A)

QuickSort(A, p, r)

print(A)