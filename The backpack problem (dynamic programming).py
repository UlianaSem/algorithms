from sys import stdin


def backpack_capacity(v, n, w):
    # finds the maximum weight in the backpack
    d = [[0 for ww in range(v + 1)] for i in range(n + 1)]
    for i in range(1, len(d)):
        for ww in range(1, len(d[i])):
            d[i][ww] = d[i-1][ww]
            if w[i-1] <= ww:
                d[i][ww] = max([d[i][ww], d[i-1][ww-w[i-1]] + w[i-1]])
    return d[n][v]


# volume - backpack volume, number - number of items, weight - weight of items
volume, number = map(int, stdin.readline().split())
weight = [int(i) for i in stdin.readline().split()[:number]]
print(backpack_capacity(volume, number, weight))
