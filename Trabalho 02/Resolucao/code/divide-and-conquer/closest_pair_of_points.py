import copy
import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f" x: {self.x}\n y: {self.y}"

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

# Calcula a distancia entre dois ponto
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))

"""
Função para encontrar a menor distancia entre um dado 
grupo de pontos 
strip: pontos a serem avaliados 
size: tamanho do array 
d: distancia incial
"""
def stripClosest(strip, size, d):
     
    min_val = d
    
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
 
    return min_val
 
"""
Ordem o vector o vector de pontos mais proximos do eixo X 
P : array de pontos 
Q : inico do array
n : fim do array 
"""
def closestUtil(P, Q, n):
     

    # Caso a quantidade de pontos seja menor que 3 
    # usa-se o metodo de força bruta 
    if n <= 3:
        return bruteForce(P, n)
 
    # pegar a metade de n
    mid = n // 2
    midPoint = P[mid]
 
    Pl = P[:mid]
    Pr = P[mid:]
 

    dl = closestUtil(Pl, Q, mid)
    dr = closestUtil(Pr, Q, n - mid)
 
  
    # Acha a menor distancia 
    d = min(dl, dr)
 

    stripP = []
    stripQ = []
    lr = Pl + Pr
    for i in range(n):
        if abs(lr[i].x - midPoint.x) < d:
            stripP.append(lr[i])
        if abs(Q[i].x - midPoint.x) < d:
            stripQ.append(Q[i])
 
    stripP.sort(key = lambda point: point.y) #<-- REQUIRED
    min_a = min(d, stripClosest(stripP, len(stripP), d))
    min_b = min(d, stripClosest(stripQ, len(stripQ), d))
     
     

    return min(min_a,min_b)
 


"""
Função principal da "classe"(orquestadora)
"""
def closest(P, n):
    P.sort(key = lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda point: point.y)   
 
 
    return closestUtil(P, Q, n)


n = 5

P = [Point(0, 2), Point(6, 67),
     Point(43, 71), Point(39, 107),
     Point(189, 140)]

print(f'Smallest distance: {closest(P,n)}')