
# Implementação do algoritmo para resolver o problema de 
# fibonnaci a partir de recursão, usando programação
# dinâmica, com a técnica de memoization
def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2: 
        return 1
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]

print(fib(50))