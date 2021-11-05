# Tássyla Lissa Lima - INF3A - 20192001990
# Referência: https://youtu.be/dYIVEW1CmBk

tb = [-1 for _ in range(1005)]

def fib_dp (n):
    global tb
    
    if n == 0: return 0
    if n == 1: return 1
    if tb[n] != -1: return tb[n]

    tb[n] = fib_dp(n-1) + fib_dp(n-2)
    return tb[n]

while True:
    try: 

        n = int(input())
        print(f'f({n}) = {fib_dp(n)}')

    except EOFError:
        break
