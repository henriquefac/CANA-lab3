import math
from vetorAleatorio import vetorAleatorio
def MergeSort(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)

def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = []
    R = []
    for i in range(int(n1)):
        L.append(A[p + i])
    for i in range(int(n2)):
        R.append(A[q + 1 + i])

    i = 0
    j = 0
    for k in range(p, r + 1):
        if i < n1 and (j >= n2 or L[i] >= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


A = vetorAleatorio()
p = 0
r = len(A) - 1
print(A)    

MergeSort(A, p, r)
print(A)
