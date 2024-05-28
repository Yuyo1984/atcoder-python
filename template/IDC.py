counter = [0] * (100001)
n = int(input())
A = [*map(int, input().split())]
for a in A:
    counter[a] += 1

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    q_t = query[0]
    v = query[1]
    if q_t == 0:
        counter[v] += 1
    elif q_t == 1:
        counter[v] = 0
    elif q_t == 2:
        print(counter[v])
