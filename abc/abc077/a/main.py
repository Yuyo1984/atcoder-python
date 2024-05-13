g = [list(input()) for i in range(2)]
if g[0][0] == g[1][2]:
    if g[0][1] == g[1][1]:
        if g[0][2] == g[1][0]:
            print("YES")
            exit()

print("NO")

