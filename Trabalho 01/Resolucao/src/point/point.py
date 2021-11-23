import random 

# Representa pontos no plano 2D
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f" x: {self.x}\n y: {self.y}"
def create_n_points(n):

    points = []

    for i in range(n):

        x = random.randrange(0,10000)
        y = random.randrange(0,10000)

        points.append(Point(x,y))

    return points