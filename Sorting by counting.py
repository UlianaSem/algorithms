from sys import stdin


def count_sort(n_l, n):
    # returns an ascending sorted list
    k = 11
    b = [0 for j in range(n)]
    c = [0 for i in range(k)]
    for i in range(n):
        c[n_l[i]] = c[n_l[i]] + 1
    for j in range(1, k):
        c[j] = c[j] + c[j - 1]
    for h in range(n-1, -1, -1):
        c[n_l[h]] = c[n_l[h]] - 1
        b[c[n_l[h]]] = n_l[h]
    return b


# number - number of numbers, number_list - numbers not exceeding 10 modulo
number = int(stdin.readline())
number_list = [int(i) for i in stdin.readline().split()[:number]]
print(*count_sort(number_list, number))
