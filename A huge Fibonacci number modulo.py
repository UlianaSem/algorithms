def fib_mod(n, m):
    fib = [i for i in range(2)]
    i = 2
    while True:
        if fib[i - 1] == 1 and fib[i - 2] == 0 and i != 2:
            break
        else:
            if (fib[i - 1] + fib[i - 2]) >= m:
                fib.append((fib[i - 1] + fib[i - 2]) - m)
            else:
                fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    period_piz = i - 2
    new_fib = fib[:period_piz]
    return new_fib[n % period_piz]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
