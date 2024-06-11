# 解説AC
# 塔の高さの差分を式に落とし込む。

a, b = map(int, input().split())

print((b - a) * (b - a + 1) // 2 - b)
