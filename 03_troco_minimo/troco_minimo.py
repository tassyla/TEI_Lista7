# Tássyla Lissa Lima - INF3A - 20192001990
# Referência: https://youtu.be/dYIVEW1CmBk

tb = [-1 for _ in range(1005)]
valores = list(map(int, input().split()))

def dp(k):
    global tb, valores

    if k == 0: return 0
    if tb[k] != -1: return tb[k]
    
    melhor = float('inf')

    for i in range(len(valores)):
        if valores[i] <= k:
            melhor = min(melhor, 1 + dp(k - valores[i]))
    
    tb[k] = melhor

    return tb[k]

while True:
    try:

        k = int(input())
        
        print(f'O troco mínimo para {k} com {valores} utiliza {dp(k)} notas')

    except EOFError:
        break
