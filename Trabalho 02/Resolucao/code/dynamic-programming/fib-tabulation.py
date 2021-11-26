
# Implementação do algoritmo para resolver o problema de 
# fibonnaci a partir de recursão, usando programação
# dinâmica, com a técnica de tabulation
def fib(n):
    table = [0 for i in range(n+1)]
    table[1] = 1
    
    for i in range(n-1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]

    return table[n-1] + table[n-2]

print(fib(50))