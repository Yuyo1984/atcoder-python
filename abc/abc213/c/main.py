from sys import stdin
input = stdin.readline

def compress(original):
    S = sorted(list(set(original)))
    rank = {x:i+1 for i, x in enumerate(S)}
    compressed = []
    for tmp in original:
        compressed.append(rank[tmp])
    return compressed

H, W, N = map(int, input().split())
h_list, w_list = [], []
for i in range(N):
    a, b = map(int, input().split())
    h_list.append(a)
    w_list.append(b)

h_list = compress(h_list)
w_list = compress(w_list)

for i in range(N):
    print(h_list[i], w_list[i])

