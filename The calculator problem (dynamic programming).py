from sys import stdin


def calculate(n):
    # finds the minimum number of operations required to get n out of 1. If operations x3, x2, +1 are available
    d = [0 for i in range(n+1)]
    val = []
    for i in range(2, n+1):
        minus = i - 1
        if i % 2 == 0:
            del_2 = int(i / 2)
        else:
            del_2 = minus
        if i % 3 == 0:
            del_3 = int(i / 3)
        else:
            del_3 = minus
        d[i] = min([d[minus], d[del_2], d[del_3]]) + 1
    print(d[n])
    k = d[n]
    h = n
    for i in range(n, 0, -1):
        if (d[i] == k and i == h or d[i] == k and i == h - 1 or d[i] == k and i == int(h / 2) and h % 2 == 0
                or d[i] == k and i == int(h / 3) and h % 3 == 0):
            val.append(i)
            k -= 1
            h = i
    val.reverse()
    print(*val)
        
            
number = int(stdin.readline())
calculate(number)
