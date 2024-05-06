import copy

h, w, k = map(int, input().split())
grid = []
for i in range(h):
    x = list(input())
    grid.append(x)

ans = 0
for h_bit in range(2 ** h):
    for w_bit in range(2 ** w):
        cnt = 0
        for i in range(h):
            for j in range(w):
                if (h_bit & 1 << i) != 0 and (w_bit & 1 << j) != 0:
                    if grid[i][j] == '#':
                        cnt += 1
        if cnt == k:
            ans += 1

print(ans)

