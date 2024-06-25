# 偶奇性に着目
# 言われている通り、a*n個、b*n個の文字列を連結
# (i + j) % 2 == 0で白、1なら黒

n, a, b = map(int, input().split())
ans = []

for i in range(n):
    for ai in range(a):
        line = []
        for j in range(n):
            for bj in range(b):
                if (i + j) % 2 == 0:
                    line.append(".")
                else:
                    line.append("#")
        ans.append(line)

for x in ans:
    print("".join(x))
