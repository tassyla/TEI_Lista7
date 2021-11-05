while True:
    try:

        n, c = map(int, input().split())
        peso = [0] + list(map(int, input().split()))
        valor = [0] + list(map(int, input().split()))

        tb = [[0 for _ in range(101)] for _ in range(101)]

        for i in range(1, n + 1):

            for j in range(1, c + 1):

                if peso[i] <= j:
                    tb[i][j] = max(tb[i-1][j-peso[i]] + valor[i], tb[i-1][j])
                else:
                    tb[i][j] = tb[i-1][j]

        print(tb[n][c])
    except EOFError:
        break
    