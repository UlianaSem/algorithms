def fib_digit(n):
    fib = [i for i in range(n + 1)]
    for i in range(len(fib)):
        if i - 1 == n:
            break
        else:
            if i == 0 or i == 1:
                continue
            else:
                fib[i] = (fib[i - 1] + fib[i - 2]) % 10
    return fib[n]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
