
# Implementação do algoritmo para resolver
# fibonnaci de forma recursiva, usando programação
# dinâmica, usando a técnica de memoization
def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2: 
        return 1
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]

print(fib(50))