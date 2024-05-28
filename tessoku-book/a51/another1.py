from collections import deque
q = int(input())
q_t = []
S = deque()
x = []
for i in range(q):
    query = list(input().split())
    q_t.append(query[0])
    if query[0] == '1':
        x.append(query[1])

for i in range(q):
    if q_t[i] == '1':
        S.append(x[i])
    if q_t[i] == '2':
        ans = S.pop()
        print(ans)
    if q_t[i] == '3':
        S.pop()

