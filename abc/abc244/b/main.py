n = int(input())
t = input()

n_p = [0, 0]
direction = ["N", "E", "S", "W"]
x = 1

for turn in t:
    n_d = direction[x]
    if turn == "S":
        if n_d == "N":
            n_p[1] += 1
        elif n_d == "E":
            n_p[0] += 1
        elif n_d == "S":
            n_p[1] -= 1
        elif n_d == "W":
            n_p[0] -= 1
    elif turn == "R":
        x += 1
        x %= 4

print(*n_p)
