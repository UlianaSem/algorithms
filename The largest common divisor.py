def gcd(a, b):
    if a != 0:
        if b != 0:
            if a > b:
                return gcd(a % b, b)
            elif a == b:
                return a
            else:
                return gcd(a, b % a)
        else:
            return a
    else:
        return b
    

def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
