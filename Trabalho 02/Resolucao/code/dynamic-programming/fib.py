
# Implementacao ingenua de um
# algoritmo para resolver fibonnaci
# de forma recursiva
def fib(n):
    if n <= 2: 
        return 1

    return (fib(n-1) + fib(n-2))

print(fib(50))
