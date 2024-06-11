# input
N = int(input())
ans_set = set()
# solve
for i in range(N):
    s = input()
    if s not in ans_set and s[::-1] not in ans_set:
        ans_set.add(s)
# output
print(len(ans_set))
