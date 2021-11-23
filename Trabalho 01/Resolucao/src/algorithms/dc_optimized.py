import copy
from algorithms.brute_force import bruteForce
from algorithms.utils import dist


"""
Função acha os pontos do array mais proximo
 dado uma distancia 

strip: array de pontos 
 size: tamanho do array 
    d: tamanho desejado
"""
def stripClosest(strip, size, d):

    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
 
    return min_val

"""
Função encontrar a menor distancia entres dados pontos 

"""
def closestUtil(Px, Py, n):
     
    if n <= 3:
        return bruteForce(Px, n)
 
    mid = n // 2
    midPoint = Px[mid]
 
    Pyl = [] 
    Pyr = []
    li = 0

    for i in range(n):
        if( (Py[i].x < midPoint.x) or ((Py[i].x == midPoint.x) and Py[i].y < midPoint.y)) and (li < mid):
            Pyl.append(Py[i])
            li += 1
        
        else:
            Pyr.append(Py[i])
 
    dl = closestUtil(Px, Pyl, mid - 1)
    dr = closestUtil(Px[mid:], Pyr, n - mid)
 

    d = min(dl, dr)
 

    strip = []
    for i in range(n):
        if abs(Py[i].x - midPoint.x) < d:
            strip.append(Py[i])

    return stripClosest(strip, len(strip), d)
 

"""
Função principal (orquestador)

P: array de pontos
n: tamanho do array
"""
def closestOptimized(P, n):
    P.sort(key = lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda point: point.y)

    return closestUtil(P, Q, n)
