N = int(input())
p = [*map(int, input().split())]

q = p[:]
q.sort()

if p == q:
    print("YES")
    exit()
for i in range(len(p)):
    for j in range(i+1, len(p)):
        x = p[:]
        x[i], x[j] = x[j], x[i]
        if x == q:
            print("YES")
            exit()

print("NO")
