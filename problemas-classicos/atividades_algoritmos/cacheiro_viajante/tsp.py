"""
Function to solve TSP problem
Dynamic Programing

g(i,S) = min_{k e s}{C_ik + g(k, s-{k})}
"""

C = [[0, 23, 17, 19],
     [14, 0, 22, 20],
     [23, 15, 0, 25],
     [13, 19, 21, 0]]

# ts = {0, 1, 2, 3}

path = []


def tsp_rec_solve(d):
    def rec_tsp_solve(c, ts):
        assert c not in ts
        if ts:
            return min((d[lc][c] + rec_tsp_solve(lc, ts - set([lc]))[0], lc) for lc in ts)
        else:
            return (d[0][c], 0)

    path = []
    c = 0
    cs = set(range(1, len(d)))
    while True:
        l, lc = rec_tsp_solve(c, cs)
        if lc == 0:
            break
        path.append(lc)
        c = lc
        cs = cs - set([lc])

    path = tuple(reversed(path))

    return path


# Para cada vertice
a = tsp_rec_solve(C)
print(a)
