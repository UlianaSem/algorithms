from sys import stdin


def count_ladder(n, w):
    # finds the maximum amount that can be obtained
    # by walking up the stairs from the bottom up by climbing one or two steps
    d = [0 for i in range(n + 1)]
    if n == 1:
        return w[0]
    else:
        d[1] = w[0]
        for i in range(2, len(d)):
            d[i] = max([d[i-1] + w[i-1], d[i-2] + w[i-1]])
        return d[n]


# number - number of steps, numbers_on_steps - numbers written on the steps
number = int(stdin.readline())
numbers_on_steps = [int(i) for i in stdin.readline().split()[:number]]
print(count_ladder(number, numbers_on_steps))
