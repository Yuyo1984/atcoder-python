from collections import deque
# func

# input
N = int(input())
A = [*map(int, input().split())]
# solve
balls = deque()
for i in range(N):
    balls.append(A[i])
    if len(balls) <= 1:
        continue
    if balls[-1] != balls[-2]:
        continue
    while balls[-1] == balls[-2]:
        x = balls.pop()
        y = balls.pop()
        z = x + 1
        balls.append(z)
        if len(balls) <= 1:
            break
        if balls[-1] != balls[-2]:
            break
    
# answer
print(len(balls))
