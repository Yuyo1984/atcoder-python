import more_itertools

s = input()

x = list(more_itertools.run_length.encode(s))

ans = ""

for c in x:
    ans += c[0] + str(c[1])

print(ans)
