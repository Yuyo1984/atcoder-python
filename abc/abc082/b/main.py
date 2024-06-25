s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
s_d = "".join(s)
t_d = "".join(t)

if s_d < t_d:
    print("Yes")
else:
    print("No")
