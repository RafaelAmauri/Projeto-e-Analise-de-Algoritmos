import sys
import time

from algorithms.brute_force import bruteForce
from algorithms.divide_and_conquer import closest
from algorithms.dc_optimized import closestOptimized
from point.point import Point
from algorithms.utils import point_factory


n = 5


P = [Point(0, 2), Point(6, 67),
     Point(43, 71), Point(39, 107),
     Point(189, 140)]

point_factory(n, "pontos.txt")

if len(sys.argv) >= 2:

    P.clear()

    f = open(sys.argv[1],"r")

    for line in f:

        P.append(Point(int(line.split(' ')[0]),int(line.split(' ')[1])))

    f.close()

    n = len(P)

print("Running Bruteforce...\n")

initialWClock = time.process_time()
print("The smallest distance is",bruteForce(P, n))
clock = time.process_time() - initialWClock
print(f'Tempo: {clock} seconds\n' )

print("Running Divide and Conquer...\n")

initialWClock = time.process_time()
print("The smallest distance is",closest(P, n))
clock = time.process_time() - initialWClock
print(f'Tempo: {clock} seconds\n' )

print("Running Divide and Conquer optimized...\n")

initialWClock = time.process_time()
print("The smallest distance is",closestOptimized(P, n))
clock = time.process_time() - initialWClock
print(f'Tempo: {clock} seconds' )
