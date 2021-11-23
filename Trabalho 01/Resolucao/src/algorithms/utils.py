import math
import random
# Calcula a distancia entre dois ponto
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))

# Gerador de pontos 
def point_factory(n, file_path):
    points = []
    
    for i in range(n):
        x = random.randint(0, 10000)
        y = random.randint(0, 10000)

        while [x, y] in points:
            x = random.randint(0, 10000)
            y = random.randint(0, 10000)
        
        points.append([x, y])


    with open(file_path, "w") as f:        
        for p in points:
            f.write(f"{p[0]} {p[1]}\n")
    
