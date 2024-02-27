N, K = map(int, input().split())
A = [*map(int, input().split())]
num = 1
li = [1]
checklist = [True] * N
checklist[0] = False
for i in range(K):
    num = A[num-1]
    if checklist[num-1]:
        li.append(num)
        checklist[num-1] = False
    else:
        break

d = li.index(num)
ans = (K - d) % (len(li) - d) + d
print(li[ans])

