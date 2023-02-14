'''def fib(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)
        
print (fib(31))'''

def fib(n):
    fib = [i for i in range(41)]
    for i in range(len(fib)):
        if i - 1 == n:
            break
        else:
            if i == 0 or i == 1:
                continue
            else:
                fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]
            
def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()