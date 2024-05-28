r, c = map(int, input().split())

if max(abs(r - 8), abs(c - 8)) % 2:
    print("black")
else:
    print("white")
