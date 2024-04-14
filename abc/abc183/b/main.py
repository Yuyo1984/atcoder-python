from sys import stdin
input = stdin.readline

S_x, S_y, G_x, G_y = map(int, input().split())

G_y = -G_y

slope = (G_y - S_y) / (G_x - S_x)

move = -S_y / slope

ans = move + S_x

print(ans)
