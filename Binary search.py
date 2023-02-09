from sys import stdin


def get_index(num, q, *a):
    res = []
    for i in range(q):
        l, r = 0, num
        while l < r:
            m = l + (r - l) // 2
            if b[i] < a[m]:
                r = m
            elif b[i] > a[m]:
                l = m + 1
            else:
                res.append(m + 1)
                break
        if l >= r:
            res.append(-1)
    return print(*res)
    

reader = (map(int, line.split()) for line in stdin)
n, *A = next(reader)
k, *b = next(reader)
get_index(n, k, *A)
