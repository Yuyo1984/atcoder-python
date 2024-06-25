# input
h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
move = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
# solve
for i in range(h):
    for j in range(w):
        for k in range(8):
            n_x = i
            n_y = j
            ansl = []
            ansl.append([n_x + 1, n_y + 1])
            string = ""
            string += s[n_x][n_y]
            for t in range(4):
                n_x += move[k][0]
                n_y += move[k][1]
                if n_x < 0 or n_x >= h or n_y < 0 or n_y >= w:
                    break
                string += s[n_x][n_y]
                ansl.append([n_x + 1, n_y + 1])
                if string == "snuke":
                    for x in range(5):
                        print(ansl[x][0], ansl[x][1])
                    exit()
# output
