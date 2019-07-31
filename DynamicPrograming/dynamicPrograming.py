def longestCommonSubsequence(x, y):
    m = len(x)
    n = len(y)
    b = []
    c = []

    for i in range(m + 1):
        b.append([0] * (n + 1))
        c.append([0] * (n + 1))

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 'd'
            else:
                if c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = 'u'
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = 'l'

    print("Longest common substring lenght: ", c[m][n])
    printLCS(b, x, m, n)


def printLCS(b, x, i, j):
    if i == 0 or j == 0:
        return

    if b[i][j] == 'd':
        printLCS(b, x, i - 1, j - 1)
        print(x[i-1], end='')
    else:
        if b[i][j] == 'u':
            printLCS(b, x, i - 1, j)
        else:
            printLCS(b, x, i, j - 1)
