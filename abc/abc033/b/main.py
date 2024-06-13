N = int(input())
c_n = []
c_p = []
cnt_p = 0
for i in range(N):
    s, p = input().split()
    c_n.append(s)
    c_p.append(int(p))
    cnt_p += int(p)

cnt_p //= 2
for n in range(N):
    if c_p[n] > cnt_p:
        print(c_n[n])
        exit()
print("atcoder")
