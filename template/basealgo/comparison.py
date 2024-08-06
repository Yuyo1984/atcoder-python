def Mymax(a, b):
    if a > b:
        return a
    else:
        return b


def Mymin(a, b):
    if a < b:
        return a
    else:
        return b


def main():
    a, b = map(int, input().split())
    print(Mymax(a, b))
    print(Mymin(a, b))


if __name__ == "__main__":
    main()
