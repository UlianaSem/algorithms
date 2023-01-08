from sys import stdin
import bisect as b
from random import choice


def partition(mas, left, right):
    t = choice(mas[left:right+1])
    m = left
    for i in range(left, right+1):
        if mas[i] < t:
            mas[i], mas[m] = mas[m], mas[i]
            m += 1
    n = m
    for j in range(m, right+1):
        if mas[j] == t:
            mas[j], mas[n] = mas[n], mas[j]
            n += 1    
    return m, n
    

def quicksort(mas, left, right):
    if left < right:
        lt, gt = partition(mas, left, right)
        quicksort(mas, left, lt)
        quicksort(mas, gt, right)
    return mas


# n - number of segments, m - number of points on a straight line, lines - coordinates of the ends of the segments
# coordinates - coordinates of points
n, m = map(int, stdin.readline().split())
lines = [[int(i) for i in stdin.readline().split()] for j in range(n)]
coordinates = list(map(int, stdin.readline().split()[:m]))
begin = [lines[j][0] for j in range(len(lines))]
end = [lines[j][1] for j in range(len(lines))]
quicksort(begin, 0, n - 1)
quicksort(end, 0, n - 1)
print(*[b.bisect(begin, p) - b.bisect_left(end, p) for p in coordinates])
