h, w, n = map(int, input().split())
q = input()

grid = []
for i in range(h):
    grid.append(input())

ans = 0
for i in range(h):
    for j in range(w):
        I = i
        J = j
        flag = True
        for k in q:
            if k == 'U':
                I -= 1
            elif k == 'D':
                I += 1
            elif k == 'L':
                J -= 1
            else:
                J += 1
            if I < 0 or I > h or J < 0 or J > w:
                flag = False
                break
            if grid[I][J] == '#':
                flag = False
                break
        if flag:
            ans += 1

print(ans)
