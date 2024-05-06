# func

# input
s = input()
t = input()

# solve
ansl = []
idx = 0
for i in range(len(t)):
    if t[i] == s[idx]:
        ansl.append(i+1)
        idx += 1
    if idx == len(s):
        break
# answer
print(*ansl)
