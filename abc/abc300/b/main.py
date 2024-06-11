h, w = map(int, input().split())
A = [list(input()) for i in range(h)]
B = [list(input()) for i in range(h)]

new_map = []
for i in range(1, h + 1):
    for j in range(1, w + 1):
        new_map = [["." for i in range(w)] for j in range(h)]
        for k in range(0, h):
            for l in range(0, w):
                H = (k - i) % h
                W = (l - j) % w
                new_map[H][W] = A[k][l]
        if new_map == B:
            print("Yes")
            exit()
print("No")
