from algorithms.utils import dist

"""
Algoritmo de Brute Force
Retorna a menor distancia dentre os pontos 
P : array de pontos
n :  tamanho do array
"""

def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
 
    return min_val