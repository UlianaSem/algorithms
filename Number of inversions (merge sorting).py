from sys import stdin


def merge(a, left, mid, right):
    result = [0 for k in range(right - left)]
    it1 = 0
    it2 = 0
    inverse = 0
    while left + it1 < mid and mid + it2 < right:
        if a[left + it1] > a[mid + it2]:
            result[it1 + it2] = a[mid + it2]
            inverse += mid - left - it1
            it2 += 1
        else:
            result[it1 + it2] = a[left + it1]
            it1 += 1
    while left + it1 < mid:
        result[it1 + it2] = a[left + it1]
        it1 += 1
    while mid + it2 < right:
        result[it1 + it2] = a[mid + it2]
        it2 += 1
    for i in range(it1 + it2):
        a[left + i] = result[i]
    return inverse


def separate(m, n, inverse=0):
    i = 1
    while i < n:
        j = 0
        while j < n - i:
            inverse += merge(m, j, j + i, min(j + 2 * i, n))
            j += 2 * i
        i = 2 * i
    return print(inverse)


number = int(stdin.readline())
massive = list(map(int, input().strip().split()[:number]))
separate(massive, number)
