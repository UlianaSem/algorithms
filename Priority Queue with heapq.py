from heapq import heappop, heappush, heapify
from sys import stdin


def insert_number(x, res):
    heappush(res, -1 * (int(x)))    


def extract_max(res):
    element = heappop(res)    
    print(-1 * element)


def get_result(o):
    result = []
    heapify(result)    
    for operation in o:
        if operation[0] == 'Insert':
            insert_number(operation[1], result)
        elif operation[0] == 'ExtractMax':
            extract_max(result)
   

def main():
    n = int(input())
    operations = [[i for i in stdin.readline().split()] for j in range(n)]
    get_result(operations)


if __name__ == '__main__':
    main()
