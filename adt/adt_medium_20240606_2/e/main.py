# input
K = int(input())
# solve
K = format(K, "b")
# output
ans = ""
for i in range(len(K)):
    ans += str(int(K[i]) * 2)

print(ans)
