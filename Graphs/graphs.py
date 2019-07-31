inf = 1000000


def breathFirst(input, start, searched):
    # u - unvisited
    # v - visited
    # a - analysed
    Q = []
    v = []
    for i in range(len(input)):
        v.append(['u', inf, None])

    v[start][0] = 'v'
    v[start][1] = 0
    v[start][2] = None

    Q.append(start)

    while len(Q) > 0:
        u = Q[0]
        del Q[0]
        for j in range(len(input)):
            if input[u][j] == 1:
                if v[j][0] == 'u':
                    v[j][0] = 'v'
                    v[j][1] = v[u][1] + 1
                    v[j][2] = u
                    Q.append(j)
        v[u][0] = 'a'

    temp = v[searched]
    print(searched, "<-", end='')

    while temp[2] != start:
        print(temp[2], "<-", end='')
        temp = v[temp[2]]

    print(start)