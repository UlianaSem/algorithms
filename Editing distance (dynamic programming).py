from sys import stdin


def diff(a, b):
    # finds the cost of replacing a character
    if a == b:
        return 0
    else:
        return 1


def edit_dist(str_1, str_2):
    # finds the editing distance
    d = [[0 for i in range(len(str_1) + 1)] for j in range(len(str_2) + 1)]
    for i in range(len(d[0])):
        d[0][i] = i
    for j in range(len(d)):
        d[j][0] = j
    for j in range(1, len(d)):
        for i in range(1, len(d[j])):
            c = diff(str_1[i-1], str_2[j-1])
            d[j][i] = min([d[j-1][i] + 1, d[j][i-1] + 1, d[j-1][i-1] + c])
    return d[len(str_2)][len(str_1)]


# string_1 and string_2 - not empty strings
string_1 = str(stdin.readline())
string_2 = str(stdin.readline())
print(edit_dist(string_1, string_2))
