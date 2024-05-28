def move(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        


def operation(c):
    x = c[0]
    y = c[1]
    flag = c[2]
    if terminal[x][y] != -1 and flag == False:
        flag = True
    elif terminal[x][y] != -1 and flag == True:
         if terminal[x][y] 

N = int(input())
terminal = [[-1 for _ in range(N)] for _ in range(N)]

c = {}
c["c1"] = [0, 0, False]
c["c2"] = [1, 0, False]
c["c3"] = [2, 0, False]
c["c4"] = [3, 0, False]
c["c5"] = [4, 0, False]
a1 = ''
a2 = ''
a3 = ''
a4 = ''
a5 = ''
containers = []
for i in range(N):
    containers.append(list(map(int, input().split())))

while True:
    for i in range(N):
        terminal[i][0] = containers[i][0]
        containers.remove([i][0])
    
    operation(c1)
    operation(c2)
    
