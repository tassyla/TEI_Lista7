# Tássyla Lissa Lima - INF3A - 20192001990
# Referência: https://youtu.be/dYIVEW1CmBk

def dp(i):
    global tb, moedas

    if i >= len(moedas): return 0
    if tb[i] != -1: return tb[i]

    tb[i] = max(dp(i+1), dp(i+2) + moedas[i])
    return tb[i]  

while True:
    try:

        tb = [-1 for _ in range(1005)]
        moedas = list(map(int, input().split()))

        print(f'A melhor opção em {moedas} é {dp(0)}')

    except EOFError:
        break
