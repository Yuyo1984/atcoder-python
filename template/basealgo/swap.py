def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def main():
    a, b = map(int, input().split())
    a, b = swap(a, b)
    print(a, b)


if __name__ == "__main__":
    main()
