from sys import stdin


def count_k(a, n):
    # finds the length of the maximum subsequence in which each element is divided by the previous one
    d = [1 for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[j] <= a[i] and a[i] % a[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    answer = 0
    for i in range(n):
        answer = max(answer, d[i])
    return answer


number = int(stdin.readline())
number_list = [int(i) for i in stdin.readline().split()[:number]]
print(count_k(number_list, number))
