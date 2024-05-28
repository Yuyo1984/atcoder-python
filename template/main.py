counter = [0 for i in range(5*10**5+1)]
n = int(input())
A = [*map(int, input().split())]
for a in A:
    counter[a] += 1

ans = 0
cnt = 0
for i in counter:
    if counter[i] > cnt :
        ans = i
        cnt = counter[i]

print(ans)
